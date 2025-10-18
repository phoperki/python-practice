def safe_read_list(filename):
    # Try to read the file
    # If file doesn't exist, return empty list and print friendly message
    # If any other error, print what went wrong

    lines = []
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"{filename} does not exist, returning empty list")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return [line.strip() for line in lines]

def safe_add_item(filename, item):
    # Try to add item
    # Handle: file not writable, disk full, permission denied
    # Return True if successful, False if failed

    try:
        with open(filename, "a") as f:
            f.write(f"{item}\n")
    except PermissionError:
        print("You do not have proper permissions to write to the file.")
    except OSError as e:
        print("General error: {e}")
    pass

def safe_remove_item(filename, item):
    # Try to remove item
    # Handle: file doesn't exist, item not in list
    # Print helpful messages for each error type
    try:
        with open(filename, "r") as file3:
            lines = file3.readlines()

        new_lines=[]
        for line in lines:
            if line.strip() != item:
                new_lines.append(line)
    
        with open(filename, "w") as file3:
            file3.writelines(new_lines)

        print(f"{item} has been removed.")
    except FileNotFoundError:
        print(f"{filename} not found.")
    except ValueError:
        print(f"{item} is not in the list.")

def get_number_from_user():
    # Ask user for a number
    # Keep asking until they enter a valid number
    # Handle: letters, symbols, empty input
    pass

# Test cases - these should NOT crash your program!
print(safe_read_list("file_that_doesnt_exist.txt"))
# Should print friendly message and return []

safe_add_item("read_only_file.txt", "test")
# Should handle permission error gracefully

safe_remove_item("missing.txt", "item")
# Should handle missing file

get_number_from_user()
# Try entering "abc", "", "12.5" - should handle all