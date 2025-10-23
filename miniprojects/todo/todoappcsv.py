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


def remove_task(user_task):
    # User should provide task
    # remove_task will check list of dictionary to see if provided task inside
    # If yes then remove and use writerow(task)
    # If no then error
    try:
        tasks = read_tasks()
        new_lines=[]
        for task_dict in tasks:
            if user_task != task_dict['task']:
                new_lines.append(task_dict)
                
        with open("tasks.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, field_names)
            writer.writeheader()
            writer.writerows(new_lines)
        
        
        
    except TypeError:
        print(f"{user_task} is not in the task list.")
    
    except Exception as e:
        print(f"An error has occured: {e}")


def clear_tasks():
    try:
        answer = input("Are you sure you want to clear ALL tasks? Yes or No ")
        if answer == "Yes":
            with open("tasks.csv", "w") as f:
                clearwriter = csv.writer(f)
                clearwriter.writerow(['task', 'status'])
        elif answer == "No":
            pass

    except ValueError:
        print("Are you sure? Enter 'Yes' or 'No' ")


def complete_task(completed_task):
    # First read the tasks
    tasks = read_tasks()
    # Change tasks['status'] = complete
    for task_dict in tasks:
        if completed_task == task_dict['task']:
            task_dict['status'] = "complete"
    # Write tasks back to tasks.txt
    with open("tasks.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, field_names)
            writer.writeheader()
            writer.writerows(tasks)


def main():
    # Simple menu:
    # 1. Add task
    # 2. Show tasks
    # 3. Remove task
    # 4. Clear Tasks
    # 5. Complete Task
    # 6. Quit

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
        elif x == 3:
            user_task = input("What task do you want to remove: ")
            remove_task(user_task)
        elif x == 4:
            clear_tasks()
        elif x == 5:
            user_task = input("What task did you complete: ")
            complete_task(user_task)
        elif x == 6:
            break
        else:
            print("Make a valid selection. ")


# Run it
main()

