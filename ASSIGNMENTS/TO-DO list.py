print("Welcome to your TO-DO-LIST manager!")
task_list = []
def view_tasks():
    if not task_list:
        print("Your To-Do List is empty.")
    else:
        print("\nYour To-Do List:")
        for i, (task, status) in enumerate(task_list, 1):
            print(f"{i}. {task} - {'Done' if status else 'Pending'}")

while True:
    print("\n---MENU---")
    print("1. Add New Task")
    print("2. Delete a Task")
    print("3. Update Task Status")
    print("4. Sort Tasks")
    print("5. View To-Do List")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    match choice:
        case 1:  
            task = str(input("Enter New Task: "))
            task_list.append((task, False))  
            print(f"Your task '{task}' has been added.")
        case 2: 
            view_tasks()
            if task_list:
                task_no = int(input("Enter the task number to remove: "))
                if 1 <= task_no <= len(task_list):
                    removed_task = task_list.pop(task_no - 1)
                    print(f"Task '{removed_task[0]}' removed successfully!")
                else:
                    print("Invalid task number!")
        case 3: 
            view_tasks()
            if task_list:
                task_no = int(input("Enter the task number to update status: "))
                if 1 <= task_no <= len(task_list):
                    task, _ = task_list[task_no - 1]
                    task_list[task_no - 1] = (task, True)  # Mark as done
                    print(f"Task '{task}' marked as done!")
                else:
                    print("Invalid task number!")
        case 4: 
            task_list.sort(key=lambda x: (x[1], x[0]))  
            print("Tasks sorted by status and name.")
        case 5:  
            view_tasks()
        case 6:  
            print("Exiting!")
            break
        case _:
            print("Oops! This is not a valid option.")
