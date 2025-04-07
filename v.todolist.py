print("welcome to your TO-DO-LIST manager!")
user_list=[]
n=str(input("Let's get started!What's your first task??\nENTER YOUR FIRST TASK:"))
user_list.append(n)
print(f'1.{n}')

while True:
    print("---MENU---")
    print("1.Add New Task")
    print("2.Delete a Task")
    print("3.View To-Do list")
    print("4.Exit")

    choice=int(input("Enter your choice: "))
    match choice:
            case 1:
                task=str(input("Enter New Task: "))
                user_list.append(task)
                print(f'your task {task} is added.')
            case 2:
                  if not user_list:
                    print("No tasks to remove.")
                  else:
                    print("\nYour To-Do List:")
                    for i, task in enumerate(user_list, 1):
                      print(f"{i}. {task}")

                    task_no = int(input("Enter the task number to remove: "))
                    if 1 <= task_no <= len(user_list):
                     removed_task = user_list.pop(task_no - 1)
                     print(f"Task '{removed_task}' removed successfully!")
                    else:
                      print("Invalid task number!")                  
                            
                 
            case 3:
                 for i, task in enumerate(user_list,1):
                     print(f'{i}.{task}')
                     
            case 4:
                 print("exiting!!")
                 break
            case _:
                print("oops!!This is not a valid option.")
