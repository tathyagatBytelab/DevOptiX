
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task.strip():
            raise ValueError("Task cannot be empty")

        self.tasks.append({
            "task": task,
            "completed": False
        })

    def list_tasks(self):
        return self.tasks

    def complete_task(self, index):
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Task not found")

        self.tasks[index]["completed"] = True


if __name__ == "__main__":
    manager = TaskManager()

    manager.add_task("Learn DevOps")
    manager.add_task("Build DevOptiX")

    manager.complete_task(0)

    print("DevOptiX Task Manager")
    for task in manager.list_tasks():
        status = "Completed" if task["completed"] else "Pending"
        print(f'{task["task"]}: {status}')
