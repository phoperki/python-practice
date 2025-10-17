def analyze_numbers(numbers):
    # Return a dictionary with these statistics:
    # {
    #   "count": how many numbers,
    #   "sum": total of all numbers,
    #   "average": mean value,
    #   "min": smallest number,
    #   "max": largest number,
    #   "range": difference between max and min,
    #   "even_count": how many even numbers,
    #   "odd_count": how many odd numbers
    # }


    stats={
       "count": "",
       "sum": "",
       "average": "",
       "min": "",
       "max": "",
       "range": "",
       "even_count": "",
       "odd_count": ""
    }
    
    even_list = []
    odd_list = []
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)


    stats['count']= len(numbers)
    stats['sum'] = sum(numbers)
    stats['average'] = stats['sum'] / stats['count'] 
    stats['min'] = min(numbers)
    stats['max'] = max(numbers)
    stats['range'] = stats["max"] - stats['min']
    stats['even_count'] = len(even_list)
    stats['odd_count'] = len(odd_list)

    return stats

# Test cases
print(analyze_numbers([1, 2, 3, 4, 5]))
# Should return: {
#   "count": 5,
#   "sum": 15,
#   "average": 3.0,
#   "min": 1,
#   "max": 5,
#   "range": 4,
#   "even_count": 2,
#   "odd_count": 3
# }

print(analyze_numbers([10, 20, 30]))
# Should return: {
#   "count": 3,
#   "sum": 60,
#   "average": 20.0,
#   "min": 10,
#   "max": 30,
#   "range": 20,
#   "even_count": 3,
#   "odd_count": 0
# }

print(analyze_numbers([-5, -2, 0, 3, 8]))
# Test with negatives and zero