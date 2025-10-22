# A simple todo list app.
# Read from tasks.txt, add todos, set deadlines, set priority, and have a menu.
# This time reading and writing to csv file
import csv

field_names = ["task", "status"]

def read_tasks():
    try:
        with open("tasks.csv", "r", newline='') as f:
            tasks = csv.DictReader(f)
            
            return list(tasks)
    
    except FileNotFoundError:
        print("File not found. Creating now... ")
        
        with open("tasks.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writeheader()
            writer.writerow({"task": "Add Tasks", "status": "Incomplete"})
            writer.writerow({"task": "Get Groceries", "status": "Complete"})

        return []


def add_task(task):
    # Use writer.writerow?
    # Append to end of task list, then rewrite whole tasks.csv?
    # Append to the file
   tasks = read_tasks()
   with open("tasks.csv", "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writerow({"task": task, "status": "Incomplete"})
   pass
    
    
def show_tasks():
    # Read tasks.csv and print all tasks
    tasks = read_tasks()
    print(f"{field_names[0]} | {field_names[1]}")
    for row in tasks:
        print(f"{row['task']} | {row['status']}")


def remove_task(task):
    # User should provide number of task to remove
    try:
        with open('tasks.txt', 'r') as f:
            lines = f.readlines()
        
        new_lines=[]
        for line in lines:
            if line.strip() != task:
                new_lines.append(line)
    
        with open('tasks.txt', "w") as f:
            f.writelines(new_lines)
    except TypeError:
        print(f"{task} is not in the task list.")
    
    except Exception as e:
        print(f"An error has occured: {e}")


def clear_tasks():
    try:
        answer = input("Are you sure you want to clear ALL tasks? Yes or No ")
        if answer == "Yes":
            tasks = ""
            with open("tasks.txt", "w") as f:
                f.write(tasks)
        elif answer == "No":
            pass

    except ValueError:
        print("Are you sure? Enter 'Yes' or 'No' ")


def complete_task(completed_task):
    # First read the tasks
    tasks = read_tasks()
    # Append --[DONE] to end of task
    for i, task in enumerate(tasks):
        if completed_task == task:
            tasks[i] = f"{task} --[Done]"
    # Write tasks back to tasks.txt
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(f"{task}\n")


def main():
    # Simple menu:
    # 1. Add task
    # 2. Show tasks
    # 3. Remove task
    # 4. Clear Tasks
    # 5. Quit

    while True:
        print("\nTodo List: \n" \
        "1 -- Add Task\n" \
        "2 -- Show Tasks\n" \
        "3 -- Remove Task\n" \
        "4 -- Clear Tasks\n" \
        "5 -- Complete Task\n"
        "6 -- Quit")

        x = int(input("What is your selection: "))
        if x == 1:
            task = input("What is your task to add: ")
            add_task(task)
        elif x == 2:
            show_tasks()
        elif x == 6:
            break
        else:
            print("Make a valid selection. ")



# Run it
main()

