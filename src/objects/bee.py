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


class Bee(pygame.sprite.Sprite):
    life_points = 1
    def __init__(self, position, buttonName):
        # Inicia os objetos
        pygame.sprite.Sprite.__init__(self)
        core = Core()

        # Insere as imagens
        self.image, self.rect = core.loadImage(buttonName)

        # Define a posicao do botao
        self.rect.centerx = position[0]
        self.rect.centery = position[1]

    def incrementLife(self, quantity):
	life_points = life_points + quantity
   
    def decrementLife(self, quantity):
        life_points = life_points - quantity
   
