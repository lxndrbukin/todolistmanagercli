# Task Manager CLI (OOP Version)

A modern, object-oriented command-line interface (CLI) application for managing tasks in Python. This tool allows users to **add**, **view**, and **delete** tasks stored in a JSON file, with a clean class-based design, formatted output using `tabulate`, and color-coded console feedback.

---

## Features

- **Add Tasks**: Create new tasks with auto-incremented unique IDs.
- **View Tasks**: Display all tasks in a beautifully formatted table using `tabulate`.
- **Delete Tasks**: Remove tasks by entering their ID.
- **Persistent Storage**: Tasks saved in `tasks.json` (auto-created if missing).
- **Color-Coded Feedback**: Success (green), errors (red), and info (blue) messages using ANSI codes.
- **Robust Error Handling**: Handles invalid input, file errors, and graceful exit on `Ctrl+C`.

---

## Requirements

- Python 3.8+
- `tabulate` library

```bash
pip install tabulate
```

---

## Installation

1. Clone or download this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   or
   ```bash
   pip install tabulate
   ```

---

## Usage

Run the application:

```bash
python main.py
```

### Interactive Menu

```
Please select an option:
1. Add Task
2. View Tasks
3. Delete Task
Enter option number:
```

#### Add a Task

```
Enter option number: 1
Enter and submit task: Finish project documentation

Task created successfully.
```

#### View Tasks

```
Full list of tasks is shown below:
+----+----------------------------------+
| ID | Task                             |
+----+----------------------------------+
| 1  | Finish project documentation     |
+----+----------------------------------+
```

#### Delete a Task

```
Enter option number: 3
Full list of tasks is shown below:
+----+----------------------------------+
| ID | Task                             |
+----+----------------------------------+
| 1  | Finish project documentation     |
+----+----------------------------------+
Please enter the task ID to delete: 1

Task under ID 1 has been successfully deleted.
```

> **Exit**: Press `Ctrl+C` to stop the program gracefully.

---

## File Structure

```
.
├── main.py           # Main script with TaskManager class and CLI
├── tasks.json        # Auto-generated JSON file storing tasks
└── README.md
```

### Example `tasks.json`

```json
[
  {
    "id": 1,
    "task": "Buy groceries"
  },
  {
    "id": 2,
    "task": "Call mom"
  }
]
```

---

## Code Overview (OOP Design)

The application is built around the `TaskManager` class:

| Method                         | Description                                        |
| ------------------------------ | -------------------------------------------------- |
| `__init__()`                   | Initializes with default `tasks.json` path         |
| `file_path`                    | Property with getter/setter for JSON file location |
| `fetch_data()` / `save_data()` | Load/save tasks from/to JSON                       |
| `create_entry(task)`           | Adds a new task with auto-incremented ID           |
| `remove_entry(task_id)`        | Deletes task by ID                                 |
| `format_task_list(tasks)`      | Prints tasks in a grid table using `tabulate`      |
| `print_message()`              | Static method for colored console output           |
| `run_cli()`                    | Main interactive loop                              |

---

## Notes

- The `tasks.json` file is **automatically created** in the script directory if it doesn’t exist.
- Task IDs are **auto-incremented** based on the highest existing ID.
- Invalid inputs (non-integers, out-of-range options) are handled with clear red error messages.
- ANSI color codes work in most modern terminals (VS Code, iTerm, Windows Terminal, etc.).
- The `file_path` can be customized via the setter if needed.

---

## Future Improvements

- [ ] Add **edit task** functionality
- [ ] Support **task priorities** (Low/Medium/High)
- [ ] Add **due dates** and reminders
- [ ] Implement **search/filter** by keyword
- [ ] Add confirmation prompt before deletion
- [ ] Export tasks to CSV or Markdown
