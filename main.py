import pygame
import os, inspect
from GameObjects.Player import Player
from GameObjects.Bear import Bear
from Tools.MusicManager import MusicManager
from Tools.utils import *
from GameObjects.InGameMenu import InGameMenu

# Initialize pygame
pygame.init()

#répertoire de travail
scriptPATH = os.path.abspath(inspect.getsourcefile(lambda:0)) # compatible interactive Python Shell
scriptDIR  = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR,"data")
  
#Variables 
#FOND = pygame.image.load(os.path.join(assets, "placeholder.png"))
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
LEVELS = []

#Sprites
PLAYER_SPRITE = pygame.image.load(os.path.join(assets, "Sprites/player.png"))
BEAR_SPRITE = pygame.image.load(os.path.join(assets, "Sprites/bear.jpg"))

#etat du jeu global
GAMES_OBJECTS = [Player((100,100),PLAYER_SPRITE),InGameMenu(),Bear((200,200),BEAR_SPRITE)]
GAME_STATE = dict()
GAME_STATE["playing"] = True
GAME_STATE["nextLevel"] = False
GAME_STATE["keyPressed"] = None
GAME_STATE["screen"] = SCREEN

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#chargement musique
musicManager = MusicManager()
musicManager.load_files("autumn", "winter")
musicManager.play("winter")
 
#titre de la fenetre
pygame.display.set_caption("Nom de code  : Vivaldi")
 
def loadNextLevel():
    GAMES_OBJECTS = [] #vidange de game object

    #objetATraiter = LEVELS.pop()

    #ajouter les games objects, changer la saison...

    return

#chargement du premier niveau
loadNextLevel()
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

    #draw des objets (seulement si y'a eu des updates du coup)
    SCREEN.fill((0,0,0)) #ecran noir pour l'instant
    for gameObject in GAMES_OBJECTS:
        gameObject.draw(GAME_STATE)

    #passage du niveau si besoin
    if GAME_STATE["nextLevel"]:
        GAME_STATE["nextLevel"] = False
        loadNextLevel()

    clock.tick(30)

    #affichage de l'ecran
    pygame.display.flip()
 

pygame.quit()