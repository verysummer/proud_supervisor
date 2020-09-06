import pygame
import os
import random
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

# setuo gpio
pin = 23
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # not Use physical pin numbering
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


random.seed
prouds = ['nothing in here']

while True:
    #input("waiting for input")
    if GPIO.input(pin) == GPIO.HIGH:
        print("pushed")
#    else:
#        print("nope")

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


