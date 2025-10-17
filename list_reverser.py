# Method 1: Using .reverse()
def reverse_with_method(my_list):
    new_list=my_list.copy()
    new_list.reverse()
    return new_list

# Method 2: Using slicing (hint: [::-1])
def reverse_with_slice(my_list):    
    newlist2=my_list[::-1]
    return newlist2

# Method 3: Using a loop (manual way)
def reverse_with_loop(my_list):
    # Create reverse list
    reverse_list = []
    # Loop through my_list. Add end of my_list to beginning of reverse_list
    for x in my_list:
        reverse_list.insert(0,x)
    return reverse_list


# Tests
test_list = [1, 2, 3, 4, 5]
print("Original:", test_list)

result1 = reverse_with_method(test_list)
print("After method:", result1)  # Should still be [1, 2, 3, 4, 5]

result2 = reverse_with_slice(test_list)
print("After slice:", result2)  # Should still be [1, 2, 3, 4, 5]

result3 = reverse_with_loop(test_list)
print("After loop:", result3)  # Should still be [1, 2, 3, 4, 5]