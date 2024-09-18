import pygame

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [960, 640]

def ChargeSerieSprites(id, spritesheet, dimensions):
   # Taille d'un sprite
    LARG = dimensions[0]
    HAUT = dimensions[1]
    sprite = []
    for i in range(4):
            spr = spritesheet.subsurface((LARG * i, HAUT * id, LARG, HAUT))
            sprite.append( spr )
    return sprite