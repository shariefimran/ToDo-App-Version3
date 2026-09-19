from menu import show_menu, menu_items

from task_manager import (
    display_tasks,
    add_task,
    delete_task,
    edit_task,
    mark_task_completed,
    search_task,
    task_summary,
    filter_tasks,
    priority_options,
    category_options,
    filter_task_by_category,
    show_overdue_tasks,
    show_due_tasks,
    show_upcoming_due_tasks,
    sort_tasks_by_priority,
    sort_tasks_by_due_date,
    sort_task_alphabetically,
    display_tasks_paginated,
    bulk_delete_tasks
)

from storage import (
    load_tasks,
    save_tasks,
    export_tasks,
    import_tasks
)


def main():
    tasks = load_tasks()

    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice: ").strip())

            if not 1 <= choice <= len(menu_items):
                print("Invalid Choice")
                continue

        except ValueError:
            print("Please enter a valid choice")
            continue

        if choice == 1:
            display_tasks_paginated(tasks)

        elif choice == 2:
            result = add_task(tasks)

            if result:
                save_tasks(tasks)

        elif choice == 3:
            result = delete_task(tasks)

            if result:
                save_tasks(tasks)

        elif choice == 4:
            result = edit_task(tasks)

            if result:
                save_tasks(tasks)

        elif choice == 5:
            result = mark_task_completed(tasks)

            if result:
                save_tasks(tasks)

        elif choice == 6:
            search_task(tasks)

        elif choice == 7:
            task_summary(tasks)

        elif choice == 8:
            priority_choice = input(
                "Enter priority choice: "
            ).strip()

            if priority_choice in priority_options:
                priority = priority_options[priority_choice]
                filter_tasks(tasks, priority)

            else:
                print("Please enter a valid priority choice")

        elif choice == 9:
            category_choice = input(
                "Enter category choice: "
            ).strip()

            if category_choice in category_options:
                category = category_options[category_choice]
                filter_task_by_category(tasks, category)

            else:
                print("Please enter a valid category choice")

        elif choice == 10:
            while True:
                print("\n====== Due Date ======")
                print("1. Overdue Tasks")
                print("2. Due Today")
                print("3. Upcoming Tasks")
                print("4. Back to Main Menu")

                due_choice = input(
                    "Enter your choice: "
                ).strip()

                if due_choice == "1":
                    show_overdue_tasks(tasks)

                elif due_choice == "2":
                    show_due_tasks(tasks)

                elif due_choice == "3":
                    show_upcoming_due_tasks(tasks)

                elif due_choice == "4":
                    break

                else:
                    print("Invalid choice")

        elif choice == 11:
            while True:
                print("\n===== Sort Tasks =====")
                print("1. Sort by Priority")
                print("2. Sort by Due Date")
                print("3. Sort by Alphabetical Order")
                print("4. Back to Main Menu")

                sort_choice = input(
                    "Enter your choice: "
                ).strip()

                if sort_choice == "1":
                    sort_tasks_by_priority(tasks)

                elif sort_choice == "2":
                    sort_tasks_by_due_date(tasks)

                elif sort_choice == "3":
                    sort_task_alphabetically(tasks)

                elif sort_choice == "4":
                    break

                else:
                    print("Invalid choice")

        elif choice == 12:
            export_tasks(tasks)

        elif choice == 13:
            imported_tasks = import_tasks()

            if imported_tasks:
                tasks = imported_tasks
                save_tasks(tasks)
        elif choice == 14:
            if bulk_delete_tasks(tasks):
                save_tasks(tasks)

        elif choice == 15:
            print("Good Bye")
            break


if __name__ == "__main__":
    main()

    