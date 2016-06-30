#!/usr/bin/python
# -*- coding: UTF-8 -*-
###########################
#   AS AVENTURAS DE BEE   #
###########################
# Autores:
# Bruno Belotti
# Gabriel Sousa Kraszczuk

import pygame
import os

# Classe com as funções basicas do jogo


class Core:
    def __init__(self):
        pass

    def loadImage(self, name):
        fullname = os.path.join("../images", name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error, message:
            print "Can't load image!: ", fullname
            raise (SystemExit, message)
        return image, image.get_rect()
