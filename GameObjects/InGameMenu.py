import pygame
from Tools.MusicManager import MusicManager
from Tools.utils import Season

class InGameMenu:
    current_season = Season.SUMMER
    seasons_icons = pygame.transform.scale(pygame.image.load("data/Sprites/seasons.png"), (100,100))
    season_counter = 0
    music_manager = MusicManager()

    def __init__(self, season, GAME_STATE):
        self.current_season = season
        GAME_STATE["saison"] = season
        GAME_STATE["active_layer"] = GAME_STATE["saison"].value
        self.music_manager.play(self.current_season.value)

    def update(self, GAME_STATE):
        keyPressed = GAME_STATE["keyPressed"]

        old_counter = self.season_counter
        self.season_counter += 1
        if keyPressed == pygame.K_1 and self.current_season != Season.WINTER:
            self.current_season = Season.WINTER
        elif keyPressed == pygame.K_2 and self.current_season != Season.SPRING:
            self.current_season = Season.SPRING
        elif keyPressed == pygame.K_3 and self.current_season != Season.SUMMER:
            self.current_season = Season.SUMMER
        elif keyPressed == pygame.K_4 and self.current_season != Season.AUTUMN:
            self.current_season = Season.AUTUMN
        else: self.season_counter -= 1

        if old_counter != self.season_counter:
            GAME_STATE["saison"] = self.current_season
            GAME_STATE["active_layer"] = GAME_STATE["saison"].value
            self.music_manager.play(self.current_season.value)

    def draw(self, GAME_STATE):
        for season in Season:
            index = ["hiver","printemps","ete","automne"].index(season.value)
            self.seasons_icons.set_alpha(255 if self.current_season.value==season.value else 100)
            GAME_STATE["screen"].blit(self.seasons_icons, (60 * index + 25, 25), ((index%2) * 52, (index//2) * 52, 50, 50))
            font = pygame.font.Font(None, 60)
            textobj = font.render(str(self.season_counter), True, (255, 255, 255))
            textrect = textobj.get_rect(midleft=(275, 50))
            GAME_STATE["screen"].blit(textobj, textrect)
