#! /usr/bin/env python3
# coding: utf-8
import random
from utils.maze import *


class Stuff:

    def __init__(self, img, level):
        """ Sprites of the character """
        self.img = pygame.image.load(img).convert_alpha()
        """ Character position in boxes and pixels """

        self.x = 0
        self.y = 0

        """ Default direction """
        self.direction = self.img
        """ Level in which the character is located """
        self.level = level
        """ random function """
    def randomize_position(self):
        self.x = random.randint(0, 14)
        self.y = random.randint(0, 14)
        if self.level[self.x][self.y] == 'm' or self.level[self.x][self.y] == 's' or self.level[self.x][self.y] == 'd' \
                or self.level[self.x][self.y] == 'g' or self.level[self.x][self.y] == 'a':
            self.randomize_position()
