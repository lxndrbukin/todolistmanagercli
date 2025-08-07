# Task Manager CLI

A simple command-line interface (CLI) application for managing tasks, built with Python. This tool allows users to add, view, and delete tasks stored in a JSON file.

## Features

- **Add Tasks**: Create new tasks with a unique ID.
- **View Tasks**: Display all tasks in a formatted table.
- **Delete Tasks**: Remove tasks by specifying their ID.
- Persistent storage using a JSON file (`tasks.json`).
- Color-coded console messages for better user experience.

## Requirements

- Python 3.x
- `tabulate` library (`pip install tabulate`)

## Installation

1. Clone or download this repository.
2. Install the required Python package:
   ```bash
   pip install tabulate
   ```
3. Ensure you have a Python environment set up (Python 3.x recommended).

## Usage

1. Run the script:
   ```bash
   python task_manager.py
   ```
2. Follow the on-screen prompts to:
   - **Add a task**: Select option 1 and enter the task description.
   - **View tasks**: Select option 2 to see all tasks in a table.
   - **Delete a task**: Select option 3, view the task list, and enter the ID of the task to delete.
3. To exit, press `Ctrl+C`.

### Example Interaction

```bash
Please select an option:
1. Add Task.
2. View Tasks.
3. Delete Task.
Enter option number: 1
Enter and submit task: Buy groceries
Task created successfully.

Full list of tasks is shown below:
+----+---------------+
| ID | Task          |
+----+---------------+
| 1  | Buy groceries |
+----+---------------+
```

## File Structure

- `task_manager.py`: The main Python script containing the task management logic.
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

- The `tasks.json` file is created in the same directory as the script if it doesn't already exist.
- Invalid inputs (e.g., non-numeric input for options or task IDs) are handled with error messages.
- The program uses ANSI color codes for console output (e.g., green for success, red for errors).

## Future Improvements

- Add task editing functionality.
- Support task priorities or categories.
- Add confirmation prompts for task deletion.
- Implement task sorting or filtering options.
