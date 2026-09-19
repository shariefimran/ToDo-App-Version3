from datetime import datetime, date
from menu import print_header
from math import ceil
from logger import log_activity
from config import TASK_ID_START,PAGE_SIZE,MAX_TASK_NAME_LENGTH


priority_options = {
    "1": "Low",
    "2": "Medium",
    "3": "High"
}


category_options = {
    "1": "Work",
    "2": "Learning",
    "3": "Personal",
    "4": "Other"
}


priority_order = {
    "High": 1,
    "Medium": 2,
    "Low": 3
}


def print_separator():
    print("-" * 40)


def display_tasks(tasks, start_number=1):
    """Display all tasks."""

    if not tasks:
        print("There are no tasks to display")

    else:
        print_header("TASKS")

        for index, task in enumerate(tasks, start=start_number):

            priority = task.get("priority", "Medium")
            category = task.get("category", "Other")
            due_date = task.get("due_date") or "Not Set"

            status = (
                "✔️ Completed"
                if task["completed"]
                else "❌ Pending"
            )

            print(f"{index}. {task['name']}")
            print(f" {'Status':<10} : {status}")
            print(f" {'Task ID':<10} : {task['task_id']}")
            print(f" {'Priority':<10} : {priority}")
            print(f" {'Category':<10} : {category}")
            print(f" {'Due Date':<10} : {due_date}")
            print()

            if index < start_number + len(tasks) - 1:
                print_separator()


def display_tasks_paginated(tasks):
    """Display tasks page by page."""

    page_size = PAGE_SIZE
    page = 1
    total_pages = ceil(len(tasks) / page_size)

    while True:

        start = (page - 1) * page_size
        end = start + page_size

        page_tasks = tasks[start:end]

        print(f"Page {page} of {total_pages}")

        display_tasks(page_tasks, start + 1)

        print("[N] Next [P] Previous [B] Back")

        navigation = input(
            "Enter your choice: "
        ).strip().lower()

        if navigation == "n" and page < total_pages:
            page += 1

        elif navigation == "p" and page > 1:
            page -= 1

        elif navigation == "b":
            break

        else:
            print(
                "Invalid choice. Please enter N, P, or B."
            )


def task_summary(tasks):
    """Display the task summary."""

    total_tasks = len(tasks)

    completed_tasks = [
        task
        for task in tasks
        if task["completed"]
    ]

    completed_count = len(completed_tasks)

    pending_tasks = [
        task
        for task in tasks
        if not task["completed"]
    ]

    pending_count = len(pending_tasks)

    high_priority_tasks = [
        task
        for task in tasks
        if task.get("priority", "Medium") == "High"
    ]

    high_priority_count = len(high_priority_tasks)

    low_priority_tasks = [
        task
        for task in tasks
        if task.get("priority", "Medium") == "Low"
    ]

    low_priority_count = len(low_priority_tasks)

    medium_priority_tasks = [
        task
        for task in tasks
        if task.get("priority", "Medium") == "Medium"
    ]

    medium_priority_count = len(medium_priority_tasks)

    work_tasks = [
        task
        for task in tasks
        if task.get("category", "Other") == "Work"
    ]

    work_count = len(work_tasks)

    learning_tasks = [
        task
        for task in tasks
        if task.get("category", "Other") == "Learning"
    ]

    learning_count = len(learning_tasks)

    personal_tasks = [
        task
        for task in tasks
        if task.get("category", "Other") == "Personal"
    ]

    personal_count = len(personal_tasks)

    other_tasks = [
        task
        for task in tasks
        if task.get("category", "Other") == "Other"
    ]

    other_count = len(other_tasks)

    no_due_date = 0
    overdue = 0
    due_today = 0
    upcoming = 0

    for task in tasks:

        due_date = task.get("due_date")

        if not due_date:
            no_due_date += 1
            continue

        due_date = datetime.strptime(
            due_date,
            "%Y-%m-%d"
        ).date()

        if due_date < date.today():
            overdue += 1

        if due_date == date.today():
            due_today += 1

        if due_date > date.today():
            upcoming += 1

    print("========== Task Summary =========")

    print("\nTasks")
    print("--------------------------------")
    print(f"Total Tasks : {total_tasks}")
    print(f"Completed Tasks : {completed_count}")
    print(f"Pending Tasks : {pending_count}")

    print("\nPriority")
    print("----------------------------------------------")
    print(
        f"High priority tasks are : "
        f"{high_priority_count}"
    )
    print(
        f"Low priority tasks are : "
        f"{low_priority_count}"
    )
    print(
        f"Medium priority tasks are : "
        f"{medium_priority_count}"
    )

    print("\nCategory")
    print("------------------------------------")
    print(f"Work tasks : {work_count}")
    print(f"Personal tasks : {personal_count}")
    print(f"Other tasks : {other_count}")
    print(f"Learning tasks : {learning_count}")

    print("\nDue Dates")
    print("---------------------------------------------------")
    print(f"Overdue : {overdue}")
    print(f"Due Today : {due_today}")
    print(f"Upcoming : {upcoming}")
    print(f"No Due Date : {no_due_date}")


