#! /usr/bin/env python3
# coding: utf-8
import pygame


class Guardian:

    def __init__(self, img, level):

        self.img = pygame.image.load(img).convert_alpha()
        """ Character position in boxes and pixels """

        self.x = 269
        self.y = 195
        """ Default direction """
        self.direction = self.img
        """ Level in which the character is located """
        self.level = level
