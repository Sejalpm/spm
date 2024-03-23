def main():
    todo= []

    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice=='1':
            task = input("Enter the task: ")
            todo.append({"task": task, "completed": False})
            print("Task added")

        elif choice=='2':
            if not todo:
                print("No tasks in list.")
            else:
                print("Tasks:")
                for index, item in enumerate(todo,start=1):
                    status = "Completed" if item["completed"] else"Pending"
                    print(f"{index}. {item['task']} - {status}")

        elif choice=='3':
            if not todo:
                print("No tasks")
            else:
                task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
                if 0 <= task_index < len(todo):
                    todo[task_index]["completed"] = True
                    print("Task marked as completed")
                else:
                    print("Invalid task index")

        elif choice == '4':
            print("Exiting")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()





