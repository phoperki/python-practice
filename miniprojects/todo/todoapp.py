# A simple todo list app.
# Read from tasks.txt, add todos, set deadlines, set priority, and have a menu.

def add_task(task):
    # Add task to tasks.txt
    # Append to the file

    
    try:
        with open('tasks.txt', 'a') as f:
            f.write(f"{task}\n")
            print(f"{task} has been added.")
    except FileNotFoundError:
        print("tasks.txt not found. Creating now")
        with open('tasks.txt', 'w') as f:
            f.write(task)
    except PermissionError:
        print("You don't have permissions to write to this directory.")
    
    

def show_tasks():
    # Read tasks.txt and print all tasks

    try:
        with open('tasks.txt', 'r') as f:
            tasks = f.readlines()

        count = 0
        for task in tasks:
            count = count+1
            task =task.strip()
            print(f"{count}. {task}")
        
    except:
        print("Error has occured.")
    

def remove_task(task):
    try:
        with open('tasks.txt', 'r') as f:
            lines = f.readlines()
        
        new_lines=[]
        for line in lines:
            if line.strip() != task:
                new_lines.append(line)
    
        with open('tasks.txt', "w") as f:
            f.writelines(new_lines)
    except Exception as e:
        print(f"An error has occured: {e}")
        


    pass

def main():
    # Simple menu:
    # 1. Add task
    # 2. Show tasks
    # 3. Remove task
    # 4. Quit

    while True:
        print("\nTodo List: \n" \
        "1 -- Add Task\n" \
        "2 -- Show Tasks\n" \
        "3 -- Remove Task\n" \
        "4 -- Quit")
        try:
            select = int(input("What is your selection: "))
            if select == 1:
                task = input("What is your task: ")
                add_task(task)
            elif select == 2:
                print("Here is the current todo list: ")
                show_tasks()
            elif select == 3:
                task = input("What task do you want to remove: ")
                remove_task(task)
            elif select == 4:
                print("Thank you for reading the task list.")
                break

        except ValueError:
            print("Enter a valid number.")

        except Exception as e:
            print(f"An error has occured: {e}")    

# Run it
main()
