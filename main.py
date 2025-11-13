import json
import os
import sys
from tabulate import tabulate

class TaskManager:
    def __init__(self, file_path=f"{sys.argv[1]}.json" if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "tasks.json")):
        self._file_path = file_path
        self.data = self.fetch_data()
        self.search_results = []
    
    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, path):
        self._file_path = path

    def fetch_data(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r") as file:
            data = json.load(file)
        return data

    def save_data(self):
        with open(self.file_path, "w") as file:
            json.dump(self.data, file)

    def create_entry(self, task):
        if not self.data:
            self.data = [{"id": 1, "entry": task["entry"], "priority": task["priority"]}]
        else:
            max_id = max(self.data, key=lambda x: x.get("id", float("-inf")))["id"] + 1
            self.data.append({"id": max_id, "entry": task["entry"], "priority": task["priority"]})
        self.save_data()

    def edit_entry(self, task_id, update):
        if not self.data:
            self.print_message("Task list empty")
        for task in self.data:
            if task["id"] == task_id:
                task["entry"] = update
        self.save_data()
        
    def remove_entry(self, task_id):
        for i, task in enumerate(self.data):
            if task.get("id") == task_id:
                del self.data[i]
                self.save_data()
                return

    def search(self, query):
        self.search_results = []
        split_query = query.lower().split()
        results = []
        for task in self.data:
            if any(term in task["entry"].lower() for term in split_query):
                results.append(task)
        for i, result in enumerate(results):
            split_result = result["entry"].split()
            for n, word in enumerate(split_result):
                if word.lower() in split_query:
                    split_result[n] = f"\033[1m{word}\033[0m"
            result["entry"] = " ".join(split_result)
            results[i] = result
        self.search_results = results

    @staticmethod
    def print_message(message, color=31):
        print(f"\033[{color};1m\n{message}\033[0m\n")

    @staticmethod
    def list_options(options):
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

    def format_task_list(self, tasks):
        self.print_message("Full list of found tasks is shown below:", 34)
        table_data = [[item["id"], item["entry"], item["priority"]] for item in tasks]
        print(tabulate(table_data, headers=["ID", "Task", "Priority"], tablefmt="grid") + "\n")

    def run_cli(self):
        while True:
            try:
                main_options = ["Add Task", "View Tasks", "Edit Task", "Delete Task", "Search", "Exit"]
                print("Please select an option:")
                self.list_options(main_options)
                selected = int(input(
                    f"Enter option number: "))
                if selected == 1:
                    input_text = str(input(f"Enter and submit task: "))
                    priority_list = ["Low", "Medium", "High"]
                    print("Priority options:")
                    self.list_options(priority_list)
                    priority = int(input("Select task priority: "))
                    self.create_entry({"entry": input_text, "priority": priority_list[priority - 1]})
                    self.print_message("Task created successfully.", 32)
                elif selected == 2:
                    self.format_task_list(self.fetch_data())
                elif selected == 3:
                    self.format_task_list(self.fetch_data())
                    task_id = int(input(f"Please enter the task ID to edit: "))
                    task_update = str(input("Please enter the updated task:\n"))
                    self.edit_entry(task_id, task_update)
                    self.print_message(f"Task under ID {task_id} has been successfully updated.", 32)
                elif selected == 4:
                    self.format_task_list(self.fetch_data())
                    task_id = int(input(f"Please enter the task ID to delete: "))
                    self.remove_entry(task_id)
                    self.print_message(f"Task under ID {task_id} has been successfully deleted.", 32)
                elif selected == 5:
                    if not self.data:
                        self.print_message("Task list empty")
                    query = str(input(f"Please enter keyword(s): "))
                    self.search(query)
                    self.format_task_list(self.search_results)
                elif selected == 6:
                    self.print_message("Program stopped")
                    break
                elif selected > len(main_options) or selected < 1:
                    self.print_message(f"Please select from options 1-{len(main_options)}")
            except ValueError:
                self.print_message("Please enter a number")
            except KeyboardInterrupt:
                self.print_message("Program stopped by user")
                break

if __name__ == "__main__":
    TaskManager().run_cli()