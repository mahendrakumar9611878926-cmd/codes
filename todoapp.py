tasks=[]

while True:
    print("1) add a task")
    print("2) remove a task")
    print("3) view tasks")
    print("4) exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added.")
    elif choice == "2":
        task = input("Enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed.")
        else:
            print("Task not found.")
    elif choice == "3":
        print("Tasks:")
        for task in tasks:
            print(f"- {task}")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")