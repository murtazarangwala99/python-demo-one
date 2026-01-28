# Flask TODO Application

A simple and elegant TODO application built with Flask and configured using TOML.

## Add, complete, and delete tasks

## Project Structure

```
.
├── app.py                 # Main Flask application
├── config.toml           # Configuration file
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # HTML template
└── todos.db              # SQLite database (created automatically)
```

## Setup (Recommended)

```
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Usage

- **Add a task**: Type your task in the input field and click "Add"
- **Complete a task**: Click the "Done" button or the checkbox
- **Delete a task**: Click the "Delete" button
- **Undo completion**: Click "Undo" on completed tasks

## Requirements

- Python 3.7+
- Flask 3.0.0
- tomli 2.0.1

## License

Free to use and modify as needed.
