import pygame
import os, inspect
from Player import Player
from Tools.MusicManager import MusicManager
from Tools.utils import *
from GameObjects.InGameMenu import InGameMenu
from GameObjects.Level import Level
from GameObjects.Bear import Bear

# Initialize pygame
pygame.init()

#répertoire de travail
scriptPATH = os.path.abspath(inspect.getsourcefile(lambda:0)) # compatible interactive Python Shell
scriptDIR  = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR,"data")
  
#Variables 
#FOND = pygame.image.load(os.path.join(assets, "placeholder.png"))
WINDOW_SIZE = [960, 640]
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
LEVELS = ["data/Sprites/tmx/lvl1.tmx"]

#Sprites
PLAYER_SPRITE = pygame.image.load(os.path.join(assets, "Sprites/player.png"))
BEAR_SPRITE = pygame.image.load(os.path.join(assets, "Sprites/bear.jpg"))

#etat du jeu global
GAME_STATE = dict()
GAME_STATE["playing"] = True
GAME_STATE["nextLevel"] = False
GAME_STATE["keyPressed"] = None
GAME_STATE["screen"] = SCREEN
GAME_STATE["player"] = Player((50,50),PLAYER_SPRITE)
GAMES_OBJECTS = []
 
#titre de la fenetre
pygame.display.set_caption("Nom de code  : Vivaldi")
 
def loadNextLevel(GAMES_OBJECTS):
    GAMES_OBJECTS.clear() #vidange de game object

    pathNextLevel = LEVELS.pop()
    GAMES_OBJECTS.append(Level(pathNextLevel,GAME_STATE))
    GAMES_OBJECTS.append(GAME_STATE["player"])
    GAMES_OBJECTS.append(Bear((250,250),BEAR_SPRITE))
    GAMES_OBJECTS.append(InGameMenu())
    return

#chargement du premier niveau
loadNextLevel(GAMES_OBJECTS)
print(GAMES_OBJECTS)
for gameObject in GAMES_OBJECTS: #premier draw
    gameObject.draw(GAME_STATE)


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
        
        #vidange de la clef stocké
        if event.type == pygame.KEYUP:
            GAME_STATE["keyPressed"] = None

    #update des objets
    for gameObject in GAMES_OBJECTS:
        gameObject.update(GAME_STATE)

    #dessin de la grille 
    SCREEN.fill((0,0,0)) #ecran noir pour l'instant
    for gameObject in GAMES_OBJECTS:
        gameObject.draw(GAME_STATE)
    

    #passage du niveau si besoin
    if GAME_STATE["nextLevel"]:
        GAME_STATE["nextLevel"] = False
        loadNextLevel()

    #affichage de l'ecran
    pygame.display.flip()
 

pygame.quit()