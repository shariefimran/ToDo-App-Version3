import json


def save_tasks(tasks):
    """Save all tasks to a file."""

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def migrate_task(task):
    """Migrate an old task to the V4 task structure."""

    task["priority"] = task.get("priority", "Medium")
    task["category"] = task.get("category", "Other")
    task["due_date"] = task.get("due_date", None)

    return task


def load_tasks():
    """Load tasks from the file and migrate old tasks."""

    with open("tasks.json", "r") as file:
        tasks = json.load(file)

    converted_tasks = []
    migration_needed = False

    for task in tasks:

        # Handle very old tasks stored as strings
        if isinstance(task, str):
            task = {
                "name": task,
                "completed": False
            }
            migration_needed = True

        # Check whether V4 fields are missing
        if "priority" not in task:
            migration_needed = True

        if "category" not in task:
            migration_needed = True

        if "due_date" not in task:
            migration_needed = True

        # Add missing V4 fields
        task = migrate_task(task)

        converted_tasks.append(task)

    # Save migrated data permanently
    if migration_needed:
        save_tasks(converted_tasks)

    return converted_tasks