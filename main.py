import pygame
import os, inspect
from enum import Enum

from helpers import *

class Season(Enum):
    AUTUMN = 1
    WINTER = 2
    SPRING = 3
    SUMMER = 4

#recherche du répertoire de travail
scriptPATH = os.path.abspath(inspect.getsourcefile(lambda:0)) # compatible interactive Python Shell
scriptDIR  = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR,"data")
  
fond = pygame.image.load(os.path.join(assets, "placeholder.png"))

# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [800, 400]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("insert game name")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

musicManager = MusicManager()
musicManager.load_files("autumn", "winter")
musicManager.play("winter")

while not done:
    event = pygame.event.Event(pygame.USEREVENT)    # Remise à zero de la variable event
   
    time = int( pygame.time.get_ticks() / 100 )
    
    # draw background and exit
    screen.blit(fond,(0,0))

    # gestion des évènements
   
    for event in pygame.event.get():  # User did something
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                musicManager.play("autumn")
        
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    clock.tick(30)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 

pygame.quit()