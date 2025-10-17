def find_max(numbers):
    # Find and return the largest number in the list
    # Don't use the built-in max() function - do it manually

    largest_number = numbers[0] 
    
    #Loop through numbers
    for number in numbers:
        if number>largest_number:
            largest_number=number
    return largest_number

def find_min(numbers):
    # Find and return the smallest number
    # Don't use the built-in min() function

    smallest_number = numbers[0]
    for number in numbers:
        if number<smallest_number:
            smallest_number=number
    return smallest_number

def find_range(numbers):
    # Return the difference between max and min
    # You can use your functions above!

    maximum=find_max(numbers)
    minimum=find_min(numbers)

    range=maximum-minimum

    return range



# Test cases
print("Max")
print(find_max([3, 7, 2, 9, 1]))          # 9
print(find_max([100]))                    # 100
print(find_max([-5, -2, -10, -1]))        # -1

print("Min")
print(find_min([3, 7, 2, 9, 1]))          # 1
print(find_min([100]))                    # 100
print(find_min([-5, -2, -10, -1]))        # -10

print("Range")
print(find_range([3, 7, 2, 9, 1]))        # 8 (9-1)
print(find_range([100]))                  # 0 (100-100)