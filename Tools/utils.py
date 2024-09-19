import pygame
from enum import Enum

WINDOW_SIZE = [960, 640]

# Etat courant du jeu
class State(Enum):
    Menu = 0
    Play = 1
    Pause = 2

# Saison courante 
class Season(Enum):
    WINTER = "hiver"
    SPRING = "printemps"
    SUMMER = "ete"
    AUTUMN = "automne"

def ChargeSerieSprites(id, spritesheet, sprite_dimensions, p_range):
   # Taille d'un sprite
    LARG = sprite_dimensions[0] # Largeur d'un sprite
    HAUT = sprite_dimensions[1] # Hauteur d'un sprite
    sprite = []
    for i in range(p_range):
            spr = spritesheet.subsurface((LARG * i, HAUT * id, LARG, HAUT))
            sprite.append( spr )
    return sprite