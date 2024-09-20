import pygame

class Fader:

    def __init__(self):
        self.alpha = 0
        sr = pygame.display.get_surface().get_rect()
        sr.width-=178
        self.veil = pygame.Surface(sr.size)
        self.veil.fill((0, 0, 0))
        self.isFading = False

    def draw(self, GAME_STATE):
        screen = GAME_STATE["screen"]
        if self.isFading:
            self.veil.set_alpha(self.alpha)
            screen.blit(self.veil, (0, 0))

    def update(self, GAME_STATE):
        if(GAME_STATE["fading"]):
            print("START FADING")
            self.alpha = 255
            print(self.alpha)
            GAME_STATE["fading"] = False
            self.isFading = True
        
        if self.isFading :
            print("IM FADING")
            print(self.alpha)
            self.alpha -= 10
            if self.alpha <= 0:
                self.alpha = 0
                self.isFading = False