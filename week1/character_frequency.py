def count_characters(text):
    # Count how many times each character appears
    # Ignore spaces and case (treat 'A' and 'a' as same)
    # Return a dictionary with character counts
    # Example: "hello" → {'h': 1, 'e': 1, 'l': 2, 'o': 1}

    # Make it lower case and remove spaces first
    # Make lowercase
    tolower = text.casefold()
    # Remove spaces
    no_spaces = tolower.replace(" ", "")
    # Create new dictionary 
    counts = {}
    
    # Create loop:
    for char in no_spaces:
        if char in counts:
            counts[char] = counts[char]+1
        else: 
            counts[char] = 1
    # Check if in dictionary 
    
    # Update the count if in dictionary

    # Create new dictionary entry if in dictionary
    return counts
    pass

# Test cases
print(count_characters("hello"))           
# Should be: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

print(count_characters("Mississippi"))     
# Should be: {'m': 1, 'i': 4, 's': 4, 'p': 2}

print(count_characters("The quick brown fox"))  
# Should ignore spaces and be case-insensitive