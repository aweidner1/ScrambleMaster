from itertools import count
from random import shuffle
from tkinter import font

import pygame
import random
import sys

pygame.init()

#set screen size
WIDTH = 500
HEIGHT = 600

#COLORS
white = (255,255,255)
black = (0,0,0)
red = (255,77,77)
green = (128,255,128)
gray = (217,217,217)
lightblue = (102,204,255)
paleyellow = (255,255,153) 

penalty = 5
tries = 0

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Scramble Master")

clock = pygame.time.Clock()
counter = 120
text = '120'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT +1 , 1000)
timer_rect = pygame.Rect(32, 48, 200, 50)

#FROM TXT FILE,
words = []
shuffled_words = []
wordStack = []

#reading from txt file, returns list of words
def getWords():
    with open('words.txt') as f:
        lines = f.readlines()
        for word in lines:
            if(not words.__contains__(word)):
                words.append(word.rstrip('\n')) 
    return words  

#maybe call above main, looks messy calling function randomly here?
#getWords()

#utilizes recursive and stack to ensure word is shuffled
def shuffle_word(word):
    word = list(word)
    shuffle(word)
    if(wordStack.__contains__(word)):#ensure shuffled word isn't shuffled correctly
        shuffle_word(word)#recursively shuffle the word again
    return ''.join(word)

TOTAL_WORDS = 4

#Push stack function
def pushStack(words, shuffled_words):
    for _ in range(TOTAL_WORDS):
        randomNum = random.randint(0,len(words))
        wordStack.append(words[randomNum]) #appends original word
        wordStack.append(shuffled_words[randomNum]) #appends shuffled word

#Peek stack function
def peekStack(stack):
    if stack:
        return stack[-1]    # this will get the last element of stack
    else:
        return None

#Peek correct word from stack
def peekStackCorrect(stack):
    if stack:
        return stack[-2]    # this will get the second last element of stack
    else:
        return None

#Calling getWords() here, a bit more clean than calling between functions above
getWords()
def main():
    shuffled_words = [shuffle_word(word) for word in words]
    pushStack(words , shuffled_words)
    draw_wordStack()
    user_input()

#WORD FONT
word_font = pygame.font.Font('freesansbold.ttf', 24)#(font name, font size)
font = pygame.font.Font('freesansbold.ttf', 24)#(font name, font size)

#Drawing wordStack boxes, stack, etc.
def draw_wordStack():
    currentWord = 1
    
    for col in range (0,1):
        
        for row in range (0, (len(wordStack)//2)):#####implement number of words in stack here

            if(len(wordStack)>=2):
                pygame.draw.rect(screen, paleyellow, [col *100 + 125, row *60 + 300, 250, 50],0,5)#([x,y,width,height], fill, corners)
                
                currentWordInStack = wordStack[-currentWord]#current scrambled word peeked from the stack
           
                piece_text = word_font.render(currentWordInStack, True, black)
            
                screen.blit(piece_text, (col*100 + 150, row*60 + 300))
            
                currentWord = currentWord + 2

#Retrieves user input, events, states, etc. Used for most functionality
def user_input():
    
    # basic font for user typed
    base_font = pygame.font.Font(None, 32)
    user_text = ''
    
    # create rectangle
    input_rect = pygame.Rect(125, 200, 250, 50)
    
    active = False
    
    while True:   
       
        for event in pygame.event.get():
            clock.tick(60) 
            global text
            global counter
            font = pygame.font.SysFont('Consolas', 30)
            pygame.draw.rect(screen, gray, input_rect)
    
            if event.type == pygame.USEREVENT+1:
                if counter > 0:
                    counter -= 1
                    text = str(counter).rjust(3)
                else:
                     clearScreen() 
                     endGame()
           
            pygame.draw.rect(screen, lightblue, timer_rect)
            
            screen.blit(font.render(text, True, black), (32, 48))
            pygame.display.flip()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
            if event.type == pygame.KEYDOWN:
    
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
    
                elif event.key == pygame.K_RETURN:
                    if checkCorrect(user_text):
                        pygame.draw.rect(screen, green, input_rect)
                        pygame.display.flip()
                        pygame.time.delay(200)
                        user_text = ''
                        wordStack.pop()
                        wordStack.pop()
                        clearScreen()
                        draw_wordStack()
                        #IF statement checking if game is over (every loop)
                        if (len(wordStack) == 0):
                            clearScreen()
                            winGame()

                    else:
                        global penalty
                        penaltyStr = str(penalty).rjust(3)
                        penalty += 5
                        pygame.draw.rect(screen, lightblue, (400,48,100,100))
                        screen.blit(word_font.render(penaltyStr, True, red), (400, 48))

                        global tries
                        tries += 1
                        tryStr = str(tries).rjust(3)
                        pygame.draw.rect(screen, lightblue, (300,48,100,100))
                        screen.blit(word_font.render(tryStr, True, red), (300, 48))

                        pygame.display.flip()
                        pygame.draw.rect(screen, red, input_rect)
                        pygame.display.flip()
                        pygame.time.delay(200)
                        counter = counter - 5
                        user_text = ''
   
                # Unicode standard is used for string
                # formation
                else:
                    user_text += event.unicode
    
        text_surface = base_font.render(user_text, True, black)
        
        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        
        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pygame.display.flip()

#checkCorrect function used in userInput fuction
def checkCorrect(userInput):
    print(userInput)
    if userInput == peekStackCorrect(wordStack):
        return True
    else:
        return False

game_over = False #CHANGE LATER

currentWord = 0 #which word in the stack is the player

#running state
running = True
startState = True
endState = True
#STATES 
running = True
startState = True

start_rect= pygame.Rect(75, 287, 350, 26)
def clearScreen():
    screen.fill(lightblue)

#Menu function when beginning the prog
def displayMenu():
    global startState
    startState = True
    while(startState):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            pygame.draw.rect(screen, paleyellow, start_rect)
            startText = "CLICK ANYWHERE TO START"
            screen.blit(font.render(startText, True, black), start_rect)
            pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                startState = False
#End game function, called in userInput to check state of game
def endGame():
     global endState
     endState = True
     while(endState):
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()
             pygame.draw.rect(screen, paleyellow, start_rect)
             endText = "GAMEOVER, click to exit."
             screen.blit(font.render(endText, True, black), start_rect)
             pygame.display.flip()
             if event.type == pygame.MOUSEBUTTONDOWN:
                 pygame.quit()
                 sys.exit()

#Win game function, called in userInput to check state of game
def winGame():
    global endState
    endState = True
    while(endState):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.draw.rect(screen, paleyellow, start_rect)
            endText = "Congrats, click to exit game."
            screen.blit(font.render(endText, True, black), start_rect)
            pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
            
while running:
    if(startState):
        clearScreen()
        displayMenu()
    else: 
        clearScreen()
        main()
    pygame.display.flip()
pygame.quit()