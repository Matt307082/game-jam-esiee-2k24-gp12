import pygame
from Tools.MusicManager import MusicManager
from Tools.utils import Season

class InGameMenu:
    current_season = Season.SUMMER
    seasons_icons = pygame.transform.scale(pygame.image.load("data/Sprites/seasons.png"), (100,100))
    music_manager = MusicManager()
    music_manager.load_files("autumn", "winter","spring","summer")
    music_manager.play("summer")

    def update(self, GAME_STATE):
        keyPressed = GAME_STATE["keyPressed"]
        GAME_STATE["saison"] = self.current_season
        GAME_STATE["active_layer"] = GAME_STATE["saison"].value

        if keyPressed == pygame.K_1 :
            self.current_season = Season.WINTER
            GAME_STATE["saison"] = Season.WINTER
            self.music_manager.play("winter")
        elif keyPressed == pygame.K_2 :
            self.current_season = Season.SPRING
            GAME_STATE["saison"] = Season.SPRING
            self.music_manager.play("spring")
        elif keyPressed == pygame.K_3 :
            self.current_season = Season.SUMMER
            GAME_STATE["saison"] = Season.SUMMER
            self.music_manager.play("summer")
        elif keyPressed == pygame.K_4 :
            self.current_season = Season.AUTUMN
            GAME_STATE["saison"] = Season.AUTUMN
            self.music_manager.play("autumn")

        GAME_STATE["active_layer"] = GAME_STATE["saison"].value

    def draw(self, GAME_STATE):
        for season in Season:
            index = ["hiver","printemps","ete","automne"].index(season.value)
            self.seasons_icons.set_alpha(255 if self.current_season.value==season.value else 100)
            GAME_STATE["screen"].blit(self.seasons_icons, (60 * index + 25, 25), ((index%2) * 52, (index//2) * 52, 50, 50))
