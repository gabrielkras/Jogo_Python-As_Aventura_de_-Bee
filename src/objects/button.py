#!/usr/bin/python
# -*- coding: UTF-8 -*-
###########################
#   AS AVENTURAS DE BEE   #
###########################
# Autores:
# Bruno Belotti
# Gabriel Sousa Kraszczuk
import pygame
from core import Core


class Button(pygame.sprite.Sprite):

    def __init__(self, position, buttonName):
        # Inicia os objetos
        pygame.sprite.Sprite.__init__(self)
        core = Core()

        # Insere as imagens
        self.image, self.rect = core.loadImage(buttonName)

        # Define a posicao do botao
        self.rect.centerx = position[0]
        self.rect.centery = position[1]

    def checkEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
