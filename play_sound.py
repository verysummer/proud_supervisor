import pygame 

# Setup the mixer
pygame.mixer.init()
pygame.mixer.music.load("sounds/wow.mp3")
pygame.mixer.music.play()

# Play sound and wait until completed
print('Starting to play the WOW')
while pygame.mixer.music.get_busy() == True:
    continue
print('Done playing the WOW')
