# Flask TODO Application

A simple and elegant TODO application built with Flask and configured using TOML.

## Features

- ✅ Add, complete, and delete tasks
- 📝 Configuration via TOML file
- 💾 SQLite database for persistent storage
- 🎨 Modern, responsive UI
- ⚡ Flash messages for user feedback

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

## Configuration (config.toml)

The application is configured using a TOML file with the following options:

- **[app]**: Application settings (name, debug, host, port)
- **[database]**: Database filename
- **[settings]**: Application behavior (max task length, pagination)

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

## Usage

- **Add a task**: Type your task in the input field and click "Add"
- **Complete a task**: Click the "Done" button or the checkbox
- **Delete a task**: Click the "Delete" button
- **Undo completion**: Click "Undo" on completed tasks

## Configuration Options

Edit `config.toml` to customize:

- `debug`: Enable/disable debug mode
- `host`: Server host (default: 0.0.0.0)
- `port`: Server port (default: 5000)
- `max_todo_length`: Maximum characters per task (default: 200)
- `items_per_page`: Number of items per page (default: 10)

## Requirements

- Python 3.7+
- Flask 3.0.0
- tomli 2.0.1

## License

Free to use and modify as needed.
