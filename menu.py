import pygame
from Tools.utils import WINDOW_SIZE, State

# Couleurs
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
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
    font = pygame.font.Font(pygame.font.match_font('papyrus'), 70)
    draw_text('Nom du Jeu', font, DEEP_BLUE, screen, WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 9-15)
    font = pygame.font.Font(None, 50)
    mx, my = pygame.mouse.get_pos()

    # Création des rectangles des options
    button_1 = pygame.Rect(WINDOW_SIZE[0] // 2 - 350, WINDOW_SIZE[1] // 2 +225, 200, 50)
    button_2 = pygame.Rect(WINDOW_SIZE[0] // 2 -100, WINDOW_SIZE[1] // 2 + 225, 200, 50)
    button_3 = pygame.Rect(WINDOW_SIZE[0] // 2 + 150, WINDOW_SIZE[1] // 2+ 225, 200, 50)

    # Vérification si le curseur est sur un bouton
    if button_1.collidepoint((mx, my)):
        pygame.draw.rect(screen, GRAY, button_1)
        if click:
            GAME_STATE["state"] = State.Play
    else:
        pygame.draw.rect(screen,LIGHT_GREEN, button_1)

    if button_2.collidepoint((mx, my)):
        pygame.draw.rect(screen, GRAY, button_2)
        if click:
            print("Options are comming soon")
    else:
        pygame.draw.rect(screen, LIGHT_BLUE, button_2)

    if button_3.collidepoint((mx, my)):
        pygame.draw.rect(screen, GRAY, button_3)
        if click:
            pygame.quit()
    else:
        pygame.draw.rect(screen, MEDIUM_RED, button_3)

    # Affichage du texte sur les boutons
    draw_text('Jouer', font, DEEP_GREEN, screen, WINDOW_SIZE[0] // 2-250, WINDOW_SIZE[1] // 2 +250)
    draw_text('Options', font,DEEP_BLUE, screen, WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 250)
    draw_text('Quitter', font, DEEP_RED, screen, WINDOW_SIZE[0] // 2+250, WINDOW_SIZE[1] // 2 + 250)


def draw_selection_screen(background_image, GAME_STATE):
    screen = GAME_STATE["screen"]
    click = GAME_STATE["click"]
    screen.blit(background_image, (0, 0))
    button_1 = pygame.Rect(WINDOW_SIZE[0]//2 - 200, 100, 400, 50)
    button_2 = pygame.Rect(WINDOW_SIZE[0]//2 - 200, 300, 400, 50)
    button_3 = pygame.Rect(WINDOW_SIZE[0]//2 - 200, 500, 400, 50)
    pygame.draw.rect(screen,LIGHT_GREEN, button_1)
    pygame.draw.rect(screen, LIGHT_BLUE, button_2)
    pygame.draw.rect(screen, MEDIUM_RED, button_3)
    font = pygame.font.Font(None, 50)

    mx, my = pygame.mouse.get_pos()
    if button_1.collidepoint((mx, my)):
        pygame.draw.rect(screen, GRAY, button_1)
        if click:
            GAME_STATE["player"].reset(GAME_STATE)
            GAME_STATE["state"] = State.Play
    else:
        pygame.draw.rect(screen,LIGHT_GREEN, button_1)

    if button_2.collidepoint((mx, my)):
        pygame.draw.rect(screen, GRAY, button_2)
        if click:
            GAME_STATE["player"].reset(GAME_STATE)
            GAME_STATE["click"] = False
            GAME_STATE["state"] = State.Menu
    else:
        pygame.draw.rect(screen, LIGHT_BLUE, button_2)

    if button_3.collidepoint((mx, my)):
        pygame.draw.rect(screen, GRAY, button_3)
        if click:
            pygame.quit()
    else:
        pygame.draw.rect(screen, MEDIUM_RED, button_3)

    draw_text('Recommencer', font, DEEP_GREEN, screen, WINDOW_SIZE[0]//2, 125)
    draw_text('Menu Principal', font,DEEP_BLUE, screen, WINDOW_SIZE[0]//2, 325)
    draw_text('Quitter', font, DEEP_RED, screen, WINDOW_SIZE[0]//2, 525)