def print_header(title):
    print("="* 30)
    print(title.center(30))
    print("="* 30)


menu_items=[
        "View Task",
        "Add Task",
        "Delete Task",
        "Edit Task",
        "Mark Task as Completed",
        "Search Task",
        "Task Summary",
        "Filter Tasks",
        "Filter Category",
        "Due Date",
        "Sort Tasks",
        "Export Tasks",
        "Import Task",
        "Exit"
    ]
def show_menu():

    """This function will show the menu"""
    # print("\n======== TO DO APP=====")
    print_header("TODO MANAGER")
   

    for index,menu in enumerate (menu_items, start=1):
        print(f"{index}. {menu}")


    # print("1. View Task")
    # print("2. Add Task")
    # print("3. Delete Task")
    # print("4. Edit Task")
    # print("5. Mark Task as Completed")
    # print("6. Search Task")
    # print("7. Task Summary")
    # print("8. Filter Tasks")
    # print("9. Filter Category")
    # print("10. Due Date")
    # print("11. Sort Tasks")
    # print("12. Exit")



