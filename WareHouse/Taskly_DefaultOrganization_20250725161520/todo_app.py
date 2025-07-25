'''
TodoApp class to manage the Todo list
'''
from task import Task
class TodoApp:
    def __init__(self):
        self.tasks = []
    def add_task(self, task_name, task_description):
        new_task = Task(task_name, task_description)
        self.tasks.append(new_task)
    def remove_task(self, task_index):
        try:
            task_index = int(task_index)
            if task_index < 1 or task_index > len(self.tasks):
                print("Invalid task index. Please enter a valid index.")
            else:
                del self.tasks[task_index - 1]
        except ValueError:
            print("Invalid input. Please enter a valid integer for the task index.")
    def display_tasks(self):
        if self.tasks:
            for index, task in enumerate(self.tasks):
                print(f"Task {index + 1}: {task.task_name} - {task.task_description}")
        else:
            print("No tasks in the list.")
    def run(self):
        while True:
            print("\nTodo App Menu:")
            print("1. Add Task")
            print("2. Remove Task")
            print("3. Display Tasks")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                task_name = input("Enter task name: ")
                task_description = input("Enter task description: ")
                self.add_task(task_name, task_description)
            elif choice == "2":
                task_index = input("Enter task index to remove: ")
                self.remove_task(task_index)
            elif choice == "3":
                self.display_tasks()
            elif choice == "4":
                print("Exiting Todo App.")
                break
            else:
                print("Invalid choice. Please try again.")