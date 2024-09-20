import pygame
from Tools.MusicManager import MusicManager
from Tools.utils import Season

class InGameMenu:
    season_counter = 0
    seasons_icons = pygame.transform.scale(pygame.image.load("data/Sprites/seasons.png"), (100,100))
    keyboard_icons = pygame.transform.scale(pygame.image.load("data/Sprites/keyboard.png"), (512, 162))
    side_image = pygame.transform.scale(pygame.image.load("data/Sprites/side.png"), (200, 660))
    
    music_manager = MusicManager()
    music_manager.load_files("hiver","printemps","ete","automne")

    def __init__(self, season, optimal_count, GAME_STATE):
        self.current_season = season
        self.change_season(GAME_STATE)
        self.optimal_count = optimal_count

    def update(self, GAME_STATE):
        keyPressed = GAME_STATE["keyPressed"]
        old_counter = self.season_counter
        self.season_counter += 1
        if (keyPressed == pygame.K_1 or keyPressed == pygame.K_KP1) and self.current_season != Season.WINTER:
            self.current_season = Season.WINTER
        elif (keyPressed == pygame.K_2 or keyPressed == pygame.K_KP2) and self.current_season != Season.SPRING:
            self.current_season = Season.SPRING
        elif (keyPressed == pygame.K_3 or keyPressed == pygame.K_KP3) and self.current_season != Season.SUMMER:
            self.current_season = Season.SUMMER
        elif (keyPressed == pygame.K_4 or keyPressed == pygame.K_KP4) and self.current_season != Season.AUTUMN:
            self.current_season = Season.AUTUMN
        else: self.season_counter -= 1

        if old_counter != self.season_counter:
            self.change_season(GAME_STATE)

    def change_season(self, GAME_STATE):
        GAME_STATE["saison"] = self.current_season
        GAME_STATE["active_layer"] = GAME_STATE["saison"].value
        GAME_STATE["fading"] = True
        self.music_manager.play(self.current_season.value)

    def draw(self, GAME_STATE):
        font = pygame.font.Font("data/Daydream.ttf", 24)
        GAME_STATE["screen"].blit(self.side_image, (950, -10))
        for season in Season:
            index = ["hiver","printemps","ete","automne"].index(season.value)
            self.seasons_icons.set_alpha(255 if self.current_season.value==season.value else 100)
            GAME_STATE["screen"].blit(self.seasons_icons, (1030, 100 * index + 25), ((index%2) * 52, (index//2) * 52, 50, 50))
            GAME_STATE["screen"].blit(self.keyboard_icons, (1080, 100 * index + 37), (index*26 + 118, 26, 24, 24))
        font = pygame.font.Font("data/Daydream.ttf", 12)
        textobj = font.render("Pause", True, (255, 255, 255))
        textrect = textobj.get_rect(center=(1050, 410))
        GAME_STATE["screen"].blit(textobj, textrect)
        GAME_STATE["screen"].blit(self.keyboard_icons, (1090, 397), (176*2,26*2,26,26))
        textobj = font.render("Reset", True, (255, 255, 255))
        textrect = textobj.get_rect(center=(1050, 445))
        GAME_STATE["screen"].blit(textobj, textrect)
        GAME_STATE["screen"].blit(self.keyboard_icons, (1090, 432), (98*2,26*2,26,26))
        textobj = font.render("Controls", True, (255, 255, 255))
        textrect = textobj.get_rect(center=(1068, 480))
        GAME_STATE["screen"].blit(textobj, textrect)
        GAME_STATE["screen"].blit(self.keyboard_icons, (1033, 495), (182*2,38*2,26*3,26*2))

        font = pygame.font.Font("data/Daydream.ttf", 20)
        textobj = font.render(str(self.season_counter) if self.season_counter<100 else "+99", True, (255, 255, 255) if self.season_counter!=self.optimal_count else (255, 200, 0))
        textrect = textobj.get_rect(midright=(1075, 578))
        GAME_STATE["screen"].blit(textobj, textrect)
        font = pygame.font.Font("data/Daydream.ttf", 8)
        textobj = font.render("changes made", True, (255, 255, 255))
        textrect = textobj.get_rect(center=(1070, 605))
        GAME_STATE["screen"].blit(textobj, textrect)
        textobj = font.render(f"/{self.optimal_count}", True, (255, 255, 255))
        textrect = textobj.get_rect(midright=(1090, 582))
        GAME_STATE["screen"].blit(textobj, textrect)
