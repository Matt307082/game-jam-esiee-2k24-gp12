import pygame
from Tools.utils import ChargeSerieSprites, Season
from math import sqrt

class Bear:
    def __init__(self, position, spritesheet):
        self.x = position[0]
        self.y = position[1]
        self.spritesheet = spritesheet
        self.width = 950 // 9
        self.height = 534 // 5.8
        self.sleep_anim = ChargeSerieSprites(4, spritesheet, (self.width,self.height),9)
        self.slash_anim = ChargeSerieSprites(2, spritesheet, (self.width,self.height),9)
        self.current_anim = self.sleep_anim # default value
        self.animation_started = False
        self.animation_index = 0         
        self.animation_speed = 10
        self.frame_counter = 0

    def update(self, GAME_STATE):
        if(GAME_STATE["saison"] != Season.WINTER):
            player = GAME_STATE["player"]
            if (sqrt((self.x+self.width//2 - (player.x+player.cell_width//2))**2 + (self.y+self.height//2 - (player.y+player.cell_height//2))**2) <= 50):
                self.current_anim = self.slash_anim
                self.animation_started = True

            if(self.animation_started):
                self.frame_counter += 1
                if self.frame_counter >= self.animation_speed:
                    self.frame_counter = 0
                    self.animation_index += 1
                    if self.animation_index >= len(self.current_anim)/2:
                        player.reset(GAME_STATE)
                    if self.animation_index >= len(self.current_anim):
                        self.animation_index = 0
                        self.current_anim = self.sleep_anim
                        self.animation_started = False

    def draw(self, GAME_STATE):
        if(GAME_STATE["saison"] != Season.WINTER):
            screen = GAME_STATE["screen"]
            if(self.current_anim == self.sleep_anim):
                screen.blit(pygame.transform.scale(self.current_anim[7],(50,64)),(self.x,self.y))
            else:
                screen.blit(pygame.transform.scale(self.current_anim[self.animation_index], (50,64)),(self.x,self.y))