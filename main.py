from menu import show_menu

from task_manager import (
    display_tasks,
    add_task,
    delete_task,
    edit_task,
    mark_task_completed,
    search_task,
)

from storage import load_tasks, save_tasks


def main():
    tasks = load_tasks()

    print(tasks)

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
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

        elif choice == "7":
            print("Good Bye")
            break


if __name__ == "__main__":
    main()