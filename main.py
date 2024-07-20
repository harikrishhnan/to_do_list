print("""
         _____  _____         ______  _____          _      _____  _____  _____
        |_   _||  _  |        |  _  \|  _  |        | |    |_   _|/  ___||_   _|
          | |  | | | |        | | | || | | |        | |      | |  \ `--.   | |
          | |  | | | |        | | | || | | |        | |      | |   `--. \  | |
          | |  \ \_/ /        | |/ / \ \_/ /        | |____ _| |_ /\__/ /  | |
          \_/   \___/         |___/   \___/         \_____/ \___/ \____/   \_/
 ______                ______                ______
|______|              |______|              |______|
""")

# Initial stage
n = int(input("Enter the number of tasks: "))
tasks = []

for i in range(1, n + 1):
    t = input(f"Enter the task for Task {i}: ")
    tasks.append({"task": t, "done": False})

print(f"Your tasks are \n{[task['task'] for task in tasks]}")

def display_help():
    print("\nChoose an action:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Exit")

def add_task():
    t = input("Enter the new task: ")
    tasks.append({"task": t, "done": False})
    print(f"Task '{t}' added.")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty!")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not done"
            print(f"{idx}. {task['task']} [{status}]")

def mark_task_as_done():
    view_tasks()
    task_num = int(input("Enter the task number to mark as done: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]["done"] = True
        print(f"Task {task_num} marked as done.")
    else:
        print("Invalid task number.")

while True:
    print("For more info, type -h or --help ")
    in_put = input(">").strip().lower()
    while True:
        if in_put == "-h" or in_put == "--help":
            display_help()
            break
        else:
            print("Invalid Variable")
            break
    try:
        ch = int(input("Enter your choice: "))
        if ch == 1:
            add_task()
        elif ch == 2:
            view_tasks()
        elif ch == 3:
            mark_task_as_done()
        elif ch == 4:
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")
    except ValueError:
        print("Invalid input, please enter a number.")
