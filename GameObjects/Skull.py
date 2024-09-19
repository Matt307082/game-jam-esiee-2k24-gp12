import pygame

class Skull :

    def __init__(self,position,sprite) :
        self.x = position[0]
        self.y = position[1]
        self.countdown = 50
        self.sprite = sprite

    def update(self, GAME_STATE):
        if self.countdown > 0 :
            self.countdown -=1
            self.y -= 0.1
            self.sprite.set_alpha(self.countdown * 5)
        else :
            GAME_STATE["gameObject"].remove(self)

    def draw(self, GAME_STATE):
        GAME_STATE["screen"].blit(pygame.transform.scale(self.sprite,(25,32)),(self.x,self.y))