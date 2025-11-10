# Task Manager CLI (OOP Version)

A modern, **object-oriented command-line interface (CLI)** application for managing tasks in Python. This tool supports **adding, viewing, editing, and deleting** tasks stored in a JSON file, with a clean class-based design, **in-memory caching for performance**, formatted output using `tabulate`, and color-coded console feedback.

---

## Features

- **Add Tasks**: Create new tasks with auto-incremented unique IDs.
- **View Tasks**: Display all tasks in a beautifully formatted table using `tabulate`.
- **Edit Tasks**: Update existing tasks by ID.
- **Delete Tasks**: Remove tasks by entering their ID.
- **Persistent Storage**: Tasks saved in `tasks.json` (or custom filename via CLI argument).
- **In-Memory Caching**: Data loaded once at startup — **instant views and edits**, disk writes only on changes.
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

### Basic Run (Default File: `tasks.json`)

```bash
python main.py
```

### Run with Custom Task File

```bash
python main.py myproject
# Creates/uses: myproject.json
```

> **Perfect for multiple task lists** (personal, work, study, etc.)

### Interactive Menu

```
Please select an option:
1. Add Task
2. View Tasks
3. Edit Task
4. Delete Task
5. Exit
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

#### Edit a Task

```
Enter option number: 3
Full list of tasks is shown below:
+----+----------------------------------+
| ID | Task                             |
+----+----------------------------------+
| 1  | Finish project documentation     |
+----+----------------------------------+
Please enter the task ID to edit: 1
Please enter the updated task:
Update documentation with examples

Task under ID 1 has been successfully updated.
```

#### Delete a Task

```
Enter option number: 4
Full list of tasks is shown below:
+----+------------------------------------+
| ID | Task                               |
+----+------------------------------------+
| 1  | Update documentation with examples |
+----+------------------------------------+
Please enter the task ID to delete: 1

Task under ID 1 has been successfully deleted.
```

> **Exit**: Select option 5 or press `Ctrl+C` to stop the program.

---

## File Structure

```
.
├── main.py           # Main script with TaskManager class and CLI
├── tasks.json        # Default task file (auto-created)
├── work.json         # Example custom file (created via `python main.py work`)
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
| `__init__()`                   | Accepts CLI argument for custom filename; loads data into `self.data` |
| `file_path`                    | Property with getter/setter for JSON file location |
| `fetch_data()` / `save_data()` | Load once at start; save only on changes           |
| `create_entry(task)`           | Adds a new task with auto-incremented ID           |
| `edit_entry(task_id, update)`  | Updates task text by ID                            |
| `remove_entry(task_id)`        | Deletes task by ID                                 |
| `format_task_list(tasks)`      | Prints tasks in a grid table using `tabulate`      |
| `print_message()`              | Static method for colored console output           |
| `run_cli()`                    | Main interactive loop                              |

---

## Performance Note

- **In-memory caching** (`self.data`) means:
  - **Instant** task listing and editing
  - Disk reads: **only once** at startup
  - Disk writes: **only when data changes**
- Feels **snappy** even with hundreds of tasks

---

## Notes

- The JSON file is **automatically created** if it doesn’t exist.
- Task IDs are **auto-incremented** based on the highest existing ID.
- Invalid inputs (non-integers, out-of-range options) are handled with clear red error messages.
- ANSI color codes work in most modern terminals (VS Code, iTerm, Windows Terminal, etc.).
- Use `python main.py <name>` to manage **multiple independent task lists** (e.g., `python main.py bootdev`, `python main.py ai-roadmap`).

---

## Future Improvements

- [x] Add **edit task** functionality  
- [x] Support **multiple task files** via CLI argument  
- [x] **In-memory caching** for performance  
- [ ] Support **task priorities/categories** (e.g. Low/Medium/High)  
- [ ] Add **due dates** and reminders  
- [ ] Implement **search/filter** by keyword  
- [ ] Add confirmation prompt before deletion  
- [ ] Export tasks to CSV or Markdown  
