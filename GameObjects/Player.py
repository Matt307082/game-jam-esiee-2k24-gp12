import pygame
from Tools.utils import ChargeSerieSprites, WINDOW_SIZE

class Player:
    def __init__(self, position, spritesheet):
        self.x = position[0]
        self.y = position[1]
        self.vx = 1
        self.vy = 1
        self.spritesheet = spritesheet
        self.width = 200 // 4
        self.height = 261 // 4
        self.down_anim = ChargeSerieSprites(0, spritesheet, (self.width,self.height),4)
        self.right_anim = ChargeSerieSprites(1, spritesheet, (self.width,self.height),4)
        self.left_anim = ChargeSerieSprites(2, spritesheet, (self.width,self.height),4)
        self.up_anim = ChargeSerieSprites(3, spritesheet, (self.width,self.height),4)
        self.current_anim = self.down_anim # default value
        self.animation_index = 0         
        self.animation_speed = 10
        self.frame_counter = 0

    def update(self, GAME_STATE):
        # initialize KeyPressed
        KeysPressed = GAME_STATE["keyPressed"]
        if(KeysPressed == pygame.K_DOWN and self.y<WINDOW_SIZE[1]-self.height):
            self.current_anim = self.down_anim
            self.y += self.vy
        elif(KeysPressed == pygame.K_UP and self.y>0):
            self.current_anim = self.up_anim
            self.y -= self.vy
        elif(KeysPressed == pygame.K_LEFT and self.x>0):
            self.current_anim = self.left_anim
            self.x -= self.vx
        elif(KeysPressed == pygame.K_RIGHT and self.x<WINDOW_SIZE[0]-self.width):
            self.current_anim = self.right_anim
            self.x += self.vx

        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.animation_index += 1
            if self.animation_index >= len(self.current_anim):
                self.animation_index = 0

    def draw(self, GAME_STATE):
        screen = GAME_STATE["screen"]
        screen.blit(self.current_anim[self.animation_index],(self.x,self.y))

    