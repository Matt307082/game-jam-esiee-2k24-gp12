import pygame
import random
import os, inspect
from enum import Enum
pygame.init()

class MusicManager:
    files = dict()
    current_music = ""

    def load_files(self, *args):
        for music_name in args:
            self.files[music_name] = open(f"data/soundtrack/{music_name}.mp3")

    def play(self, music_name):
        if music_name in self.files and self.current_music != music_name:
            self.current_music = music_name;
            pygame.mixer.music.load(self.files[music_name])
            pygame.mixer.music.play(-1, random.uniform(0, 300))

