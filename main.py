import pygame
import os, inspect
from GameObjects.Player import Player
from GameObjects.Bear import Bear
from Tools.MusicManager import MusicManager
from Tools.utils import *
from GameObjects.InGameMenu import InGameMenu
from GameObjects.Level import Level
from menu import *

# Initialize pygame
pygame.init()

# Loop until the user clicks the close button.
done = False

#répertoire de travail
scriptPATH = os.path.abspath(inspect.getsourcefile(lambda:0)) # compatible interactive Python Shell
scriptDIR  = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR,"data")
  
#Variables 
#FOND = pygame.image.load(os.path.join(assets, "placeholder.png"))
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
LEVELS = ["data/Sprites/tmx/lvl1.tmx"]

#Sprites
MENU_SPRITE = pygame.image.load(os.path.join(assets, "Sprites/menu.png"))
MENU_SPRITE = pygame.transform.scale(MENU_SPRITE, WINDOW_SIZE)
PLAYER_SPRITE = pygame.image.load(os.path.join(assets, "Sprites/player.png"))
BEAR_SPRITE = pygame.image.load(os.path.join(assets, "Sprites/bear.png"))

#etat du jeu global
GAME_STATE = dict()
GAME_STATE["state"] = State.Menu
GAME_STATE["nextLevel"] = False
GAME_STATE["click"] = False
GAME_STATE["keyPressed"] = None
GAME_STATE["screen"] = SCREEN
GAME_STATE["debug"] = False
GAMES_OBJECTS = []
 
#titre de la fenetre
pygame.display.set_caption("Nom de code  : Vivaldi")
 
def loadNextLevel(GAMES_OBJECTS):
    GAMES_OBJECTS.clear() #vidange de game object

    pathNextLevel = LEVELS.pop()
    GAMES_OBJECTS.append(Level("data/Sprites/tmx/lvl1.tmx",GAME_STATE))
    GAME_STATE["player"] = Player(PLAYER_SPRITE,GAME_STATE)
    GAMES_OBJECTS.append(GAME_STATE["player"])
    GAMES_OBJECTS.append(InGameMenu(Season.SUMMER, GAME_STATE))
    GAMES_OBJECTS.append(Bear((100,100), BEAR_SPRITE))
    return

#chargement du premier niveau
loadNextLevel(GAMES_OBJECTS)
print(GAMES_OBJECTS)
for gameObject in GAMES_OBJECTS: #premier draw
    gameObject.draw(GAME_STATE)

while not done:

    if(GAME_STATE["state"] == State.Menu):
        event = pygame.event.Event(pygame.USEREVENT)    # Remise à zero de la variable event
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    GAME_STATE["click"] = True
        
        main_menu(MENU_SPRITE, GAME_STATE)

    if(GAME_STATE["state"] == State.Pause):
        event = pygame.event.Event(pygame.USEREVENT)    # Remise à zero de la variable event
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    GAME_STATE["click"] = True
        
        draw_selection_screen(MENU_SPRITE, GAME_STATE)
    
    if(GAME_STATE["state"] == State.Play):
        event = pygame.event.Event(pygame.USEREVENT)    # Remise à zero de la variable event
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                pygame.quit()
    
            #recuperation de la key_down (pas d'action continue si on maintien la touche)
            if event.type == pygame.KEYDOWN and GAME_STATE["keyPressed"] != event.key:
                GAME_STATE["keyPressed"] = event.key
                if event.key == pygame.K_r:
                    GAME_STATE["player"].reset(GAME_STATE)
                if event.key == pygame.K_m:
                    GAME_STATE["click"] = False
                    GAME_STATE["state"] = State.Pause
                if event.key == pygame.K_d :
                    GAME_STATE["debug"] = not GAME_STATE["debug"]
            
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

    #affichage de l'ecran
    pygame.display.flip()
 

pygame.quit()