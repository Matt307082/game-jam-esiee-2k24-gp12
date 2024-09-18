import pygame

WINDOW_SIZE = [800, 400]

def ChargeSerieSprites(id, spritesheet, sprite_dimensions, p_range):
   # Taille d'un sprite
    LARG = sprite_dimensions[0] # Largeur d'un sprite
    HAUT = sprite_dimensions[1] # Hauteur d'un sprite
    sprite = []
    for i in range(p_range):
            spr = spritesheet.subsurface((LARG * i, HAUT * id, LARG, HAUT))
            sprite.append( spr )
    return sprite