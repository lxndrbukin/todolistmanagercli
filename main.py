import json
import os

file_path = os.path.join(os.path.dirname(__file__), "tasks.json")

def create_task(task):
    with open(file_path, "r") as file:
        data = json.load(file)
    data.append({'id': max(data, key=lambda x: x.get("id", float("-inf")))["id"] + 1, 'task': task})
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

def format_task_list(tasks):
    print("\n**************\nID  TASK:")
    for item in tasks:
        print(f"{item['id']}.  {item['task']}")
    print("**************\n")

def print_error(message):
    print(f"\033[31;1m\n{message}\033[0m\n")

while True:
    try:
        option = int(input(f"Please select an option:\n1. Add Task.\n2. View Tasks.\n3. Delete Task.\nEnter option number: "))
        if option == 1:
            task = input(f"Enter and submit task: ")
            create_task(task)
            format_task_list(get_tasks())
        if option == 2:
            format_task_list(get_tasks())
        if option == 3:
            format_task_list(get_tasks())
            task_id = int(input(f"Please enter the task ID to delete: "))
            delete_task(task_id)
            format_task_list(get_tasks())
        elif option > 3 or option < 1:
            print_error("Please select from options 1-3")
    except ValueError:
        print_error("Please enter a number")
    except KeyboardInterrupt:
        print_error("Program stopped by user")
        break