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
from objects.life import Life
from objects.mana import Mana
from objects.ferrao import Ferrao
from objects.honey import Honey
from random import randint

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
font = pygame.font.SysFont("monospace", 15, True)
fontData = pygame.font.SysFont("monospace", 36, True)
fontHits = pygame.font.SysFont("monospace", 20, True)

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

def atack(mov_imagem, x_ferrao, y_ferrao):
    screen.blit(mov_imagem.image, (x_ferrao, y_ferrao))


def beeMove(mov_imagem, x_abelha, y_abelha, scenario):
    screen.blit(scenario.image, scenario.rect)
    screen.blit(mov_imagem.image, (x_abelha, y_abelha))


def game():
    x_abelha = (400)
    y_abelha = (400)
    x_zangao = (randint(0,800))
    y_zangao = (randint(0,600))
    x_ferrao = x_abelha
    y_ferrao = y_abelha
    x_pote   = randint(30,699)
    y_pote   = 0
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
    vida = Life([44,69], "vida.png")
    mana = Mana([44,174], "mana.png")
    ferrao_left = Ferrao([800, 600], "ferrao_2.png")
    ferrao_right = Ferrao([800, 600], "ferrao_1.png")
    poteMel = Honey([randint(30,699),0],"pote_mel.png")
    tituloVida = font.render("Vida", 2, white)
    tituloMana = font.render("Mana", 2, white)
    quantidadeVida = fontData.render(str(bee_left.life_points),2,(178,034,034))
    quantidadeMana = fontData.render(str(bee_left.mana_points),2,(000,000,205))
    pygame.display.update()
    mov_imagem = bee_right
    morta = False
    atacking = None
    zangao = True
    pote_mel = False
    mana_ciclos = 0
    hits_ciclos = 0
    hits_zangao_ciclo = 0
    velocidade_zangao = 1
    velocidade_bee = 5
    pote_mel_ciclo_presente = randint(0,1000)
    pote_mel_ciclos = 0
    scenario = Scenario([200, 200], "paisagem_fundo.jpg")
    while not morta:
        quantidadeVida = fontData.render(str(bee_left.life_points),2,(178,034,034))
        quantidadeMana = fontData.render(str(bee_left.mana_points),2,(000,000,205))
	zangao_hits = fontHits.render("HITS "+str(hits_zangao_ciclo),2,(218,165,32))
	zangao_life = fontHits.render("VIDA "+str(zangao_left.life_points),2,(178,034,034))
        bee_hits = fontHits.render("HITS "+str(hits_ciclos),2,(218,165,32))
        if x_zangao >= x_abelha:
            x_zangao = x_zangao - velocidade_zangao
            mov_zangao = zangao_left
        if y_zangao >= y_abelha:
            y_zangao = y_zangao - velocidade_zangao
        if x_zangao <= x_abelha:
            x_zangao = x_zangao + velocidade_zangao
            mov_zangao = zangao_right
        if y_zangao <= y_abelha:
            y_zangao = y_zangao + velocidade_zangao

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                morta = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    mov_x = velocidade_bee
                    mov_imagem = bee_right
                if event.key == pygame.K_LEFT:
                    mov_x = velocidade_bee * (-1)
                    mov_imagem = bee_left
                if event.key == pygame.K_DOWN:
                    mov_y = velocidade_bee
                if event.key == pygame.K_UP:
                    mov_y = velocidade_bee * (-1)
                if event.key == pygame.K_SPACE:
		    if bee_left.mana_points >= ferrao_left.mana_cust:
                        x_ferrao = x_abelha
                        y_ferrao = y_abelha
                    	if mov_imagem == bee_right:
                              atack(ferrao_left, x_ferrao, y_abelha)
                              atacking = "left"
                              bee_left.decrementMana(ferrao_left.mana_cust)
                    	if mov_imagem == bee_left:
			      atack(ferrao_right, x_ferrao, y_abelha)
                              atacking = "right"
                              bee_left.decrementMana(ferrao_right.mana_cust)


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    mov_x = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    mov_y = 0

        if bee_right.rect.colliderect(zangao_right.rect):
	        if zangao == True:
                    hits_ciclos = hits_ciclos + 1
        if bee_left.rect.colliderect(zangao_left.rect):
                if zangao == True:
                    hits_ciclos = hits_ciclos + 1
        if ferrao_left.rect.colliderect(zangao_left.rect):
		hits_zangao_ciclo = hits_zangao_ciclo + ferrao_left.hits
	if ferrao_right.rect.colliderect(zangao_right.rect):
		hits_zangao_ciclo = hits_zangao_ciclo + ferrao_left.hits
        if bee_left.rect.colliderect(poteMel.rect):
	        bee_left.incrementMana(5)
                velocidade_bee = velocidade_bee + 1
                bee_left.incrementLife(1)
                pote_mel_ciclos = 0
                pote_mel_ciclos_presente = randint(0,5000)
 		pote_mel = False
                x_pote = randint(30,699)
                y_pote = 0
        if bee_right.rect.colliderect(poteMel.rect):
	        bee_left.incrementMana(5)
                velocidade_bee = velocidade_bee + 1
                bee_left.incrementLife(1)
                pote_mel_ciclos = 0
                pote_mel_ciclos_presente = randint(0,5000)
 		pote_mel = False
                x_pote = randint(30,699)
                y_pote = 0




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
        ferrao_left.rect.center = (x_ferrao,y_ferrao)
        ferrao_right.rect.center = (x_ferrao,y_ferrao)
        poteMel.rect.center = (x_pote,y_pote)
        beeMove(mov_imagem, x_abelha, y_abelha, scenario)
        if zangao == True:
	       enemy(mov_zangao, x_zangao, y_zangao)
	screen.blit(tituloVida, (25,10))
        screen.blit(quantidadeVida, (80,59))
	screen.blit(quantidadeMana, (80,164))
        screen.blit(tituloMana, (25,115))
	screen.blit(vida.image, vida.rect)
        screen.blit(mana.image, mana.rect)
        if atacking == "right":
             x_ferrao = x_ferrao + 7
             atack(ferrao_right, x_ferrao , y_ferrao)
        if atacking == "left":
             x_ferrao = x_ferrao - 7
             atack(ferrao_left, x_ferrao, y_ferrao)
        if x_ferrao >= 800 or x_ferrao <= 0:
             atacking = None
             x_ferrao = x_abelha
             y_ferrao = y_abelha
        mana_ciclos = mana_ciclos + 1
        pote_mel_ciclos = pote_mel_ciclos + 1
        if pote_mel_ciclos >= pote_mel_ciclo_presente:
             pote_mel = True
        if mana_ciclos >= 100:
             bee_left.incrementMana(1)
	     mana_ciclos = 0
        if hits_ciclos >= 100:
             bee_left.decrementLife(1)
             zangao_left.incrementLife(1)
             hits_ciclos = 0
        if hits_zangao_ciclo >= 1000:
	     zangao_left.decrementLife(1)
             velocidade_zangao = velocidade_zangao + 1
             hits_zangao_ciclo = 0
        if bee_left.life_points <= 0:
	     morta = True
        if zangao_left.life_points <= 0:
             zangao = False
	     hits_zangao_ciclo = 0
        if hits_zangao_ciclo > 0:
	    screen.blit(zangao_hits, (x_zangao, y_zangao - 20))
	    screen.blit(zangao_life, (x_zangao, y_zangao + 90))
        if hits_ciclos > 0:
	    screen.blit(bee_hits, (x_abelha, y_abelha - 20))
        if pote_mel == True:
            y_pote = y_pote + 5
            screen.blit(poteMel.image, (x_pote,y_pote))
	if y_pote >= 600:
	    pote_mel = False,
	    y_pote = 0
            x_pote = randint(30,699)
            pote_mel_ciclos = 0
            pote_mel_ciclos_presente = randint(0,5000)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()

pygame.quit()
quit()
