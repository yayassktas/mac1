#! /usr/bin/env python3
# coding: utf-8

import pygame
from utils.custom import *
from utils.constantes import *


class Mac(Custom):

    def __init__(self, img, level):

        self.img = pygame.image.load(img).convert_alpha()

        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.direction = self.img
        self.level = level

    def goright(self):
        if self.case_x < (number_sprite_side - 1):
            if self.level.structure[self.case_y][self.case_x + 1] != 'm':
                self.case_x += 1
                self.x = self.case_x * size_sprite

    def goleft(self):
        if self.case_x > 0:
            if self.level.structure[self.case_y][self.case_x - 1] != 'm':
                self.case_x -= 1
                self.x = self.case_x * size_sprite

    def go_up(self):
        if self.case_y > 0:
            if self.level.structure[self.case_y - 1][self.case_x] != 'm':
                self.case_y -= 1
                self.y = self.case_y * size_sprite

    def go_down(self):
        if self.case_y < (number_sprite_side - 1):
            if self.level.structure[self.case_y + 1][self.case_x] != 'm':
                self.case_y += 1
                self.y = self.case_y * size_sprite

    def move(self, direction):
        # Method for moving the character

        if direction == 'right':
            self.goright()

        elif direction == 'left':
            self.goleft()

        elif direction == 'up':
            self.go_up()

        elif direction == 'down':
            self.go_down()
