import pygame
from Tools.utils import ChargeSerieSprites
from math import sqrt

class Fog:
    def __init__(self, position, size):
        self.x = position[0]
        self.y = position[1]
        self.width = size[0]
        self.height = size[1]

    def update(self, GAME_STATE):
        return

    def draw(self, GAME_STATE):
        if (GAME_STATE["active_layer"] == "hiver"):
            pygame.draw.rect(GAME_STATE["screen"], (230, 230, 230), pygame.Rect(self.x, self.y, self.width, self.height))