def filter_tasks(tasks, priority):
    """Filter tasks by priority."""

    filtered_tasks = [
        task
        for task in tasks
        if task.get("priority", "Medium") == priority
    ]

    if not filtered_tasks:
        print("There are no tasks with this priority.")
        return False

    for index, task in enumerate(filtered_tasks, start=1):

        print(
            f"{index}. {task['name']} | "
            f"Priority: {task.get('priority', 'Medium')}"
        )

    return True


def filter_task_by_category(tasks, category):
    """Filter tasks by category."""

    task_by_category = [
        task
        for task in tasks
        if task.get("category", "Other") == category
    ]

    if not task_by_category:
        print("There are no tasks with this category.")
        return False

    for index, task in enumerate(
        task_by_category,
        start=1
    ):

        print(
            f"{index}. {task['name']} | "
            f"Category: {task.get('category', 'Other')}"
        )

    return True


def generate_task_id(tasks):
    """Generate the next unique task ID."""

    if not tasks:
        return TASK_ID_START

    task_ids = [
        task["task_id"]
        for task in tasks
        if "task_id" in task
    ]

    if task_ids:
        return max(task_ids) + 1

    return TASK_ID_START


def add_task(tasks):
    """Add a new task."""

    task_to_add = input(
        "Enter the task name to add: "
    ).strip().lower()

    if not task_to_add:
        print("Task can't be empty")
        return False

    if len(task_to_add) > MAX_TASK_NAME_LENGTH:
        print("Task name is too long")
        return False

    for task in tasks:

        if task["name"].lower() == task_to_add:
            print("Task already exists")
            return False

    print("Priority Options:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    priority_choice = input(
        "Enter the priority: "
    ).strip()

    if priority_choice in priority_options:
        priority = priority_options[priority_choice]

    else:
        print("Please enter a valid priority number")
        return False

    print("Category Options")
    print("1. Work")
    print("2. Learning")
    print("3. Personal")
    print("4. Other")

    category_choice = input(
        "Enter the category: "
    ).strip()

    if category_choice in category_options:
        category = category_options[category_choice]

    else:
        print("Please enter a valid category number")
        return False

    due_date = input(
        "Enter the due date (YYYY-MM-DD): "
    ).strip()

    try:

        due_date = datetime.strptime(
            due_date,
            "%Y-%m-%d"
        ).date()

    except ValueError:

        print("Please enter a valid date")
        return False

    if due_date < date.today():

        print("Due date cannot be in the past")
        return False

    new_task = {
        "name": task_to_add,
        "completed": False,
        "priority": priority,
        "category": category,
        "due_date": due_date.strftime("%Y-%m-%d"),
        "task_id": generate_task_id(tasks)
    }

    tasks.append(new_task)

    log_activity(
        f"Added task : {new_task['name']} "
        f"(ID: {new_task['task_id']})"
    )

    print(
        f"{task_to_add} added successfully"
    )

    return True


def show_overdue_tasks(tasks):
    """Display overdue tasks."""

    overdue_found = False

    for task in tasks:

        due_date = task.get("due_date")

        if due_date:

            due_date = datetime.strptime(
                due_date,
                "%Y-%m-%d"
            ).date()

            if due_date < date.today():

                print(task["name"])
                overdue_found = True

    if not overdue_found:
        print("No overdue tasks found")


def show_due_tasks(tasks):

    today_due_date = False

    for task in tasks:

        due_date = task.get("due_date")

        if due_date:

            due_date = datetime.strptime(
                due_date,
                "%Y-%m-%d"
            ).date()

            if due_date == date.today():

                print(task["name"])
                today_due_date = True

    if not today_due_date:
        print("Due date is not today")


def show_upcoming_due_tasks(tasks):

    upcoming_due_date = False

    for task in tasks:

        due_date = task.get("due_date")

        if due_date:

            due_date = datetime.strptime(
                due_date,
                "%Y-%m-%d"
            ).date()

            if due_date > date.today():

                print(task["name"])
                upcoming_due_date = True

    if not upcoming_due_date:
        print("No upcoming tasks found")


def sort_tasks_by_priority(tasks):
    """Sort tasks based on priority."""

    sorted_tasks = sorted(
        tasks,
        key=lambda task:
        priority_order[
            task.get("priority", "Medium")
        ]
    )

    for task in sorted_tasks:

        print(
            f"{task['name']} | "
            f"Priority: "
            f"{task.get('priority', 'Medium')}"
        )


def due_date_key(task):

    due_date = task.get("due_date")

    if due_date:

        return datetime.strptime(
            due_date,
            "%Y-%m-%d"
        ).date()

    return date.max


def sort_tasks_by_due_date(tasks):
    """Sort tasks by due date."""

    sorted_tasks = sorted(
        tasks,
        key=due_date_key
    )

    for task in sorted_tasks:

        print(
            f"{task['name']} | "
            f"Due date: "
            f"{task.get('due_date', 'Not Set')}"
        )


def sort_task_alphabetically(tasks):
    """Sort tasks alphabetically."""

    sorted_task = sorted(
        tasks,
        key=lambda task:
        task["name"].lower()
    )

    for task in sorted_task:

        print(task["name"])


