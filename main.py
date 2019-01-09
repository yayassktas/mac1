#!/usr/bin/python3
# -*- coding: Utf-8 -*
from utils.macg import *
from utils.stuff import *
from pygame.locals import *
from utils.maze import *

pygame.init()

# Opening the Pygame window (square: width = height)
window = pygame.display.set_mode((side_window, side_window))
# Icone
icon = pygame.image.load(picture_icon)
pygame.display.set_icon(icon)
# Title
pygame.display.set_caption(title_window)

# background loading
background = pygame.image.load(picture_background).convert()

# Generating a level from a file
level = Level('utils/n1')
level.genererate()
level.screen(window)

# creates objets
macgyver = mac("utils/ressources/mac.png", level)
stuff2 = Stuff("utils/ressources/tube.png", level.structure)
stuff2.randomize_position()
level.structure[stuff2.y][stuff2.x] = 's'
stuff3 = Stuff("utils/ressources/syringe.png", level.structure)
stuff3.randomize_position()
level.structure[stuff3.y][stuff3.x] = 's'
stuff4 = Stuff("utils/ressources/ether.png", level.structure)
stuff4.randomize_position()
level.structure[stuff4.y][stuff4.x] = 's'

win = pygame.image.load("utils/ressources/winner.png").convert_alpha()
loose = pygame.image.load("utils/ressources/looser.png").convert_alpha()
over2 = False
over1 = False
over = False
continu = 1
continu_game = 1
count = 0


def end():
    global continu_game

    if level.structure[macgyver.case_y][macgyver.case_x] == 'a' and count == 3:
        window.blit(win, (100, 100))
        pygame.display.flip()
        continu_game = 0

    if level.structure[macgyver.case_y][macgyver.case_x] == 'g' and count != 3:
        window.blit(loose, (100, 100))
        pygame.display.flip()
        continu_game = 0


def artefact():
    global over
    global over1
    global over2
    global count

    if stuff2.y * size_sprite == macgyver.x and stuff2.x * size_sprite == macgyver.y and not over:
        over = True
        count = count + 1
    if not over:
        window.blit(stuff2.direction, (stuff2.y * size_sprite, stuff2.x * size_sprite))

    if stuff3.y * size_sprite == macgyver.x and stuff3.x * size_sprite == macgyver.y and not over1:
        over1 = True
        count = count + 1
    if not over1:
        window.blit(stuff3.direction, (stuff3.y * size_sprite, stuff3.x * size_sprite))

    if stuff4.y * size_sprite == macgyver.x and stuff4.x * size_sprite == macgyver.y and not over2:
        over2 = True
        count = count + 1
    if not over2:
        window.blit(stuff4.direction, (stuff4.y * size_sprite, stuff4.x * size_sprite))

    window.blit(macgyver.direction, (macgyver.x, macgyver.y))
    pygame.display.flip()


# game loop
while continu_game:
    for event in pygame.event.get():

        if event.type == QUIT:
            continu_game = 0
            continu = 0

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                continu_game = 0

            # movement key
            elif event.key == K_RIGHT:
                macgyver.move('right')
            elif event.key == K_LEFT:
                macgyver.move('left')
            elif event.key == K_UP:
                macgyver.move('up')
            elif event.key == K_DOWN:
                macgyver.move('down')

        # Displays at new positions
        window.blit(background, (0, 0))
        level.screen(window)
        artefact()
        end()