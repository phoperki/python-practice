def get_even_numbers(numbers):
    # Take a list of numbers
    # Return a new list with only the even numbers
    # Keep them in the same order
    even_list = []

    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)

    return even_list

def get_odd_numbers(numbers):
    # Same thing, but return only odd numbers

    odd_list = []

    for number in numbers:
        if number % 2 != 0:
            odd_list.append(number)


    return odd_list

# Test cases

print("Even function")
print(get_even_numbers([1, 2, 3, 4, 5, 6]))        # [2, 4, 6]
print(get_even_numbers([10, 15, 20, 25]))          # [10, 20]
print(get_even_numbers([1, 3, 5]))                 # []
print(get_even_numbers([]))                        # []

print("Odd function")
print(get_odd_numbers([1, 2, 3, 4, 5, 6]))         # [1, 3, 5]
print(get_odd_numbers([10, 15, 20, 25]))           # [15, 25]

def split_even_odd(numbers):
    # Return TWO lists: (evens, odds)
    # Example: [1,2,3,4] → ([2,4], [1,3])


    evens=[]
    odds=[]
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
        elif number % 2 != 0:
            odds.append(number)

    return evens,odds

    
print("Split function:")

evens, odds = split_even_odd([1, 2, 3, 4, 5, 6])
print(evens)  # [2, 4, 6]
print(odds)   # [1, 3, 5]