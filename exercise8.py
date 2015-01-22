from sys import argv
script, filepath = argv

def file_into_wordlist(path):
    """unpack text file, and place into list of words.  
    each word is a string.  List is ordered.  
    Return word_list"""
    file_obj = open(path)
    wordlist = []
    for line in file_obj:
        line = line.rstrip()
        wordlist.extend(line.split(" "))
    return wordlist

def create_dictionary(alist):
    """Create a dictionary, with a bigram as a key, 
    and the value is a list containing words that follow 
    each occurrence of the bigram in the word_list. 
    Returns dictionary."""
    bigram_dict= {}
    for index in range(len(alist)-2):
        key = (alist[index],alist[index+1])
        value = alist[index+2]
        if key not in bigram_dict:
            bigram_dict[key] = [value]
        else:
            bigram_dict[key].append(value)
    return bigram_dict 

def string_generator(adict, max_len):
    """Start with a bigram (one of the keys) from the
    dictionary, and add subsequent words to this string based 
    on random choice from the dictionary. returns a newly
    generated string."""
    # create random start which is constructed from one of the tuple keys
    import random
    list_of_keys = list(adict)
    start = random.choice(list_of_keys)
    output_string = start[0] + " " + start[1]
    while (start in adict) and (max_len > 0):
        # identify the next word using dictionary
        choices_list = adict[start]
        next_word = random.choice(choices_list)
        # string together tuple and next word
        output_string = output_string + " " + next_word
        start = (start[1],next_word)
        max_len -= 1
    return output_string


def main():
    markov_chains = create_dictionary(file_into_wordlist(filepath))
    print string_generator(markov_chains, 50)
   

main()
