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

- `main.py`: The main Python script containing the task management logic.
- `tasks.json`: The JSON file where tasks are stored (automatically created if it doesn't exist).

## Code Overview

- **Task Storage**: Tasks are stored in `tasks.json` as a list of dictionaries, each with an `id` and `task` field.
- **Functions**:
  - `create_task(task)`: Adds a new task with an auto-incremented ID.
  - `get_tasks()`: Retrieves all tasks from the JSON file.
  - `delete_task(task_id)`: Deletes a task by its ID.
  - `format_task_list(tasks)`: Displays tasks in a tabular format using the `tabulate` library.
  - `print_message(message, color)`: Prints color-coded messages to the console.
- **Main Loop**: A `while` loop provides a menu-driven interface, handling user input and exceptions (e.g., invalid input, `Ctrl+C`).

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
