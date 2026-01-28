from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path
import os

# -------------------------------------------------
# Basic app setup
# -------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "todos.db"

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")


# -------------------------------------------------
# Database helpers
# -------------------------------------------------
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    conn.commit()
    conn.close()


# -------------------------------------------------
# Routes
# -------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()

    if request.method == "POST":
        task = request.form.get("task", "").strip()

        if not task:
            flash("Task cannot be empty", "error")
        else:
            conn.execute(
                "INSERT INTO todos (task, completed) VALUES (?, 0)",
                (task,)
            )
            conn.commit()
            flash("Task added successfully", "success")

        conn.close()
        return redirect(url_for("index"))

    todos = conn.execute(
        "SELECT id, task, completed FROM todos ORDER BY id DESC"
    ).fetchall()
    conn.close()

    return render_template("index.html", todos=todos)


@app.route("/complete/<int:todo_id>")
def complete(todo_id):
    conn = get_db_connection()
    conn.execute(
        """
        UPDATE todos
        SET completed = CASE completed
            WHEN 1 THEN 0
            ELSE 1
        END
        WHERE id = ?
        """,
        (todo_id,)
    )
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    conn = get_db_connection()
    conn.execute(
        "DELETE FROM todos WHERE id = ?",
        (todo_id,)
    )
    conn.commit()
    conn.close()
    flash("Task deleted", "success")
    return redirect(url_for("index"))


# -------------------------------------------------
# App entry point
# -------------------------------------------------
if __name__ == "__main__":
    init_db()
    app.run(debug=True)
