import pygame
import os, inspect, sys
from GameObjects.Player import Player
from GameObjects.Bear import Bear
from Tools.MusicManager import MusicManager
from Tools.utils import *
from GameObjects.InGameMenu import InGameMenu
from GameObjects.Level import Level
from GameObjects.Skull import Skull
from GameObjects.Fader import Fader
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
LEVELS = [{"levelFile": "data/Sprites/tmx/lvl1.tmx", "season": Season.SUMMER, "optimalCount": 1},
          {"levelFile": "data/Sprites/tmx/lvl2.tmx", "season": Season.SUMMER, "optimalCount": 1},
          {"levelFile": "data/Sprites/tmx/lvl3.tmx", "season": Season.WINTER, "optimalCount": 1},
          {"levelFile": "data/Sprites/tmx/lvl4.tmx", "season": Season.SPRING, "optimalCount": 1},
          {"levelFile": "data/Sprites/tmx/lvl5.tmx", "season": Season.AUTUMN, "optimalCount": 8},
        ]
INDEX = 0

#Sprites
ICON = pygame.image.load(os.path.join(assets, "Sprites/menu.png"))
MENU_SPRITE = pygame.image.load(os.path.join(assets, "Sprites/menu.png"))
MENU_SPRITE = pygame.transform.scale(MENU_SPRITE, WINDOW_SIZE)
PLAYER_SPRITE = pygame.image.load(os.path.join(assets, "Sprites/player.png"))
BEAR_SPRITE = pygame.image.load(os.path.join(assets, "Sprites/bear.png"))
SKULL_SPRITE = pygame.image.load(os.path.join(assets,"Sprites/skull.png"))
FOND_PAUSE = pygame.image.load(os.path.join(assets,"Sprites/carreBlanc.jpg"))
FOND_PAUSE = pygame.transform.scale(FOND_PAUSE,(1138,640))
FOND_PAUSE.set_alpha(128)

#etat du jeu global
GAMES_OBJECTS = []
GAME_STATE = dict()
GAME_STATE["state"] = State.Menu
GAME_STATE["nextLevel"] = False
GAME_STATE["click"] = False
GAME_STATE["keyPressed"] = None
GAME_STATE["screen"] = SCREEN
GAME_STATE["debug"] = False
GAME_STATE["skullSprite"] = SKULL_SPRITE
GAME_STATE["gameObject"] = GAMES_OBJECTS
GAME_STATE["fading"] = False

 
#titre de la fenetre
pygame.display.set_caption("Orchestral Seasons")

#icone
pygame.display.set_icon(ICON)
 
def loadNextLevel(GAMES_OBJECTS,INDEX):

    if len(LEVELS) == (INDEX) :
        GAME_STATE["state"] = State.End
        return

    GAMES_OBJECTS.clear() #vidange de game object

    nextLevel = LEVELS[INDEX]
    INDEX+=1
    GAMES_OBJECTS.append(Level(nextLevel["levelFile"],GAME_STATE))
    GAME_STATE["player"] = Player(PLAYER_SPRITE,GAME_STATE)
    GAMES_OBJECTS.append(GAME_STATE["player"])
    GAME_STATE["startingSeason"] = nextLevel["season"]
    GAME_STATE["menu"] = InGameMenu(nextLevel["season"], nextLevel["optimalCount"], GAME_STATE)
    GAMES_OBJECTS.append(GAME_STATE["menu"])

    if 'bear' in GAME_STATE['layer_obj']:
        for bear_position in GAME_STATE['layer_obj']['bear']:
            print(bear_position)
            GAMES_OBJECTS.append(Bear((bear_position['rect'].x-16, bear_position['rect'].y-32), BEAR_SPRITE))
    

    GAMES_OBJECTS.append(Fader())
    
#chargement du premier niveau
loadNextLevel(GAMES_OBJECTS,INDEX)
INDEX+=1
print(GAMES_OBJECTS)
for gameObject in GAMES_OBJECTS: #premier draw
    gameObject.draw(GAME_STATE)

while not done:

    if(GAME_STATE["state"] != State.Play):
        GAME_STATE["click"] = False #vidange de l'event click
        event = pygame.event.Event(pygame.USEREVENT)    # Remise à zero de la variable event
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    GAME_STATE["click"] = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                 GAME_STATE["state"] = State.Play
                 break
        
        if (GAME_STATE["state"] == State.Menu):
            main_menu(MENU_SPRITE, GAME_STATE)
            INDEX = 0
        elif (GAME_STATE["state"] == State.Pause):
            draw_pause_menu(GAME_STATE)
        elif GAME_STATE["state"] == State.End :
            end_menu(GAME_STATE)
    
    elif(GAME_STATE["state"] == State.Play):
        event = pygame.event.Event(pygame.USEREVENT)    # Remise à zero de la variable event
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
            #recuperation de la key_down (pas d'action continue si on maintien la touche)
            if event.type == pygame.KEYDOWN and GAME_STATE["keyPressed"] != event.key:
                GAME_STATE["keyPressed"] = event.key
                if event.key == pygame.K_r:
                    GAME_STATE["player"].reset(GAME_STATE)
                if event.key == pygame.K_p:
                    GAME_STATE["click"] = False
                    GAME_STATE["state"] = State.Pause
                    SCREEN.blit(FOND_PAUSE,(0,0))
                elif event.key == pygame.K_F12 :
                    GAME_STATE["debug"] = not GAME_STATE["debug"]
                elif event.key == pygame.K_F11 :
                    GAME_STATE["nextLevel"] = True
                elif event.key == pygame.K_SPACE :
                    print(GAME_STATE['layer_obj'])

            #vidange de la clef stocké
            if event.type == pygame.KEYUP:
                GAME_STATE["keyPressed"] = None

        #si jamais la gestion des keys a changé l'état du jeu on passe au tour suivant
        #(pas d'update et de draw)
        if GAME_STATE["state"] != State.Play :
            continue

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
            loadNextLevel(GAMES_OBJECTS,INDEX)
            INDEX+=1

    #affichage de l'ecran
    pygame.display.flip()
 

pygame.quit()