from menu import show_menu
from task_manager import display_tasks,add_task,delete_task,edit_task,mark_task_completed,search_task
# from task_manager import *
from storage import load_tasks,save_tasks

tasks=load_tasks()

while True:
    show_menu()
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        display_tasks(tasks)
    elif choice =="2":
        add_task(tasks)
        save_tasks(tasks)
    elif choice =="3":
        delete_task(tasks)
        save_tasks(tasks)
    elif choice =="4":
        edit_task(tasks)
    elif choice == "5":
         mark_task_completed(tasks)
    elif choice == "6":
          search_task(tasks)
    elif choice =="7":
          print("Good Bye")
          break
