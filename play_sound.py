import pygame
import os
import random

random.seed
prouds = ['nothing in here']

while True:
    input("waiting for input")

    # if list of sounds is empty, make list with all sounds
    if len(prouds) == 1:
        print('is empty; make new one')
        #os.chdir('sounds')
        prouds = os.listdir('sounds')
    else:
        print('not empty yet')

        
    # randomly select one sound and delete from list
    howmany = len(prouds)
    print(howmany)
    mynum = random.randrange(1,howmany)
    mysound = prouds.pop(mynum)

    # Setup the mixer and play
    pygame.mixer.init()
    pygame.mixer.music.load('sounds/' + mysound)
    pygame.mixer.music.play()

    # Play sound and wait until completed
    # print('Starting to play the WOW')
    # while pygame.mixer.music.get_busy() == True:
    #     continue
    # print('Done playing the WOW')


