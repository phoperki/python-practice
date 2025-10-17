def is_palindrome(text):
    # A palindrome reads the same forwards and backwards
    # Ignore spaces, punctuation, and capitalization
    # "A man a plan a canal Panama" = True
    # "racecar" = True
    # "hello" = False

    # Make lowercase
    tolower = text.casefold()
    # Remove spaces
    no_spaces = tolower.replace(" ", "")
    # Reverse
    reversed = no_spaces[::-1]
    
    return no_spaces == reversed
    

# Test cases
print(is_palindrome("racecar"))              # True
print(is_palindrome("hello"))                # False
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Was it a car or a cat I saw"))  # True
print(is_palindrome(""))                     # True (empty is palindrome)