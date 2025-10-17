def find_longest_word(sentence):
    words=sentence.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
            
    return longest_word

print(find_longest_word("The brown fox jumps over the lazy dog"))

