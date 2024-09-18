import os
import pygame
import sys

# Définir le répertoire de travail sur le dossier contenant le script
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'menu.png')

# Initialisation de pygame
pygame.init()

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


# Dimensions de la fenêtre
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Menu d'Accueil du Jeu")

# Charger l'image de fond
try:
    background_image = pygame.image.load(image_path)  # Utilisation du chemin complet
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
except pygame.error as e:
    print(f"Erreur lors du chargement de l'image : {e}")
    pygame.quit()
    sys.exit()

# Police de caractère
font = pygame.font.Font(None, 74)

# Fonctions pour afficher les options du menu
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

# Boucle principale
def main_menu():
    while True:
        # Afficher l'image de fond
        screen.blit(background_image, (0, 0))
        font = pygame.font.Font(pygame.font.match_font('papyrus'), 70)
        draw_text('Nom du Jeu', font, DEEP_BLUE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 9-15)
        font = pygame.font.Font(None, 50)
        mx, my = pygame.mouse.get_pos()

        # Création des rectangles des options
        button_1 = pygame.Rect(SCREEN_WIDTH // 2 - 350, SCREEN_HEIGHT // 2 +225, 200, 50)
        button_2 = pygame.Rect(SCREEN_WIDTH // 2 -100, SCREEN_HEIGHT // 2 + 225, 200, 50)
        button_3 = pygame.Rect(SCREEN_WIDTH // 2 + 150, SCREEN_HEIGHT // 2+ 225, 200, 50)

        # Vérification si le curseur est sur un bouton
        if button_1.collidepoint((mx, my)):
            pygame.draw.rect(screen, GRAY, button_1)
            if click:
                game()
        else:
            pygame.draw.rect(screen,LIGHT_GREEN, button_1)

        if button_2.collidepoint((mx, my)):
            pygame.draw.rect(screen, GRAY, button_2)
            if click:
                options()
        else:
            pygame.draw.rect(screen, LIGHT_BLUE, button_2)

        if button_3.collidepoint((mx, my)):
            pygame.draw.rect(screen, GRAY, button_3)
            if click:
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(screen, MEDIUM_RED, button_3)

        # Affichage du texte sur les boutons
        draw_text('Jouer', font, DEEP_GREEN, screen, SCREEN_WIDTH // 2-250, SCREEN_HEIGHT // 2 +250)
        draw_text('Options', font,DEEP_BLUE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 250)
        draw_text('Quitter', font, DEEP_RED, screen, SCREEN_WIDTH // 2+250, SCREEN_HEIGHT // 2 + 250)

        # Gestion des événements
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

# Fonction du jeu
def game():
    running = True
    while running:
        screen.fill(WHITE)
        draw_text('Jeu en cours...', font, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

# Fonction pour les options
def options():
    running = True
    while running:
        screen.fill(WHITE)
        draw_text('Options', font, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

# Lancement du menu principal
main_menu()
