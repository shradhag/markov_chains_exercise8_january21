from sys import argv
script, filepath = argv
print filepath

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

def string_generator(adict,start):
    """Start with a bigram (one of the keys) from the
    dictionary, and add subsequent words to this string based 
    on random choice from the dictionary. returns a newly
    generated string."""
    import random
    list_of_next_words = adict.get(start)
    return list_of_next_words




def main():
    bigrams = create_dictionary(file_into_wordlist(filepath))
    start = ("could","you")
    print string_generator(bigrams, start)

main()
