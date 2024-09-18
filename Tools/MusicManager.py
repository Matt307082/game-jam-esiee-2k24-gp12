import pygame
import random
import os, inspect
from enum import Enum
pygame.init()

class MusicManager:
    files = dict()

    def load_files(this, *args):
        for music_name in args:
            this.files[music_name] = open(f"data/soundtrack/{music_name}.mp3")

    def play(this, music_name):
        pygame.mixer.music.load(this.files[music_name])
        pygame.mixer.music.play(-1, random.uniform(0, 300))

