import json

def create_task(task):
    with open("tasks.json", "r") as file:
        data = json.load(file)
    data.append({'id': len(data) + 1, 'task': task})
    with open("tasks.json", "w") as file:
        json.dump(data, file)

def get_tasks():
    with open("tasks.json", "r") as file:
        data = json.load(file)
    return data

def delete_task(task_id):
    with open("tasks.json", "r") as file:
        data = json.load(file)
    del data[task_id - 1]
    with open("tasks.json", "w") as file:
        json.dump(data, file)

def format_task_list(tasks):
    print("\n**************\nTASKS LIST:")
    for item in tasks:
        print(f"{item['id']}. {item['task']}")
    print("**************\n")


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
    except ValueError:
        print("Please enter a number")
    except KeyboardInterrupt:
        print("\nProgram stopped")
        break