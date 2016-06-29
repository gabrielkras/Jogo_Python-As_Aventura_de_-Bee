#!/usr/bin/python
# -*- coding: UTF-8 -*-
###########################
#   AS AVENTURAS DE BEE   #
###########################
# Autores: 
# Bruno Belotti
# Gabriel Sousa Kraszczuk
import pygame
import sys
from core import Core

class Button(pygame.sprite.Sprite):
	def __init__(self,position,buttonName):
		# Inicia os objetos
		pygame.sprite.Sprite.__init__(self)
		core = Core()

		# Insere as imagens
		self.image, self.rect = core.loadImage(buttonName)
		
		#define a posicao do botao
		self.rect.centerx = position[0]
		self.rect.centery = position[1]
		
	
#	def checkEvent(self):
#		for event in pygame.mouse.get_pressed():
#			if event[0] == TRUE:
#				print("CLIQUEI COM O MOUSE")		


