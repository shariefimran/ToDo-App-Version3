from menu import show_menu

from task_manager import (
    display_tasks,
    add_task,
    delete_task,
    edit_task,
    mark_task_completed,
    search_task,
    task_summary,
    filter_tasks,
    priority_options
)

from storage import load_tasks, save_tasks


def main():
    tasks = load_tasks()

    

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice not in ["1", "2", "3", "4", "5", "6", "7","8","9"]:
            print("Invalid choice")
            continue

        if choice == "1":
            display_tasks(tasks)

        elif choice == "2":
            result = add_task(tasks)

            if result:
                save_tasks(tasks)

        elif choice == "3":
            result = delete_task(tasks)

            if result:
                save_tasks(tasks)

        elif choice == "4":
            result = edit_task(tasks)

            if result:
                save_tasks(tasks)

        elif choice == "5":
            result = mark_task_completed(tasks)

            if result:
                save_tasks(tasks)

        elif choice == "6":
            search_task(tasks)
        elif choice =="7":
            task_summary(tasks)
        elif choice =="8":
            priority_choice = input("Enter priority choice: ").strip()
            if priority_choice in priority_options:
                priority= priority_options[priority_choice]
                filter_tasks(tasks,priority)
            else:
                print("please enter a valid priority choice")

            

        elif choice == "9":
            print("Good Bye")
            break


if __name__ == "__main__":
    main()