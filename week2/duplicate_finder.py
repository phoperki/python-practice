def find_duplicates(x):
    dup_list=[]
    counted_list=[]
    for i in x:
        if i in counted_list:
            dup_list.append(i)

        counted_list.append(i)
    
    return list(set(dup_list))

# Test 1: Numbers
print(find_duplicates([1, 2, 3, 2, 4, 5, 3, 6]))  # Should show [2, 3]

# Test 2: Strings
print(find_duplicates(["dog", "cat", "dog", "bird"]))  # Should show ["dog"]

# Test 3: No duplicates
print(find_duplicates([1, 2, 3, 4, 5]))  # Should show []

# Test 4: All duplicates
print(find_duplicates([1, 1, 1, 1]))  # Should show [1]