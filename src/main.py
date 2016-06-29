#!/usr/bin/python
# -*- coding: UTF-8 -*-
###########################
#   AS AVENTURAS DE BEE   #
###########################
# Autores: 
# Bruno Belotti
# Gabriel Sousa Kraszczuk

import pygame
from objects.button import Button

#Inicializando screen
pygame.init()
size = width, height = 800, 600 
screen = pygame.display.set_mode(size)
black = 0, 0, 0

#Variaveis Globais
button_start = None
button_exit  = None
button_stats = None

#Inicializando Jogo
def main():
	pygame.display.set_caption("As Aventuras de Bee - v1.0")
	startMenu()

# Definindo os botoes nas variaveis globais
def startMenu():
	button_start = Button([400,300],"button_start_game_normal_01.png")
	button_stats = Button([400,400],"button_stats_game_normal_01.png")
	button_exit  = Button([400,500],"button_exit_game_normal_01.png")
	while 1:
		screen.fill(black)
        	screen.blit(button_start.image, button_start.rect)
		screen.blit(button_stats.image, button_stats.rect)
        	screen.blit(button_exit.image, button_exit.rect)
		pygame.display.flip()
#		button_start.checkEvent()
#		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#			if bstart.collidepoint(pos):
#				print("SHOW BOTAO START")


if __name__ == "__main__":
    main()
