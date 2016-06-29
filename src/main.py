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
from objects.logo import Logo
from objects.bee import Bee
from objects.scenario import Scenario

#Inicializando screen
pygame.init()
size = width, height = 800, 600 
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
black = 0, 0, 0
white = 255, 255, 255

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
	scenario = Scenario([200,200],"paisagem_fundo.jpg")
	button_start = Button([400,300],"button_start_game_normal_01.png")
	button_stats = Button([400,400],"button_stats_game_normal_01.png")
	button_exit  = Button([400,500],"button_exit_game_normal_01.png")
	logo = Logo([400,100],"logo_jogo.png")
	screen.blit(scenario.image,scenario.rect)
        screen.blit(button_start.image, button_start.rect)
	screen.blit(button_stats.image, button_stats.rect)
        screen.blit(button_exit.image, button_exit.rect)
	screen.blit(logo.image, logo.rect)
	pygame.display.flip()
	menu = True
	while menu:
		if button_start.checkEvent() == True:
			menu = False
			game()
#		if button_exit.checkEvent() == True:
#			menu = False
#			pygame.quit()
#			quit()
		

def beeMove(mov_imagem, x_abelha, y_abelha, scenario):
	screen.blit(scenario.image, scenario.rect)
	screen.blit(mov_imagem, (x_abelha, y_abelha))

def game():
	x_abelha = (800*0.45)
	y_abelha = (600*0.8)
	mov_x = 0
	mov_y = 0
	_abelha = (800*0.45)
	_abelha = (600*0.8)
	bee_right = Bee([400,200],"abelha_bee_direita.png").image
	bee_left = Bee([400,200],"abelha_bee_esquerda.png").image
	mov_imagem = bee_right
	morta = False
	clock = pygame.time.Clock()
	scenario = Scenario([200,200],"paisagem_fundo.jpg")
	while not morta:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
        	    morta = True
	        if event.type == pygame.KEYDOWN:
	            if event.key == pygame.K_RIGHT:
        	        mov_x = 5
	               	mov_imagem = bee_right
        	    if event.key == pygame.K_LEFT:
                	mov_x = -5
	                mov_imagem = bee_left
        	    if event.key == pygame.K_DOWN:
	                mov_y = 5
	            if event.key == pygame.K_UP:
	                mov_y = -5

	        if event.type == pygame.KEYUP:
        	    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                	mov_x = 0
	            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
	                mov_y = 0

	    x_abelha += mov_x
	    y_abelha += mov_y
	    beeMove(mov_imagem, x_abelha, y_abelha, scenario)
	    pygame.display.update()
	    screen.fill(white)
	    clock.tick(300)


if __name__ == "__main__":
    main()

pygame.quit()
quit()
