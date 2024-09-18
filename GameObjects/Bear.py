import pygame
from Tools.utils import ChargeSerieSprites

class Bear:
    def __init__(self, position, spritesheet):
        self.x = position[0]
        self.y = position[1]
        self.spritesheet = spritesheet
        self.width = 800 // 9
        self.height = 534 // 5.9
        self.sleep_anim = ChargeSerieSprites(4, spritesheet, (self.width,self.height),9)
        self.slash_anim = ChargeSerieSprites(2, spritesheet, (self.width,self.height),9)
        self.current_anim = self.sleep_anim # default value
        self.animation_index = 0         
        self.animation_speed = 10
        self.frame_counter = 0

    def update(self, GAME_STATE):
        # initialize KeyPressed
        KeysPressed = GAME_STATE["keyPressed"]
        if(KeysPressed == pygame.K_SPACE):
            self.current_anim = self.slash_anim

        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.animation_index += 1
            if self.animation_index >= len(self.current_anim):
                self.animation_index = 0

    def draw(self, GAME_STATE):
        screen = GAME_STATE["screen"]
        if(self.current_anim == self.sleep_anim):
            screen.blit(self.current_anim[7],(self.x,self.y))
        else:
            screen.blit(self.current_anim[self.animation_index],(self.x,self.y))