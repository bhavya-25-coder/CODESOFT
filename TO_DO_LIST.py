import os
task_file = "tasks.txt"
def enter_tasks():
    if not os.path.exists(task_file):
        return []
    with open(task_file, "r") as file:
        return [line.strip() for line in file.readline()]
    
def save_task(tasks):
    with open(task_file,"w") as file:
        for task in tasks:
            file.write(task +"\n")

def show_task(tasks):
    if not tasks:
        print("No Task is found.")
    else:
        for i ,task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("New Task to go...: \nEnter your Task: ")
    tasks.append(task)
    save_task(tasks)
    print("Hurry! your task is added.")

def del_task(tasks):
    show_task(tasks)
    try:
        num=int(input("Enter task no to delete:"))
        if 0 < num <= len(tasks):
            removed = tasks.pop(num-1)
            save_task(tasks)
            print(f"Task'{removed}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please Enter a valid number.")

def main():
    tasks = enter_tasks()
    while True:
        print("\n----- TO-DO LIST -----")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Choose an Otion: ")

        if choice == "1":
            show_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            del_task(tasks)
        elif choice == "4":
            print(" Byeeeee!")
            break
        else:
            print("Invalid option. try again.")

if __name__ == "__main__" :
    main()       
