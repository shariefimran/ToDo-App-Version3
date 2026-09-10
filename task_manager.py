priority_options = {
        "1" : "Low",
        "2" : "Medium",
        "3" : "High"
    }
category_options={
     "1":"Work",
        "2":"Learning",
        "3":"Personal",
        "4":"Other"
}
   


def display_tasks(tasks):
    """Display all tasks."""

    if not tasks:
        print("There are no tasks to display")
    else:
        for index, task in enumerate(tasks, start=1):
            priority = task.get("priority","Medium")
            category = task.get("category","Other")
            if task["completed"]:
                print(f"{index}. ✔️ {task['name']} | priority : {priority} | category : {category}")
            else:
                print(f"{index}. {task['name']} | priority : {priority} | category : {category}")


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
        if task.get("priority","Medium") == "High"
    ]

    high_priority_count=len(high_priority_tasks)

    low_priority_tasks = [
           task
           for task in tasks
           if task.get("priority","Medium") == "Low"
       ]
   
    low_priority_count=len(low_priority_tasks)

    Medium_priority_tasks = [
               task
               for task in tasks
               if task.get("priority","Medium") == "Medium"
           ]
       
    Medium_priority_count=len(Medium_priority_tasks)
   

    print("========== Task Summary =========")
    print(f"Total Tasks : {total_tasks}")
    print(f"Completed Tasks : {completed_count}")
    print(f"Pending Tasks : {pending_count}")
    print(f"High priority tasks are : {high_priority_count}")
    print(f"low priority tasks are : {low_priority_count}")
    print(f"Medium priority tasks are : {Medium_priority_count}")

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

def add_task(tasks):
    """Add a new task."""

    task_to_add = input(
        "Enter the task name to add: "
    ).strip().lower()

    for task in tasks:
        if task["name"].lower() == task_to_add:
            print("Task already exists")
            return False
    # priority_options = {
    #     "1" : "Low",
    #     "2" : "Medium",
    #     "3" : "High"
    # }
    priority_choice=input("enter the priority").strip()

    if priority_choice in priority_options:
        priority=priority_options[priority_choice]
    else:
        print("Please enter the valid priority number")
        return False
  
     
    category_choice = input("enter the category").strip()

    if category_choice in category_options:
        category=category_options[category_choice]
    else:
        print("Please enter a valid category number")
        return False

    new_task = {
        "name": task_to_add,
        "completed": False,
        "priority":priority,
        "category": category
    }

    tasks.append(new_task)

    print(f"{task_to_add} added successfully")
    return True


def delete_task(tasks):
    """Delete a task."""

    if not tasks:
        print("There are no tasks to delete.")
        return False

    display_tasks(tasks)

    try:
        task_to_delete = int(
            input("Enter the task number to delete: ")
        )

    except ValueError:
        print("Please enter a valid number.")
        return False

    if 1 <= task_to_delete <= len(tasks):
        removed_task = tasks.pop(task_to_delete - 1)

        print(
            f"{removed_task['name']} deleted successfully"
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
            input("Enter the task number to edit: ")
        )

    except ValueError:
        print("Please enter a valid number to edit.")
        return False

    if 1 <= task_to_edit <= len(tasks):

        new_task = input(
            "Enter the new task: "
        ).strip().lower()

        for index, task in enumerate(tasks, start=1):
            if (
                task["name"] == new_task
                and index != task_to_edit
            ):
                print("This task already exists.")
                return False

        old_task_name = tasks[task_to_edit - 1]["name"]

        tasks[task_to_edit - 1]["name"] = new_task

        print(
            f"{old_task_name} updated with {new_task}"
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
            input("Enter the task number to mark: ")
        )

    except ValueError:
        print(
            "Please enter a valid task number "
            "to mark as completed."
        )
        return False

    if 1 <= completed_task <= len(tasks):

        if tasks[completed_task - 1]["completed"]:
            print("Task is already completed.")
            return False

        else:
            tasks[completed_task - 1]["completed"] = True

            print(
                f"{tasks[completed_task - 1]['name']} "
                "marked as completed."
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

    for index, task in enumerate(tasks, start=1):

        if find_task in task["name"].lower():
            print(f"{index}. {task['name']}")
            found = True

    if not found:
        print("Task not found.")
        return False

    return True