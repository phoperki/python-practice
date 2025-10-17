def count_word_frequency(text):
    # Take a string of text
    # Return a dictionary with each word and how many times it appears
    # Make it case-insensitive and ignore punctuation
    # Example: "Hello world! Hello." → {"hello": 2, "world": 1}
    text = text.lower()
    text = text.replace(".", "").replace("!","")
    words= text.split()
    frequency_dict={}
    
    for word in words:
        if word not in frequency_dict:
            frequency_dict[word]=words.count(word)
    return frequency_dict

def get_top_words(word_freq, n):
    # Take a word frequency dictionary
    # Return the top N most common words as a list of tuples
    # Example: ({"hello": 5, "world": 2, "test": 3}, 2) → [("hello", 5), ("test", 3)]
    # Hint: You'll need to sort somehow...
    
    # Convert list to list of tuples
    word_list = []
    for word, count in word_freq.items():
        # Appends word_list with (word,count) as one value.
        word_list.append((word,count))
    
    # Sorted function(data, key parameter tells python to use this to compare items., reverse=True because default is smallest to largest.)
    sorted_list = sorted(word_list, key=lambda x: x[1], reverse=True)
    
    return sorted_list[:n]
    

def get_unique_words(text):
    # Return a list of words that appear exactly once
    freq_dict=count_word_frequency(text)
    unique=[]
    for word, count in freq_dict.items():
        if count==1:
            unique.append(word)

    return unique

def word_length_stats(text):
    # Return a dictionary with:
    #   - "shortest": the shortest word
    #   - "longest": the longest word
    #   - "average_length": average word length (as float)

    text = text.lower()
    text = text.replace(".", "").replace("!","")
    words = text.split()
    stats={"shortest": "", "longest": "", "average_length": ""}
    

    shortest=words[0]
    longest=words[0]
    
    shortest_length=len(words[1])
    longest_length=len(words[1])
    sum=0

    for word in words:
        sum=sum+len(word)
        if len(word)<shortest_length:
            shortest=word
        if len(word)>longest_length:
            longest=word

    stats["average_length"] = sum / len(words)
    stats["shortest"]=shortest
    stats["longest"]=longest
    return stats

# Test cases
sample_text = "Hello world! Hello Python. Python is great. Python Python Python."

print(count_word_frequency(sample_text))
# Should be: {"hello": 2, "world": 1, "python": 5, "is": 1, "great": 1}

freq = count_word_frequency(sample_text)
print(get_top_words(freq, 3))
# Should be: [("python", 5), ("hello", 2), ("world", 1)] or similar

print(get_unique_words(sample_text))
# Should be: ["world", "is", "great"] (words appearing once)

print(word_length_stats(sample_text))
# Should be something like: {"shortest": "is", "longest": "python", "average_length": 5.something}