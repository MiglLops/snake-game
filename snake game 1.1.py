import pygame, random #tutorial do canal hashtag :D // Versao 1.1 // 27/01/2025

#configuracoes iniciais

pygame.init() # inicia o pygame
pygame.display.set_caption("Jogo da cobrinha em Python") #nome da janela
largura, altura = 600, 400 #tamanho da janela
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

#cores RGB
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 20, 20)
azul = (30, 20, 255)
verde = (0, 255, 0)
verde1 = (165, 244, 51)
verde2 = (143, 212, 0)

#Confg da snake
quadrado = 20 #altura e largura em pixel
velocidade = 15 #velocidade do jogo

def gerar_comida():

    comida_x = round(random.randrange(0, largura - quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - quadrado) / 20.0) * 20.0
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.circle(tela, vermelho, (comida_x + tamanho // 2, comida_y + tamanho // 2), tamanho // 2)

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, azul, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Times New Roman", 25)
    texto = fonte.render(f"Pontos: {pontuacao}", True, preto)
    tela.blit(texto, [1, 1])


def desenhar_chao_xadrez():
    for linha in range(0, altura, quadrado):  
        for coluna in range(0, largura, quadrado): 
            cor = verde1 if (linha // quadrado + coluna // quadrado) % 2 == 0 else verde2
            pygame.draw.rect(tela, cor, (coluna, linha, quadrado, quadrado))

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0 
        velocidade_y = quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0 
        velocidade_y = - quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = - quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y

def rodar_jogo():

    fim_jogo = False
    x, y = largura/2, altura/2
    velocidade_x, velocidade_y = 0, 0

    tamanho_cobra = 1
    pixels = []
    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

        desenhar_chao_xadrez()
        #desenho da comida
        desenhar_comida(quadrado, comida_x, comida_y) 

        if x < 0 or x >= largura:
            fim_jogo = True
        if y < 0 or y >= altura:
            fim_jogo = True

        #atualizar posicao
        x += velocidade_x
        y += velocidade_y

        #desenho da cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        #se a cobra bater no proprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True

        desenhar_cobra(quadrado, pixels)
        desenhar_pontuacao(tamanho_cobra - 1)

        #atualizacao da tela
        pygame.display.update()

        #criar nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()
    
        relogio.tick(velocidade)
        
rodar_jogo()

