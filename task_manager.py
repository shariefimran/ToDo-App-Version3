def display_tasks(tasks):
    """This Function will be used to view the menu"""
    if not tasks:
        print("There are no tasks to display")
    else:
        for index, item in enumerate(tasks,start=1):
            print(f"{index}.{item}")


def add_task(tasks):
    """This will Add task"""
    task_to_add=input("enter the task name to add").strip().lower()
    if task_to_add not in tasks:
        tasks.append(task_to_add)
        print(f"{task_to_add} added successfully")
    else:
        print("entered task already present in the list ")

def delete_task(tasks):
    """This will delete task"""
    # for index,item in enumerate(tasks,start=1):
    #     print(f"{index}.{item}")
    if not tasks:    
        return
    display_tasks(tasks)
    task_to_delete=int(input("Enter the task number to delete"))
    if 1 <= task_to_delete <= len(tasks):
        removed_task= tasks.pop(task_to_delete-1)
        print(f"{removed_task} deleted  successfully")
    else:
        print("Invalid task number ")


def edit_task(tasks):
    """this will edit task"""
    if not tasks:
        print("there are no tasks to edit")
        return
    display_tasks(tasks)
    task_to_edit=int(input("enter the task number to edit "))
    if 1 <= task_to_edit <= len(tasks):
        new_task=input("enetr the new task").strip().lower()
        if new_task not in tasks:
            old_task=tasks[task_to_edit-1]
            tasks[task_to_edit-1]=new_task
            print(f"{old_task}updated with {new_task}")
        else:
            print("This task already exists.") 
    else:
        print("invalid task ")

def mark_task_completed(tasks):
    """Mark task completed """
    if not tasks:
                
                print("There are no tasks to mark.")
                return
    display_tasks(tasks)
    completed_task = int(input("Enter the task number to mark: "))
    
    if 1 <= completed_task <= len(tasks):
                    
                    if tasks[completed_task - 1].startswith("✔️"):
                        print("Task is already completed.")
                    else:
                        tasks[completed_task - 1] = "✔️ " + tasks[completed_task - 1]
                        print(f'{tasks[completed_task - 1]} marked as completed.')
    
    else:
                    
                    print("Invalid task number.")



def search_task(tasks):
    """Searches for a task."""

    if not tasks:
        print("There are no tasks to search.")
        return

    find_task = input("Enter the task name to search: ").strip().lower()

    found = False

    for index, item in enumerate(tasks, start=1):

        if find_task in item.lower():
            print(f"{index}. {item}")
            found = True

    if not found:
        print("Task not found.")
