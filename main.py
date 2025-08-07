import json
import os
from tabulate import tabulate

file_path = os.path.join(os.path.dirname(__file__), "tasks.json")
if not os.path.exists(file_path):
    with open(file_path, "w") as file:
        json.dump([], file)

def create_task(task):
    with open(file_path, "r") as file:
        data = json.load(file)
    if not data:
        data = [{"id": 1, "task": task}]
    else:
        max_id = max(data, key=lambda x: x.get("id", float("-inf")))["id"] + 1
        data.append({'id': max_id, 'task': task})
    with open(file_path, "w") as file:
        json.dump(data, file)

def get_tasks():
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def delete_task(task_id):
    with open(file_path, "r") as file:
        data = json.load(file)
    for i, task in enumerate(data):
        if task.get("id") == task_id:
            del data[i]
            with open(file_path, "w") as file:
                json.dump(data, file)
            return
    print_message("Task not found. Please enter a valid task ID.")


def format_task_list(tasks):
    print_message("Full list of tasks is shown below:", 34)
    table_data = [[item['id'], item['task']] for item in tasks]
    print(tabulate(table_data, headers=["ID", "Task"], tablefmt="grid") + "\n")

def print_message(message, color=31):
    print(f"\033[{color};1m\n{message}\033[0m\n")

while True:
    try:
        option = int(input(f"Please select an option:\n1. Add Task.\n2. View Tasks.\n3. Delete Task.\nEnter option number: "))
        if option == 1:
            input_text = str(input(f"Enter and submit task: "))
            create_task(input_text)
            print_message("Task created successfully.", 32)
        if option == 3:
            format_task_list(get_tasks())
            task_id = int(input(f"Please enter the task ID to delete: "))
            delete_task(task_id)
            print_message(f"Task under ID {task_id} has been successfully deleted.", 32)
        elif option > 3 or option < 1:
            print_message("Please select from options 1-3")
        format_task_list(get_tasks())
    except ValueError:
        print_message("Please enter a number")
    except KeyboardInterrupt:
        print_message("Program stopped by user")
        break