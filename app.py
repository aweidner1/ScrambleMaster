from random import shuffle
import random

words = []
stack = []

def getWords():
    with open('words.txt') as f:
        lines = f.readlines()
        for word in lines:
            words.append(word) 
    return words        

def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

def pushStack(words, shuffled_words):
    #add second parameter for scrambled word list?
    #in result, why does it also shuffle '\n' into the list too? Look into
    for i in range(4):
        stack.append(words[i]) #appends original word
        stack.append(shuffled_words[i]) #appends shuffled word
    print(stack)
    #stack.pop()
    #print(stack)

def main():
    getWords()
    shuffled_words = [shuffle_word(word) for word in words]
    #print(shuffled_words) #printing scrambled word list
    #print(words) #printing word list
    pushStack(words, shuffled_words)

if __name__ == '__main__':
    main()

#push array to stack non-scrambeled
#two arrays, parallel grab same index of both, then push to stack 
# (then we can pop after comparing to top value)
