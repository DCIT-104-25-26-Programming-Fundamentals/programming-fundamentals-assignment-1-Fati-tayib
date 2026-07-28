# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
# =============================================================================

def display_menu():
    """Prints the main menu."""
    print("============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def add_task(tasks):
    """Prompts for a task description and adds it to the list."""
    task = input("Enter task: ")
    tasks.append(task)
    print(f'Task added: "{task}"')


def view_tasks(tasks):
    """Displays all tasks, numbered from 1. Shows a message if empty."""
    if not tasks:
        print("Your to-do list is empty. Add a task to get started!")
        return

    print("Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def delete_task(tasks):
    """Shows the tasks, asks which one to delete, and removes it."""
    if not tasks:
        print("Your to-do list is empty. Nothing to delete.")
        return

    view_tasks(tasks)
    choice = input("Enter task number to delete: ")

    if not choice.isdigit():
        print("Error: Please enter a valid task number.")
        return

    index = int(choice)

    if index < 1 or index > len(tasks):
        print("Error: Invalid task number.")
        return

    removed = tasks.pop(index - 1)
    print(f'Task "{removed}" has been removed.')


def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 4.")

        print()  # blank line for readability between menu cycles


if __name__ == "__main__":
    main()
