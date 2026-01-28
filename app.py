from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import tomli
from pathlib import Path

# Load configuration from TOML file
config_path = Path(__file__).parent / "config.toml"
with open(config_path, "rb") as f:
    config = tomli.load(f)

app = Flask(__name__)
app.secret_key = "your-secret-key-here"

# Database setup
DATABASE = config["database"]["filename"]

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    todos = conn.execute('SELECT * FROM todos ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('index.html', todos=todos, config=config)

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get('task', '').strip()
    max_length = config["settings"]["max_todo_length"]
    
    if not task:
        flash('Task cannot be empty!', 'error')
    elif len(task) > max_length:
        flash(f'Task cannot exceed {max_length} characters!', 'error')
    else:
        conn = get_db_connection()
        conn.execute('INSERT INTO todos (task) VALUES (?)', (task,))
        conn.commit()
        conn.close()
        flash('Task added successfully!', 'success')
    
    return redirect(url_for('index'))

@app.route('/toggle/<int:todo_id>')
def toggle_todo(todo_id):
    conn = get_db_connection()
    conn.execute('UPDATE todos SET completed = NOT completed WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(
        debug=config["app"]["debug"],
        host=config["app"]["host"],
        port=config["app"]["port"]
    )
