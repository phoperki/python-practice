def count_words(sentence):

    sentence_list = sentence.split()
    counts_dict = {}
    for word in sentence_list:
        if word in counts_dict:
            counts_dict[word] = counts_dict[word] +1
        else:
            counts_dict[word] = 1
    return counts_dict

    
sentence = "hello world hello"
print(count_words(sentence))


print(sentence.split())