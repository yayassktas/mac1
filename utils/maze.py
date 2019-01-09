#! /usr/bin/env python3
# coding: utf-8
import pygame
from utils.constantes import *

pygame.init()


class Level:  # generate level

    def __init__(self, file):
        self.file = file
        self.structure = 0

    def genererate(self):
        """Method for generating the level based on the file.
         We create a general list, containing a list per line to display"""

        with open(self.file, "r") as file:
            structure_level = []

            for line in file:
                line_level = []
                # On browses the sprites (letters) contained in the file
                for sprite in line:
                    # We ignore the end of line "\ n"
                    if sprite != '\n':
                        # We add the sprite to the list of the line
                        line_level.append(sprite)
                # Add the line to the level list
                structure_level.append(line_level)
            # We safeguard this structure
            self.structure = structure_level

    def screen(self, window):

        wall = pygame.image.load(picture_wall).convert()
        start = pygame.image.load(picture_start).convert()
        come = pygame.image.load(picture_come).convert_alpha()
        guardian = pygame.image.load(gardian).convert_alpha()

        # We go through the list of level
        num_line = 0
        for line in self.structure:
            # We go through the lists of lines
            num_case = 0
            for sprite in line:
                # The actual position in pixels is calculated
                x = num_case * size_sprite
                y = num_line * size_sprite
                if sprite == 'm':  # m = Mur
                    window.blit(wall, (x, y))
                elif sprite == 'd':  # d = Départ
                    window.blit(start, (x, y))
                elif sprite == 'g':
                    window.blit(guardian, (x, y))
                elif sprite == 'a':  # a = Arrivée
                    window.blit(come, (x, y))

                num_case += 1
            num_line += 1
