def get_word_lengths(sentence):
    # Take a sentence (string)
    # Return a list of the length of each word
    # Example: "hello world" → [5, 5]

    # Split sentence by space
    sent_list=sentence.split(" ")
    count_list=[] 
    # Loop through sentence list
    # For each word in sentence list count the number of letters
    # Assign count to list in order 
    for word in sent_list:
        count=0 
        for letter in word:
            count=count+1

        count_list.append(count)
    
    return count_list

def get_long_words(sentence, min_length):
    # Return only words that are at least min_length characters
    # Example: ("hello world test", 5) → ["hello", "world"]
    # Split sentence by space
    sent_list=sentence.split(" ")
    word_list=[] 
    # Assign count to list in order 
    for word in sent_list:
        count=0 
        for letter in word:
            count=count+1

        if count>=min_length:
            word_list.append(word)
    
    return word_list

def get_short_words(sentence, max_length):
    # Return only words that are at most max_length characters
    # Example: ("hello world test", 4) → ["test"]
    # Use get_word_length function 
    words=sentence.split()
    word_lengths=get_word_lengths(sentence)
    short_words=[]
    for i in range(len(words)):
        if word_lengths[i] <= max_length:
            short_words.append(words[i])

    return short_words

def get_shortest_word(sentence):
    # Return the shortest word in the sentence
    # If there's a tie, return the first one
    #print(min_word) 
    sent_list=sentence.split(" ")
    #print(sent_list)
    min_word=sent_list[0]
    min_word_length=len(min_word)
    #print(min_word_length)

    # Assign count to list in order 
    for word in sent_list:
        word_length=len(word)  

        if word_length<min_word_length:
            min_word=word
            min_word_length=word_length
    
    return min_word
    

# Test cases
print(get_word_lengths("hello world"))                    # [5, 5]
print(get_word_lengths("the quick brown fox"))            # [3, 5, 5, 3]
print(get_word_lengths("Python"))                         # [6]

print(get_long_words("hello world test", 5))              # ['hello', 'world']
print(get_long_words("the quick brown fox jumps", 4))     # ['quick', 'brown', 'jumps']
print(get_long_words("I am ok", 3))                       # []

print(get_short_words("hello world test", 4))              # ['hello', 'world']
print(get_short_words("the quick brown fox jumps", 3))     # ['quick', 'brown', 'jumps']
print(get_short_words("I am ok", 2))         

print(get_shortest_word("the quick brown fox"))           # "the"
print(get_shortest_word("hello world"))                   # "hello" (tie, return first)
print(get_shortest_word("supercalifragilistic"))          # "supercalifragilistic" 



def create_word_length_dict(sentence):
    # Return a dictionary mapping each word to its length
    # Example: "hello world" → {"hello": 5, "world": 5}
    word_length_dict={}
    words=sentence.split()
    
    for i in range(len(words)):
        key=words[i]
        value=len(key)
        word_length_dict[key]=value
    return word_length_dict

print(create_word_length_dict("hello world")) # {"hello": 5, "world": 5}
print(create_word_length_dict("bunch of words and their lengths")) # {'bunch': 5, 'of': 2, 'words': 5, 'and': 3, 'their': 5, 'lengths': 7}