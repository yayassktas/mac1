#! /usr/bin/env python3
# coding: utf-8
from utils.custom import *


class guardian(Custom):

    case_x = 0
    case_y = 0

    def __init__(self, img, level):

        self.img = pygame.image.load(img).convert_alpha()
        # Character position in boxes and pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 269
        self.y = 200
        # Default direction
        self.direction = self.img
        # Level in which the character is located
        self.level = level
