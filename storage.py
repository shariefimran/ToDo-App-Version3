import json

from task_manager import generate_task_id


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

    migration_needed = False

    # Handle very old tasks stored as strings
    for index, task in enumerate(tasks):
        if isinstance(task, str):
            tasks[index] = {
                "name": task,
                "completed": False
            }

            migration_needed = True

    # Generate Task IDs for tasks that don't have one
    for task in tasks:
        if "task_id" not in task:
            migration_needed = True
            task["task_id"] = generate_task_id(tasks)

    converted_tasks = []

    for task in tasks:

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


def export_tasks(tasks):
    """Export tasks to a separate JSON file."""

    if not tasks:
        print("There are no tasks to export.")
        return False

    with open("tasks_export.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print("Tasks exported successfully.")
    return True


def import_tasks():
    """Import tasks from the export file."""

    try:
        with open("tasks_export.json", "r") as file:
            tasks = json.load(file)

    except FileNotFoundError:
        print("Export file not found.")
        return False

    except json.JSONDecodeError:
        print("Export file contains invalid JSON.")
        return False

    print("Tasks imported successfully.")
    return tasks