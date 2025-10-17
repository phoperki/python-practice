def longest_word(sentence):
    #Split sentence
    words = sentence.split()
    longest_word_length = 0
    longest_word = ""  
     
    for word in words:
        length_of_word = len(word)
        if length_of_word > longest_word_length:
            longest_word = word
            longest_word_length = length_of_word 
            
    return longest_word

        


print(longest_word("the quick brown fox"))
# Should return: "quick" (5 letters)

print(longest_word("I love programming"))
# Should return: "programming" (11 letters)