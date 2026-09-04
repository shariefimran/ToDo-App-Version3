def display_tasks(tasks):
    """This function will be used to view the tasks."""

    if not tasks:
        print("There are no tasks to display")
    else:
        for index, task  in enumerate(tasks, start=1):
            if task["completed"]:
                print(f"{index}.✔️{task['name']}")
            else:

                print(f"{index}. {task['name']}")


# def add_task(tasks):
#     """This will add a task."""

#     task_to_add = input("Enter the task name to add: ").strip().lower()

#     if task_to_add not in tasks:
#         tasks.append(task_to_add)
#         print(f"{task_to_add} added successfully")
#         return True
#     else:
#         print("Entered task already present in the list.")
#         return False


def add_task(tasks):
    task_to_add=input("Enter the task name to add : ").strip().lower()
    for task in tasks:
        if task["name"].lower()==task_to_add:
            print("Task already exists")
            return False
    
    new_task={
                "name":task_to_add,
                "completed":False
            }
    tasks.append(new_task)
    print(f"{task_to_add} added successfully")
    return True

def delete_task(tasks):
    """This will delete a task."""

    if not tasks:
        print("There are no tasks to delete.")
        return False

    display_tasks(tasks)

    try:
        task_to_delete = int(input("Enter the task number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return False

    if 1 <= task_to_delete <= len(tasks):
        removed_task = tasks.pop(task_to_delete - 1)
        print(f"{removed_task['name']} deleted successfully")
        return True
    else:
        print("Invalid task number.")
        return False


def edit_task(tasks):
    """This will edit a task."""

    if not tasks:
        print("There are no tasks to edit.")
        return False

    display_tasks(tasks)

    try:
        task_to_edit = int(input("Enter the task number to edit: "))

    except ValueError:
        print("Please enter a valid number to edit.")
        return False

    if 1 <= task_to_edit <= len(tasks):

        new_task = input("Enter the new task: ").strip().lower()

        for task in tasks:
            if task["name"] == new_task:
                print("This task already exists.")
                return False

        old_task = tasks[task_to_edit - 1]["name"]

        tasks[task_to_edit - 1]["name"] = new_task

        print(f"{old_task} updated with {new_task}")

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
        completed_task = int(input("Enter the task number to mark: "))
    except ValueError:
        print("Please enter a valid task number to mark as completed.")
        return False

    if 1 <= completed_task <= len(tasks):

        if tasks[completed_task - 1]['completed']:
            print("Task is already completed.")
            return False
        else:
            tasks[completed_task - 1]['completed']= True 
             

            print(
                f"{tasks[completed_task - 1]['name']} marked as completed."
            )
            return True

    else:
        print("Invalid task number.")
        return False


def search_task(tasks):
    """Searches for a task."""

    if not tasks:
        print("There are no tasks to search.")
        return False

    find_task = input(
        "Enter the task name to search: "
    ).strip().lower()

    found = False

    for index, item in enumerate(tasks, start=1):

        if find_task in item['name'].lower():
            print(f"{index}. {item['name']}")
            found = True

    if not found:
        print("Task not found.")
        return False

    return True