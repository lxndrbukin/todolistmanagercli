task_list = []

def create_task(task):
    task_list.append({'id': len(task_list) + 1, 'task': task})

def get_tasks():
    return task_list

def delete_task(task_id):
    del task_list[task_id - 1]

def format_task_list(tasks):
    print("*******\nTASKS LIST:\n")
    for item in tasks:
        print(f"{item['id']}. {item['task']}")
    print("*******")


while True:
    try:
        option = int(input(f"Please select an option:\n1. Add Task.\n2. View Tasks.\n3. Delete Task.\nEnter option number: "))
        if option == 1:
            task = input(f"Enter and submit task: ")
            create_task(task)
            print(get_tasks())
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