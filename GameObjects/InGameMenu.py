import pygame
from enum import Enum
pygame.init()

class Season(Enum):
    WINTER = "hiver"
    SPRING = "printemps"
    SUMMER = "ete"
    AUTUMN = "automne"

class InGameMenu:
    current_season = Season.SUMMER
    seasons_icons = pygame.transform.scale(pygame.image.load("data/Sprites/seasons.png"), (100,100))

    def update(this, GAME_STATE):
        keyPressed = GAME_STATE["keyPressed"]
        GAME_STATE["saison"] = this.current_season
        GAME_STATE["active_layer"] = GAME_STATE["saison"].value

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

        GAME_STATE["active_layer"] = GAME_STATE["saison"].value

    def draw(this, GAME_STATE):
        for season in Season:
            this.seasons_icons.set_alpha(255 if this.current_season.value==season.value else 0)
            GAME_STATE["screen"].blit(this.seasons_icons, (60 + 25, 25), ((0%2) * 52, (0//2) * 52, 50, 50))
