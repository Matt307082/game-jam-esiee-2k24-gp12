import pygame
from enum import Enum
pygame.init()

class Season(Enum):
    WINTER = 0
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3

class InGameMenu:
    current_season = Season.SPRING
    seasons_icons = pygame.transform.scale(pygame.image.load("data/Sprites/seasons.png"), (100,100))

    def update(this, GAME_STATE):
        keyPressed = GAME_STATE["keyPressed"]

        if keyPressed == pygame.K_1 :
            this.current_season = Season.WINTER
            GAME_STATE["saison"] = Season.WINTER
        elif keyPressed == pygame.K_2 :
            this.current_season = Season.SPRING
            GAME_STATE["saison"] = Season.SPRING
        elif keyPressed == pygame.K_3 :
            this.current_season = Season.SUMMER
            GAME_STATE["saison"] = Season.SUMMER
        elif keyPressed == pygame.K_4 :
            this.current_season = Season.AUTUMN
            GAME_STATE["saison"] = Season.AUTUMN

    def draw(this, GAME_STATE):
        for season in Season:
            this.seasons_icons.set_alpha(255 if this.current_season.value==season.value else 100)
            GAME_STATE["screen"].blit(this.seasons_icons, (60*season.value + 25, 25), ((season.value%2) * 52, (season.value//2) * 52, 50, 50))
