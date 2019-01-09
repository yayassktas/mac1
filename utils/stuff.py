#! /usr/bin/env python3
# coding: utf-8
import random
from utils.maze import *


class Stuff:
    case_x = 0
    case_y = 0

    def __init__(self, img, level):
        # Sprites of the character
        self.img = pygame.image.load(img).convert_alpha()
        # Character position in boxes and pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0

        # Default direction
        self.direction = self.img
        # Level in which the character is located
        self.level = level

    def randomize_position(self):
        self.x = random.randint(0, 14)
        self.y = random.randint(0, 14)
        if self.level[self.x][self.y] == 'm':
            self.randomize_position()

