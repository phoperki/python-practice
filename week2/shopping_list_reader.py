def read_shopping_list(filename):
    # Read the file and return a list of items
    # Remove any extra whitespace/newlines
    # Example return: ["apples", "bananas", "milk", ...]
    file = open(filename, 'r')
    lines = file.readlines()
    file.close
   
    clean_lines = []
    for line in lines:
        clean_lines.append(line.strip())
   
    return clean_lines
def count_items(filename):
    # Return how many items are in the shopping list
    return len(filename)
def search_item(filename, item):
    # Return True if item is in the list, False if not
    # Make it case-insensitive
    list = read_shopping_list(filename)
    if item.lower() in list:
        return True
    else:
        return False
   
def add_item_to_list(filename, new_item):
    # Add a new item to the end of the file
    # (We'll do this in Day 8, but try if you want!)
    pass
# Test cases
items = read_shopping_list("shopping_list.txt")
print(items)  # Should print list of items
print(count_items("shopping_list.txt"))  # Should print 7
print(search_item("shopping_list.txt", "milk"))   # True
print(search_item("shopping_list.txt", "pizza"))  # False
