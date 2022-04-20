from itertools import count
from random import shuffle

import pygame
import random
import sys

pygame.init()

#set screen size
WIDTH = 500
HEIGHT = 600

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Scramble Master")

#set framerate
fps = 60
timer = pygame.time.Clock()

# FROM TXT FILE,
words = []
shuffled_words = []
wordStack = []

def getWords():
    with open('words.txt') as f:
        lines = f.readlines()
        for word in lines:
            words.append(word.rstrip('\n')) 
    return words        

def shuffle_word(word):
    word = list(word)
    shuffle(word)
    return ''.join(word)

TOTAL_WORDS = 4

def pushStack(words, shuffled_words):
    #suggestion: INSTEAD of adding words to stack after 30 seconds, decrease timer by an additional 15 seconds, probably easier than adding to stack
    for i in range(TOTAL_WORDS):
        wordStack.append(words[i]) #appends original word
        wordStack.append(shuffled_words[i]) #appends shuffled word
    #print(wordStack)
    #stack.pop()
    #print(stack)

#Made a peek function without linked list, could be helpful in event handlers
def peekStack(stack):
    if stack:
        return stack[-1]    # this will get the last element of stack
    else:
        return None

def main():
    getWords()
    shuffled_words = [shuffle_word(word) for word in words]
    pushStack(words , shuffled_words)
    print(peekStack(wordStack))
    draw_wordStack()
    user_input()
    #display_currentWord()
    #print(shuffled_words) #printing scrambled word list
    #print(words) #printing word list

#WORD FONT
word_font = pygame.font.Font('freesansbold.ttf', 24)#(font name, font size)

def draw_wordStack():
    global wordStack
    #print(shuffled_words) #printing scrambled word list
    #print(words) #printing word list
    #print(wordStack)
    
    for col in range (0,1):
        
        for row in range (0, TOTAL_WORDS):#####implement number of words in stack here
            pygame.draw.rect(screen, red, [125, 200, 250, 50], 0, 5)#PLAYER TEXT BOX
            pygame.draw.rect(screen, white, [col *100 + 125, row *60 + 300, 250, 50],0,5)#([x,y,width,height], fill, corners)
            
            currentWordInStack = wordStack.pop()#current scrambled word popped from the stack
           
            piece_text = word_font.render(currentWordInStack, True, black)
            
            screen.blit(piece_text, (col*100 + 150, row*60 + 300))

            wordStack.pop()#pop "correct" word spelling
    
#def display_currentWord():
   # currentWord = wordStack[1]
    #topword_text = word_font.render(currentWord, True, black) 
    #screen.blit(topword_text, (250, 300))
    #user_input()

def user_input():
    
    # basic font for user typed
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    
    # create rectangle
    input_rect = pygame.Rect(125, 200, 250, 50)
    
    active = False
    
    while True:
        for event in pygame.event.get():
    
        # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
            if event.type == pygame.KEYDOWN:
    
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
    
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
    
                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode
                    
        pygame.draw.rect(screen, red, input_rect)
    
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        
        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        
        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pygame.display.flip()

game_over = False#CHANGE LATER

currentWord = 0 #which word in the stack is the player

#running state
running = True
active_type = True

while running:
    #timer.tick(fps)
    screen.fill(black)
    main()
    pygame.display.flip()
pygame.quit()