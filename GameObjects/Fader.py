import pygame

class Fader:

    def __init__(self):
        self.fading = None
        self.alpha = 0
        sr = pygame.display.get_surface().get_rect()
        self.veil = pygame.Surface(sr.size)
        self.veil.fill((0, 0, 0))

    def draw(self, GAME_STATE):
        screen = GAME_STATE["screen"]
        if self.fading:
            self.veil.set_alpha(self.alpha)
            screen.blit(self.veil, (0, 0))

    def update(self, GAME_STATE):
        if(GAME_STATE["fading"]):
            self.fading = 'OUT'
        
        GAME_STATE["fading"] = False
        if self.fading == 'OUT':
            self.alpha += 8
            if self.alpha >= 255:
                self.fading = 'IN'
        else:
            self.alpha -= 8
            if self.alpha <= 0:
                self.fading = None