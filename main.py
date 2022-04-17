from itertools import count

import pygame
import random

pygame.init()

#set screen size
WIDTH = 500
HEIGHT = 600

white = (255,255,255)
black = (0,0,0)

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Scramble Master")

#set framerate
fps = 60
timer = pygame.time.Clock()


#Word stack
wordStack = []


#WORD FONT
word_font = pygame.font.Font('freesansbold.ttf', 24)#(font name, font size)

#GET RANDOM WORD FROM TXT FILE
def get_RandomWord():
    newRandomWord = random.choice(open("words.txt","r").readline().split())
    return newRandomWord

#print Stack

def draw_wordStack():
    global wordStack
    wordStack.append('test')
    wordStack.append('test1')
    wordStack.append('test2')
    wordStack.append('test3')
    wordStack.append('test4')
    
    for col in range (0,1):
        
        for row in range (0,5):#####implement number of words in stack here
            pygame.draw.rect(screen, white, [col *100 + 125, row *60 + 300, 250, 50],0,5)#([x,y,width,height], fill, corners)
             
            currentWordInStack = wordStack.pop()#current scrambled word popped from the stack
            piece_text = word_font.render(currentWordInStack, True, black)
            screen.blit(piece_text, (col*100 + 150, row*60 + 300))


game_over = False#CHANGE LATER

currentWord = 0 #which word in the stack is the player

#running state
running = True
turn_active = True

while running:
    timer.tick(fps)
    screen.fill(black)
    draw_wordStack()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                turn_active = False
        
        if event.type == pygame.TEXTINPUT and turn_active and not game_over:
            entry = event.__getattribute__('text')
            wordStack[currentWord]
        

    pygame.display.flip()
pygame.quit()