def add_task(tasks):
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        print(f'Task added: "{task}"')
    else:
        print("Task cannot be empty.")


def view_tasks(tasks):
    if not tasks:
        print("Your tasks list is empty.")
        return

    print("Your Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def delete_task(tasks):
    if not tasks:
        print("Your tasks list is empty.")
        return

    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to delete: "))
    except ValueError:
        print("Invalid task number.")
        return

    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f'Task "{removed_task}" has been removed.')
    else:
        print("Invalid task number.")


def main():
    tasks = []

    while True:
        print("============================")
        print("TO-DO LIST MENU")
        print("============================")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ").strip()

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
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

