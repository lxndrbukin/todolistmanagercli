import json
import os
from tabulate import tabulate

class TaskManager:
    def __init__(self, file_path=os.path.join(os.path.dirname(__file__), "tasks.json")):
        self._file_path = file_path
    
    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, path):
        self._file_path = path

    def fetch_data(self):
        with open(self.file_path, "r") as file:
            data = json.load(file)
        return data

    def save_data(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file)

    def create_entry(self, task):
        data = self.fetch_data()
        if not data:
            data = [{"id": 1, "task": task}]
        else:
            max_id = max(data, key=lambda x: x.get("id", float("-inf")))["id"] + 1
            data.append({'id': max_id, 'task': task})
        self.save_data(data)

    def edit_entry(self, task_id, update):
        data = self.fetch_data()
        if not data:
            self.print_message("Task list empty")
        for task in data:
            if task["id"] == task_id:
                task["task"] = update 
        self.save_data(data)
        
    def remove_entry(self, task_id):
        data = self.fetch_data()
        for i, task in enumerate(data):
            if task.get("id") == task_id:
                del data[i]
                self.save_data(data)
                return
    
    @staticmethod
    def print_message(message, color=31):
        print(f"\033[{color};1m\n{message}\033[0m\n")

    def format_task_list(self, tasks):
        self.print_message("Full list of tasks is shown below:", 34)
        table_data = [[item['id'], item['task']] for item in tasks]
        print(tabulate(table_data, headers=["ID", "Task"], tablefmt="grid") + "\n")

    def run_cli(self):
        while True:
            try:
                options = ["Add Task", "View Tasks", "Edit Task", "Delete Task"]
                print("Please select an option:")
                for i, option in enumerate(options, 1):
                    print(f"{i}. {option}")
                selected = int(input(
                    f"Enter option number: "))
                if selected == 1:
                    input_text = str(input(f"Enter and submit task: "))
                    self.create_entry(input_text)
                    self.print_message("Task created successfully.", 32)
                if selected == 3:
                    self.format_task_list(self.fetch_data())
                    task_id = int(input(f"Please enter the task ID to edit: "))
                    task_update = str(input("Please enter the updated task:\n"))
                    self.edit_entry(task_id, task_update)
                    self.print_message(f"Task under ID {task_id} has been successfully updated.", 32)
                if selected == 4:
                    self.format_task_list(self.fetch_data())
                    task_id = int(input(f"Please enter the task ID to delete: "))
                    self.remove_entry(task_id)
                    self.print_message(f"Task under ID {task_id} has been successfully deleted.", 32)
                elif selected > len(options) or selected < 1:
                    self.print_message(f"Please select from options 1-{len(options)}")
                self.format_task_list(self.fetch_data())
            except ValueError:
                self.print_message("Please enter a number")
            except KeyboardInterrupt:
                self.print_message("Program stopped by user")
                break

if __name__ == "__main__":
    TaskManager().run_cli()