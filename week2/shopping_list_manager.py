def read_shopping_list(shopping_list):
    # Use with to open shopping_list in readmode and assign to file1
    with open(shopping_list, "r") as file1:
        lines = file1.readlines() # readlines() reads all the lines in the file

    # Need to remove \n from all the lines.
    clean_lines=[]
    for line in lines:
        clean_lines.append(line.strip()) # Strip removes the \n
    
    return clean_lines

def add_item(filename, item):
    # Add ONE item to the end of the file
    # Each item should be on a new line

    with open(filename, "a") as file2:
        file2.write(f"\n{item}")
    

def remove_item(filename, item):
    # Remove an item from the list
    # Read the file, remove the item, write back
    with open(filename, "r") as file3:
        lines = file3.readlines()

    new_lines=[]
    for line in lines:
        if line.strip() != item:
            new_lines.append(line)
    
    with open(filename, "w") as file3:
        file3.writelines(new_lines)

    print(f"{item} has been removed.")

def create_new_list(filename, items):
    # Create a brand new file with a list of items
    # items is a list like: ["apples", "bananas", "milk"]
    # WARNING: This will overwrite the file if it exists!

    with open(filename, 'w') as file4:
        for item in items:
            file4.write(f"{item}\n")
    
    print(f"{items} has been added to the file {filename}")

def clear_list(filename):
    # Delete all items from the file (make it empty)
    with open(filename, "w") as file5:
        file5.write("")


print(read_shopping_list("shopping_list.txt"))
# Test cases
add_item("shopping_list.txt", "pizza")
# Check the file - pizza should be at the end

remove_item("shopping_list.txt", "bread")
# Check the file - bread should be gone

create_new_list("new_list.txt", ["coffee", "tea", "sugar"])
# Should create a new file with these 3 items

clear_list("new_list.txt")
# File should now be empty