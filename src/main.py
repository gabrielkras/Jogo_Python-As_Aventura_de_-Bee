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
from objects.zangao import Zangao

# Inicializando screen
pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
black = 0, 0, 0
white = 255, 255, 255

# Variaveis Globais
button_start = None
button_exit = None
button_stats = None


def main():  # Inicializando Jogo
    pygame.display.set_caption("As Aventuras de Bee - v1.0")
    startMenu()
    # game()


def startMenu():  # Definindo os botoes nas variaveis globais
    scenario = Scenario([200, 200], "paisagem_fundo.jpg")
    button_start = Button([400, 300], "button_start_game_normal_01.png")
    button_stats = Button([400, 400], "button_stats_game_normal_01.png")
    button_exit = Button([400, 500], "button_exit_game_normal_01.png")
    logo = Logo([400, 100], "logo_jogo.png")
    screen.blit(scenario.image, scenario.rect)
    screen.blit(button_start.image, button_start.rect)
    screen.blit(button_stats.image, button_stats.rect)
    screen.blit(button_exit.image, button_exit.rect)
    screen.blit(logo.image, logo.rect)
    pygame.display.update()
    aux = True
    while aux:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.rect.collidepoint(pygame.mouse.get_pos()):
                    aux = False
                    game()


def enemy(mov_imagem, x_zangao, y_zangao):
    screen.blit(mov_imagem.image, (x_zangao, y_zangao))


def beeMove(mov_imagem, x_abelha, y_abelha, scenario):
    screen.blit(scenario.image, scenario.rect)
    screen.blit(mov_imagem.image, (x_abelha, y_abelha))


def game():
    x_abelha = (400)
    y_abelha = (400)
    x_zangao = (0)
    y_zangao = (0)
    mov_x = 0
    mov_y = 0
    _abelha = (800*0.45)
    _abelha = (600*0.8)
    bee_right = Bee([64, 54], "abelha_bee_direita.png")
    bee_right.rect.center = (x_abelha,y_abelha)
    bee_left = Bee([64, 54], "abelha_bee_esquerda.png")
    bee_left.rect.center = (x_abelha,y_abelha)
    zangao_left = Zangao([80, 84], "zangao_esquerda.png")
    zangao_left.rect.center = (x_zangao,y_zangao)
    zangao_right = Zangao([80, 84], "zangao_direita.png")
    zangao_right.rect.center = (x_zangao,y_zangao)
    mov_imagem = bee_right
    morta = False
    scenario = Scenario([200, 200], "paisagem_fundo.jpg")
    while not morta:
        if x_zangao >= x_abelha:
            x_zangao = x_zangao - 1
            mov_zangao = zangao_left
        if y_zangao >= y_abelha:
            y_zangao = y_zangao - 1
        if x_zangao <= x_abelha:
            x_zangao = x_zangao + 1
            mov_zangao = zangao_right
        if y_zangao <= y_abelha:
            y_zangao = y_zangao + 1

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

        if bee_right.rect.colliderect(zangao_right.rect):
            morta = True
        if bee_left.rect.colliderect(zangao_left.rect):
            morta = True

        if (x_abelha + mov_x + 64) > 800 or (x_abelha + mov_x) < 0:
            mov_x = 0
        else:
            x_abelha += mov_x

        if (y_abelha + mov_y + 54) > 600 or (y_abelha + mov_y) < 0:
            mov_y = 0
        else:
            y_abelha += mov_y

        bee_right.rect.center = (x_abelha,y_abelha)
	bee_left.rect.center = (x_abelha,y_abelha)
	zangao_right.rect.center = (x_zangao,y_zangao)
        zangao_left.rect.center = (x_zangao,y_zangao)
        beeMove(mov_imagem, x_abelha, y_abelha, scenario)
        enemy(mov_zangao, x_zangao, y_zangao)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()

pygame.quit()
quit()
