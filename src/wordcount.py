#!/usr/bin/python -tt

'''
now under Git 
'''

import sys

def count_all_words(filename):
    #create an empty dictionary
    word_count = {}
  
    infile = open(filename, 'r')
    for line in infile:
        words = line.split()
        for word in words:
            word = word.lower()
            # word not in dictionary yet, set it's value to 1
            if not word in word_count:
                word_count[word] = 1
            else:
            #word is already in, add 1 to existing value
                word_count[word] = word_count[word] + 1 
    infile.close()
    return word_count
  
def print_words(filename):
    word_count = count_all_words(filename) 
    # insert the words as keys
    words = sorted(word_count.keys())
    for word in words:
        #extract the keys (the words), then the values (the word count)
        print word, word_count[word]
  
def get_count(word_count_tuple):
    return word_count_tuple[1]
  
def print_top(filename):
    word_count = count_all_words(filename)
    items = sorted(word_count.items(), key=get_count, reverse=True)
    # insert the words as keys
    for item in items[:20]:
        print item[0], item[1]

  
def main():
    if len(sys.argv) != 3:
        print 'usage: ./wordcount.py {--count | --topcount} file'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
  
    if option == '--count':
        print_words(filename)
   
    
    elif option == '--topcount':
        print_top(filename)
    
    else:
        print 'unknown option: ' + option
        sys.exit(1)

  
if __name__ == '__main__':
    main()