def delete_task(tasks):
    """Delete a task."""

    if not tasks:

        print("There are no tasks to delete.")
        return False

    display_tasks(tasks)

    try:

        task_to_delete = int(
            input(
                "Enter the task number to delete: "
            )
        )

    except ValueError:

        print("Please enter a valid number.")
        return False

    if 1 <= task_to_delete <= len(tasks):

        removed_task = tasks.pop(
            task_to_delete - 1
        )

        log_activity(
            f"Deleted task : {removed_task['name']} "
            f"(ID: {removed_task['task_id']})"
        )

        print(
            f"{removed_task['name']} "
            f"deleted successfully"
        )

        return True

    else:

        print("Invalid task number.")
        return False


def edit_task(tasks):
    """Edit an existing task."""

    if not tasks:

        print("There are no tasks to edit.")
        return False

    display_tasks(tasks)

    try:

        task_to_edit = int(
            input(
                "Enter the task number to edit: "
            )
        )

    except ValueError:

        print(
            "Please enter a valid number to edit."
        )

        return False

    if 1 <= task_to_edit <= len(tasks):

        new_task = input(
            "Enter the new task: "
        ).strip().lower()

        for index, task in enumerate(
            tasks,
            start=1
        ):

            if (
                task["name"] == new_task
                and index != task_to_edit
            ):

                print(
                    "This task already exists."
                )

                return False

        old_task_name = tasks[
            task_to_edit - 1
        ]["name"]

        task_id = tasks[
            task_to_edit - 1
        ]["task_id"]

        tasks[
            task_to_edit - 1
        ]["name"] = new_task

        log_activity(
            f"Edited task : "
            f"{old_task_name} to {new_task} "
            f"(ID: {task_id})"
        )

        print(
            f"{old_task_name} "
            f"updated with {new_task}"
        )

        return True

    else:

        print("Invalid task number.")
        return False


def mark_task_completed(tasks):
    """Mark a task as completed."""

    if not tasks:

        print("There are no tasks to mark.")
        return False

    display_tasks(tasks)

    try:

        completed_task = int(
            input(
                "Enter the task number to mark: "
            )
        )

    except ValueError:

        print(
            "Please enter a valid task number "
            "to mark as completed."
        )

        return False

    if 1 <= completed_task <= len(tasks):

        task = tasks[
            completed_task - 1
        ]

        if task["completed"]:

            print(
                "Task is already completed."
            )

            return False

        task["completed"] = True

        log_activity(
            f"Completed task : "
            f"{task['name']} "
            f"(ID: {task['task_id']})"
        )

        print(
            f"{task['name']} "
            f"marked as completed."
        )

        return True

    else:

        print("Invalid task number.")
        return False


def search_task(tasks):
    """Search for a task."""

    if not tasks:

        print("There are no tasks to search.")
        return False

    find_task = input(
        "Enter the task name to search: "
    ).strip().lower()

    found = False

    for index, task in enumerate(
        tasks,
        start=1
    ):

        if find_task in task["name"].lower():

            print(
                f"{index}. {task['name']}"
            )

            found = True

    if not found:

        print("Task not found.")
        return False

    return True


def bulk_delete_tasks(tasks):
    """Delete multiple tasks using Task IDs."""

    user_input = input(
        "Enter the task IDs to delete "
        "(comma separated): "
    ).strip()

    try:

        task_ids = [
            int(task_id.strip())
            for task_id in user_input.split(",")
        ]

    except ValueError:

        print(
            "Invalid Task ID. "
            "Please enter numbers separated by commas."
        )

        return False

    tasks_to_delete = [
        task
        for task in tasks
        if task["task_id"] in task_ids
    ]

    if not tasks_to_delete:

        print("No matching tasks found.")
        return False

    for task in tasks_to_delete:

        log_activity(
            f"Deleted task : "
            f"{task['name']} "
            f"(ID: {task['task_id']})"
        )

        tasks.remove(task)

    if len(tasks_to_delete) == 1:

        print("1 task deleted.")

    else:

        print(
            f"{len(tasks_to_delete)} tasks deleted."
        )

    return True


def bulk_complete_tasks(tasks):
    """Mark multiple tasks as completed using Task IDs."""

    user_input = input(
        "Enter the task IDs to complete "
        "(comma separated): "
    ).strip()

    try:

        task_ids = [
            int(task_id.strip())
            for task_id in user_input.split(",")
        ]

    except ValueError:

        print(
            "Invalid Task ID. "
            "Please enter numbers separated by commas."
        )

        return False

    completed_count = 0

    for task in tasks:

        if task["task_id"] in task_ids:

            if not task["completed"]:

                task["completed"] = True

                log_activity(
                    f"Completed task : "
                    f"{task['name']} "
                    f"(ID: {task['task_id']})"
                )

                completed_count += 1

    if completed_count == 0:

        print(
            "No pending matching tasks found."
        )

        return False

    if completed_count == 1:

        print(
            "1 task marked as completed."
        )

    else:

        print(
            f"{completed_count} "
            f"tasks marked as completed."
        )

    return True

