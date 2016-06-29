import pygame

pygame.init()

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Jogo Teste')
clock = pygame.time.Clock()


def abelhaMov(x_abelha, y_abelha):
    tela.blit(imgAbelhaDireita, (x_abelha, y_abelha))
x_abelha = (800*0.45)
y_abelha = (600*0.8)

mov_x = 0
mov_y = 0

imgAbelhaDireita = pygame.image.load('abelha_bee_direita.png')
imgAbelhaEsquerda = pygame.image.load('abelha_bee_esquerda.png')
morta = False

while not morta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            morta = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                mov_x = 5
            if event.key == pygame.K_LEFT:
                mov_x = -5
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
    tela.fill(BRANCO)
    abelhaMov(x_abelha, y_abelha)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
