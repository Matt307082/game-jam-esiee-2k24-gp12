import pygame

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [800, 400]
screen = pygame.display.set_mode(WINDOW_SIZE)


def ChargeSerieSprites(id, spritesheet, sheet_dimensions, num_sprites):
   # Taille d'un sprite
    LARG = sheet_dimensions[0] // num_sprites[0]  # Largeur d'un sprite
    HAUT = sheet_dimensions[1] // num_sprites[1] # Hauteur d'un sprite
    sprite = []
    for i in range(4):
            spr = spritesheet.subsurface((LARG * i, HAUT * id, LARG, HAUT))
            sprite.append( spr )
    return sprite