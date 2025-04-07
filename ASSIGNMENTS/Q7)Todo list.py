'''Develop a Python program to manage a task list using lists and tuples,
including adding, removing, updating, and sorting tasks.'''

todo_list = []
task = input("Enter what you wanna get done today:")
task_list = list(map(str, task.split()))
print("All tasks:", task_list)
