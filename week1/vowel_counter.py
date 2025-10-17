def count_vowels(text):
    # Count how many vowels (a, e, i, o, u) are in the text
    # Case-insensitive
    # Return the count as an integer

    # Count "a,e,i,o,u" string method .count() did not work
    count=0
    vowel = ["a","e","i","o","u"]
    to_lower = text.lower()
    for letter in to_lower:
        if letter in vowel:
            count=count+1
    return count

print(count_vowels("hello"))              # 2 (e, o)
print(count_vowels("programming"))        # 3 (o, a, i)
print(count_vowels("AEIOU"))              # 5
print(count_vowels("sky"))                # 0 
print(count_vowels("rhythm"))             # 0 (no vowels!)
print(count_vowels("The quick brown fox"))  # 5 (e, u, i, o, o)