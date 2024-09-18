import pygame
import os, inspect
from enum import Enum

from helpers import *

class Season(Enum):
    AUTUMN = 1
    WINTER = 2
    SPRING = 3
    SUMMER = 4

# Initialize pygame
pygame.init()

#répertoire de travail
scriptPATH = os.path.abspath(inspect.getsourcefile(lambda:0)) # compatible interactive Python Shell
scriptDIR  = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR,"data")
  
#Variables 
#FOND = pygame.image.load(os.path.join(assets, "placeholder.png"))
WINDOW_SIZE = [800, 400]
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
LEVELS = []

#etat du jeu global
GAMES_OBJECTS = []
GAME_STATE = dict()
GAME_STATE["playing"] = True
GAME_STATE["nextLevel"] = False
GAME_STATE["keyPressed"] = None

 
#titre de la fenetre
pygame.display.set_caption("Nom de code  : Vivaldi")
 
def loadNextLevel():
    GAMES_OBJECTS = [] #vidange de game object

    objetATraiter = LEVELS.pop()

    #ajouter les games objects, changer la saison...

    return

#chargement du premier niveau
loadNextLevel()
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

while GAME_STATE["playing"]:
    
    #recupération d'un evenement
    event = pygame.event.Event(pygame.USEREVENT)    # Remise à zero de la variable event
    for event in pygame.event.get():  
        
        #si le joueur quitte la partie
        if event.type == pygame.QUIT:  
            GAME_STATE["playing"] = False 

        #recuperation de la key_down (pas d'action continue si on maintien la touche)
        if event.type == pygame.KEYDOWN and GAME_STATE["keyPressed"] != event.key:
            GAME_STATE["keyPressed"] = event.key 

            #update des objets
            for gameObject in GAMES_OBJECTS:
                gameObject.update(GAME_STATE)

            #draw des objets (seulement si y'a eu des updates du coup)
            for gameObject in GAMES_OBJECTS:
                gameObject.draw(GAME_STATE)
        
        #vidange de la clef stocké
        if event.type == pygame.KEYUP:
            GAME_STATE["keyPressed"] = None

    #passage du niveau si besoin
    if GAME_STATE["nextLevel"]:
        GAME_STATE["nextLevel"] = False
        loadNextLevel()


    #Affichage de l'écran
   
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