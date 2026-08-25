import json


def save_tasks(tasks):
    """Save all tasks to a file."""

    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


def load_tasks():
    """Load tasks from the file."""

    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    converted_tasks = []

    for task in tasks:
        if isinstance(task, str):
            converted_tasks.append({
                "name": task,
                "completed": False
            })
        else:
            converted_tasks.append(task)

    return converted_tasks