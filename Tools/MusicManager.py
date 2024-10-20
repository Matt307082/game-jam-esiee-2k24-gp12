import pygame
import random
import os, inspect
from enum import Enum
pygame.init()

class MusicManager:
    files = dict()

    def load_files(self, *args):
        for music_name in args:
            self.files[music_name] = open(f"data/soundtrack/{music_name}.mp3")

    def play(self, music_name):
        pygame.mixer.music.unload()
        pygame.mixer.music.load(self.files[music_name])
        pygame.mixer.music.play(-1, random.uniform(0, 300))
        self.load_files(music_name)

    def use_effect(self, effect_name, volume = 1):
        sound = pygame.mixer.Sound(self.files[effect_name])
        sound.set_volume(volume)
        sound.play()
        self.load_files(effect_name)