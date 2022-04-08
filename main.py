from random import shuffle

words = []

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

def main():
    A = [shuffle_word(word) for word in L]
    getWords()
    print(A)


#push array to stack non-scrambeled
#two arrays, parallel grab same index of both, then push to stack 
# (then we can pop after comparing to top value)
