'''
Task class to represent a single task in the Todo list
'''
class Task:
    def __init__(self, task_name, task_description):
        self.task_name = task_name
        self.task_description = task_description
        self.task_status = "Pending"
    def update_status(self, new_status):
        self.task_status = new_status