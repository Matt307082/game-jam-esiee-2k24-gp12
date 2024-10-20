import pygame
import sys
import os, inspect
from Tools.utils import WINDOW_SIZE, State

# Couleurs
WHITE = (255, 255, 255)
GRAY = (100, 100, 100,128)
RED = (255, 0, 0)
PINK = (200,0,0)

PINK_LIGHT = (255, 182, 193)  # Rose clair
PINK_MEDIUM = (255, 105, 180) # Rose moyen
PINK_DEEP = (255, 20, 147)    # Rose foncé
RED_AUTUMN = (255, 99, 71)     # Rouge automne
LIGHT_BLUE = (173, 216, 230)   # Bleu clair
LIGHT_GREEN = (144, 238, 144)  # Vert clair
LIGHT_PINK = (255, 182, 193)   # Rose clair

# Couleurs pour Rouge
LIGHT_RED = (255, 182, 193)    # Rouge clair
MEDIUM_RED = (255, 99, 71)     # Rouge moyen
DEEP_RED = (139, 0, 0)         # Rouge foncé

# Couleurs pour Bleu
LIGHT_BLUE = (173, 216, 230)   # Bleu clair
MEDIUM_BLUE = (70, 130, 180)   # Bleu moyen
DEEP_BLUE = (0, 0, 139)        # Bleu foncé

# Couleurs pour Vert
LIGHT_GREEN = (144, 238, 144)  # Vert clair
MEDIUM_GREEN = (50, 205, 50)   # Vert moyen
DEEP_GREEN = (0, 100, 0)       # Vert foncé

# Police de caractère
font = pygame.font.Font(None, 74)

#Import sprite
#répertoire de travail
scriptPATH = os.path.abspath(inspect.getsourcefile(lambda:0)) # compatible interactive Python Shell
scriptDIR  = os.path.dirname(scriptPATH)
assets = os.path.join(scriptDIR,"data")
PAUSE_SPRITE = pygame.image.load(os.path.join(assets, "Sprites/PauseMenu.png"))
MENU_FIN = pygame.image.load(os.path.join(assets, "Sprites/ecranFin.png"))

# Fonctions pour afficher les options du menu
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

# Boucle principale
def main_menu(background_image,GAME_STATE):
    screen = GAME_STATE["screen"]
    click = GAME_STATE["click"]
    # Afficher l'image de fond
    screen.blit(background_image, (0, 0))
    
    font = pygame.font.Font(None, 50)
    mx, my = pygame.mouse.get_pos()

    # Création des rectangles des options


    button_1 = pygame.Rect(WINDOW_SIZE[0] // 2 - 90, WINDOW_SIZE[1] // 2 +20, 180, 30)
    button_3 = pygame.Rect(WINDOW_SIZE[0] // 2  -70 , WINDOW_SIZE[1] // 2+ 90, 140, 30)

    # Vérification si le curseur est sur un bouton
    if button_1.collidepoint((mx, my)):
        if click:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            GAME_STATE["state"] = State.Play
            GAME_STATE["nextLevel"] = True
        else:
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)
            


    elif button_3.collidepoint((mx, my)):
        if click:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            pygame.quit()
            sys.exit()
        else:
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)

    else: pygame.mouse.set_cursor(*pygame.cursors.arrow)



def draw_pause_menu(GAME_STATE):
    screen = GAME_STATE["screen"]
    click = GAME_STATE["click"]
    GAME_STATE["keyPressed"] = None
    button_1 = pygame.Rect(461, 349, 227, 54)
    button_2 = pygame.Rect(461, 413, 227, 54)
    button_3 = pygame.Rect(485, 480, 179, 51)
    
    #afficher nouveau menu
    screen.blit(PAUSE_SPRITE,(206,58))

    mx, my = pygame.mouse.get_pos()
    if button_1.collidepoint((mx, my)):
        if click:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            GAME_STATE["player"].reset(GAME_STATE)
            GAME_STATE["state"] = State.Play
        else:
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)

    elif button_2.collidepoint((mx, my)):
        if click:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            GAME_STATE["click"] = False
            GAME_STATE["state"] = State.Menu
        else:
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)

    elif button_3.collidepoint((mx, my)):
        if click:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            pygame.quit()
            sys.exit()
            exit(0)
        else:
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)
    else: pygame.mouse.set_cursor(*pygame.cursors.arrow)

def end_menu(GAME_STATE) :
    screen = GAME_STATE["screen"]
    click = GAME_STATE["click"]
    GAME_STATE["keyPressed"] = None
    
    button = pygame.Rect(387, 544, 380, 61)

    screen.blit(MENU_FIN,(0,0))

    mx, my = pygame.mouse.get_pos()
    if button.collidepoint((mx, my)):
        if click:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            GAME_STATE["click"] = False
            GAME_STATE["state"] = State.Menu
            GAME_STATE["nextLevel"] = True
        else:
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)
    else:
        pygame.mouse.set_cursor(*pygame.cursors.arrow)

