import pygame
from Tools.MusicManager import MusicManager
from Tools.utils import Season

class InGameMenu:
    current_season = Season.SUMMER
    seasons_icons = pygame.transform.scale(pygame.image.load("data/Sprites/seasons.png"), (100,100))
    keyboard_icons = pygame.transform.scale(pygame.image.load("data/Sprites/keyboard.png"), (512, 162))
    side_image = pygame.transform.scale(pygame.image.load("data/Sprites/side.png"), (200, 660))
    
    music_manager = MusicManager()
    music_manager.load_files("hiver","printemps","ete","automne")

    def __init__(self, season, season_counter, GAME_STATE):
        self.current_season = season
        self.change_season(GAME_STATE)
        self.season_counter = season_counter
        self.total_counter = season_counter

    def update(self, GAME_STATE):
        if self.season_counter != 0:
            keyPressed = GAME_STATE["keyPressed"]
            old_counter = self.season_counter
            self.season_counter -= 1
            if (keyPressed == pygame.K_1 or keyPressed == pygame.K_KP1) and self.current_season != Season.WINTER:
                self.current_season = Season.WINTER
            elif (keyPressed == pygame.K_2 or keyPressed == pygame.K_KP2) and self.current_season != Season.SPRING:
                self.current_season = Season.SPRING
            elif (keyPressed == pygame.K_3 or keyPressed == pygame.K_KP3) and self.current_season != Season.SUMMER:
                self.current_season = Season.SUMMER
            elif (keyPressed == pygame.K_4 or keyPressed == pygame.K_KP4) and self.current_season != Season.AUTUMN:
                self.current_season = Season.AUTUMN
            else: self.season_counter += 1

            if old_counter != self.season_counter:
                self.change_season(GAME_STATE)

    def change_season(self, GAME_STATE):
        GAME_STATE["saison"] = self.current_season
        GAME_STATE["active_layer"] = GAME_STATE["saison"].value
        self.music_manager.play(self.current_season.value)

    def draw(self, GAME_STATE):
        font = pygame.font.Font(None, 60)
        GAME_STATE["screen"].blit(self.side_image, (950, -10))
        for season in Season:
            index = ["hiver","printemps","ete","automne"].index(season.value)
            self.seasons_icons.set_alpha(255 if self.current_season.value==season.value else 100)
            GAME_STATE["screen"].blit(self.seasons_icons, (1030, 100 * index + 25), ((index%2) * 52, (index//2) * 52, 50, 50))
            GAME_STATE["screen"].blit(self.keyboard_icons, (1080, 100 * index + 37), (index*26 + 118, 26, 24, 24))
        textobj = font.render(str(self.season_counter) if self.season_counter<100 else "+99", True, (255, 255, 255))
        textrect = textobj.get_rect(center=(1070, 560))
        GAME_STATE["screen"].blit(textobj, textrect)
        font = pygame.font.Font(None, 20)
        textobj = font.render("changements", True, (255, 255, 255))
        textrect = textobj.get_rect(center=(1070, 590))
        GAME_STATE["screen"].blit(textobj, textrect)
        textobj = font.render("autorisés", True, (255, 255, 255))
        textrect = textobj.get_rect(center=(1070, 610))
        GAME_STATE["screen"].blit(textobj, textrect)
