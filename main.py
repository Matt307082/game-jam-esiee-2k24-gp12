import pygame
import os, inspect
from Player import Player
from Tools.MusicManager import MusicManager
from Tools.utils import *
from GameObjects.InGameMenu import InGameMenu
import pytmx

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
LEVELS = []

#Sprites
PLAYER_SPRITE = pygame.image.load(os.path.join(assets, "Sprites/player.png"))

#etat du jeu global
GAME_STATE = dict()
GAME_STATE["playing"] = True
GAME_STATE["nextLevel"] = False
GAME_STATE["keyPressed"] = None
GAME_STATE["screen"] = SCREEN
GAME_STATE["player"] = Player((50,50),PLAYER_SPRITE)
GAMES_OBJECTS = [GAME_STATE["player"],InGameMenu()]

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


#===============TMX
tmx_data = pytmx.load_pygame("data/Sprites/tmx/lvl1.tmx")
layer_obj = {}

def get_collision_objects_by_layer(tmx_data):
    layers = {}
    for layer in tmx_data.layers:
        if isinstance(layer, pytmx.TiledObjectGroup):  # Si c'est un layer d'objets
            collision_objects = []
            for obj in layer:
                # On cherche les objets ayant la propriété 'class' == 'block' ou un type 'block'
                if obj.type == 'block' or obj.properties.get('class') == 'block':
                    # Stocker le nom de l'objet et son rectangle
                    collision_objects.append({
                        "name": obj.name,
                        "rect": pygame.Rect(obj.x, obj.y, obj.width, obj.height)
                    })
            layers[layer.name] = collision_objects
    return layers

layer_obj = get_collision_objects_by_layer(tmx_data)


GAME_STATE["active_layer"] = "ete"
GAME_STATE["layer_obj"] = layer_obj
def draw_map(screen, tmx_data, active_layer):
    for layer in tmx_data.layers:
        if isinstance(layer, pytmx.TiledTileLayer) and layer.name == active_layer:
            for x, y, gid in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    screen.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))

def debugColide(active_layer):
    font = pygame.font.Font(None, 24)
    realActiveLayer = active_layer + "Obj"

    debugText = {
        "DEBUG": "COLLISION",
        "active_layer": active_layer,
        "Object": realActiveLayer
    }
    pygame.draw.rect(SCREEN, (255, 255, 255), (0, 0, 200, debugText.__len__() * 20))
    debugTextY = 0
    for key, value in debugText.items():
        textDebug = font.render(key + ": " + value, True, (0, 0, 0))
        SCREEN.blit(textDebug, (0, debugTextY))
        debugTextY += 20

    if realActiveLayer in layer_obj:
        for obj in layer_obj[realActiveLayer]:
            pygame.draw.rect(SCREEN, (0, 255, 0), obj["rect"], 2)
            if obj["name"]:
                text_surface = font.render(obj["name"], True, (0, 0, 0))
                SCREEN.blit(text_surface, (obj["rect"].x, obj["rect"].y - 20))



#===============


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
            SCREEN.fill((0,0,0)) #ecran noir pour l'instant
            draw_map(SCREEN, tmx_data, GAME_STATE["active_layer"])
            debugColide(GAME_STATE["active_layer"])
            for gameObject in GAMES_OBJECTS:
                gameObject.draw(GAME_STATE)
        
        #vidange de la clef stocké
        if event.type == pygame.KEYUP:
            GAME_STATE["keyPressed"] = None

    #passage du niveau si besoin
    if GAME_STATE["nextLevel"]:
        GAME_STATE["nextLevel"] = False
        loadNextLevel()

    #affichage de l'ecran
    pygame.display.flip()
 

pygame.quit()