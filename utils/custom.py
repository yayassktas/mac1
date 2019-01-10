#! /usr/bin/env python3
# coding: utf-8


class Custom:

    def __init__(self, img, level):
        self.img = pygame.image.load(img).convert_alpha()
        """ Character position in boxes and pixels """
        self.case_x = 0
        self.case_y = 0

        """ Default direction """
        self.direction = self.img
        """ Level in which the character is located """
        self.level = level
