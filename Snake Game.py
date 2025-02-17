import pygame, random, math #tutorial do canal hashtag :D // Versao 1.4 // 15/02/2025 - 17/02/2025

#configuracoes iniciais

pygame.init() # inicia o pygame
pygame.display.set_caption("Jogo da cobrinha em Python") #nome da janela
relogio = pygame.time.Clock()
dificuldade2 = 0


#cores RGB
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 20, 20)
azul = (30, 20, 255)
verde = (20, 255, 150)
verde1 = (165, 244, 51)
verde2 = (143, 212, 0)

#Confg da snake
quadrado = 20 #altura e largura em pixel
velocidade = 5 #velocidade do jogo

def gerar_comida():

    comida_x = round(random.randrange(0, largura - quadrado) / quadrado) * quadrado
    comida_y = round(random.randrange(0, altura - quadrado) / quadrado) * quadrado
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    if cor_personalizada_vermelha[0] == 255:
        pygame.draw.circle(tela, cor_personalizada_vermelha, (comida_x + tamanho // 2, comida_y + tamanho // 2), tamanho // 2)
    else:
        pygame.draw.rect(tela, cor_personalizada_vermelha, [comida_x, comida_y, tamanho, tamanho])
    pygame.draw.rect(tela, verde, [comida_x, comida_y, 5, 10])
    
def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        if cor_personalizada_vermelha[0] == 255:
            pygame.draw.rect(tela, cor_personalizada_azul, [pixel[0], pixel[1], tamanho, tamanho])
        else:
            pygame.draw.circle(tela, cor_personalizada_azul, [pixel[0], pixel[1]], tamanho // 2)

def desenhar_pontuacao(pontuacao, velocidade):
    fonte = pygame.font.SysFont("Times New Roman", 25)
    texto = fonte.render(f"Pontos: {pontuacao}", True, preto)
    tela.blit(texto, [1, 1])
    texto = fonte.render(f"Vel: {velocidade}", True, preto)
    tela.blit(texto, [1, 20])

def desenhar_chao_xadrez():
    for linha in range(0, altura, quadrado):  
        for coluna in range(0, largura, quadrado): 
            cor = verde1 if (linha // quadrado + coluna // quadrado) % 2 == 0 else verde2
            pygame.draw.rect(tela, cor, (coluna, linha, quadrado, quadrado))

def game_over(pontos):
    desenhar_chao_xadrez()
    pygame.draw.rect(tela, cor_personalizada_azul2, (80, 135, 490, 50))
    fonte = pygame.font.SysFont("Times New Roman", 50)
    fonte2 = pygame.font.SysFont("Times New Roman", 20)
    texto = fonte.render(f"Game Over! Pontos: {pontos}", True, branco)
    tela.blit(texto, [80, 135])
    pygame.draw.rect(tela, cor_personalizada_azul2, (80, 240, 200, 50))
    texto = fonte.render("Reiniciar", True, branco)
    tela.blit(texto, [80, 240])
    pygame.draw.rect(tela, cor_personalizada_azul2, (440, 240, 83, 50))
    texto = fonte.render("Sair", True, branco)
    tela.blit(texto, [440, 240])
    quadrado_desenho_restart = pygame.Rect(80, 240, 200, 50)
    quadrado_sair = pygame.Rect(440, 240, 83, 50)
    rodar = True
    while rodar == True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodar = False
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if quadrado_desenho_restart.collidepoint(evento.pos):
                    rodar_jogo()
                if quadrado_sair.collidepoint(evento.pos):
                    rodar = False
        pygame.display.update()

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
    elif tecla == pygame.K_ESCAPE:
        tela_inicial()
    return velocidade_x, velocidade_y

def rodar_jogo():
    global velocidade
    fim_jogo = False
    x, y = largura / 2, altura / 2
    velocidade_x, velocidade_y = 0, 0

    tamanho_cobra = 1
    pixels = []
    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
                exit()
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)
        

        #Desenho do chao
        desenhar_chao_xadrez()
        #desenho da comida
        desenhar_comida(quadrado, comida_x, comida_y) 

        if dificuldade2 == 1 or dificuldade2 == 2 or dificuldade2 == 0:
            if x < 0:  # Se a cobra passar da parede esquerda
                x = largura - quadrado
            elif x >= largura:  # Se a cobra passar da parede direita
                x = 0 - quadrado
            if y < 0:  # Se a cobra passar da parede superior
                y = altura - quadrado
            elif y >= altura:  # Se a cobra passar da parede inferior
                y = 0 - quadrado
        else:

            if x < 0 or x >= largura or y < 0 or y >= altura:
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
        desenhar_pontuacao(tamanho_cobra - 1, velocidade)

        #atualizacao da tela
        pygame.display.update()

        #criar nova comida

        if x == comida_x and y == comida_y:
            if velocidade <= 10:
                velocidade += 1
            else:
                velocidade += 0.5
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()
    
        relogio.tick(velocidade)
    
    game_over(tamanho_cobra - 1)


def tela_inicial():
    global largura, altura, tela, cor_personalizada_azul, cor_personalizada_vermelha, cor_personalizada_azul2, velocidade
    largura = 600
    altura = 400
    tela = pygame.display.set_mode((largura, altura))
    rodando = True
    pos_circulo = 570, 30
    raio = 20
    quadrado_desenho_start = pygame.Rect(20, 300, 180, 37)
    quadrado_desenho_quit = pygame.Rect(40, 350, 190, 35)
    pos_circulo2 = 430, 130
    raio2 = 10
    pos_circulo3 = 420, 180
    pos_circulo4 = 440, 180
    pos_circulo5 = 420, 183
    pos_circulo6 = 440, 183
    raio3 = 5
    raio4 = 2
    cor_personalizada_azul = 30, 20, 255
    cor_personalizada_azul2 = 15, 0, 155
    cor_personalizada_vermelha = 255, 20, 20
    while rodando:
        desenhar_chao_xadrez()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                exit()
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x_mouse2, y_mouse2 = evento.pos
                distancia_mouse2 = math.sqrt((x_mouse2 - pos_circulo2[0]) ** 2 + (y_mouse2 - pos_circulo2[1]) ** 2)
                if distancia_mouse2 <= 20:
                    if cor_personalizada_azul[0] == 30:
                        cor_personalizada_azul2 = 200, 40, 40
                        cor_personalizada_azul = 255, 10, 20
                        cor_personalizada_vermelha = 30, 20, 255
                    elif cor_personalizada_azul[0] == 255:
                        cor_personalizada_azul2 = 15, 0, 155
                        cor_personalizada_azul = 30, 20, 255
                        cor_personalizada_vermelha = 255, 20, 20
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x_mouse, y_mouse = evento.pos
                distancia_mouse = math.sqrt((x_mouse - pos_circulo[0]) ** 2 + (y_mouse - pos_circulo[1]) ** 2)
                if distancia_mouse <= 20:
                    tela_confg()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if quadrado_desenho_start.collidepoint(evento.pos):
                     rodar_jogo()
                if quadrado_desenho_quit.collidepoint(evento.pos):
                    rodando = False

        pygame.draw.rect(tela, cor_personalizada_azul, (180, 310, 140, 20))
        pygame.draw.rect(tela, cor_personalizada_azul, (40, 320, 20, 65))
        pygame.draw.rect(tela, cor_personalizada_azul2, (20, 300, 180, 37)) #Start
        pygame.draw.rect(tela, cor_personalizada_azul2, (40, 350, 190, 35)) #Quit
        pygame.draw.rect(tela, cor_personalizada_azul, (300, 200, 120, 20))
        pygame.draw.rect(tela, cor_personalizada_azul, (300, 200 + 10, 20, 120))
        pygame.draw.rect(tela, cor_personalizada_azul, (420, 180, 20, 40))
        pygame.draw.circle(tela, cor_personalizada_vermelha, pos_circulo2, raio2)

        pygame.draw.circle(tela, branco, pos_circulo3, raio3)
        pygame.draw.circle(tela, branco, pos_circulo5, raio3)
        pygame.draw.circle(tela, preto, pos_circulo3, raio4)

        pygame.draw.circle(tela, preto, pos_circulo, raio)

        pygame.draw.circle(tela, branco, pos_circulo4, raio3)
        pygame.draw.circle(tela, branco, pos_circulo6, raio3)
        pygame.draw.circle(tela, preto, pos_circulo4, raio4)

        fonte1 = pygame.font.SysFont("Times New Roman", 40)
        texto = fonte1.render("Start", True, branco)
        tela.blit(texto, [70, 295])
        texto = fonte1.render("Quit", True, branco)
        tela.blit(texto, [100, 345])
        fonte3 = pygame.font.SysFont("Arial", 90)
        texto = fonte3.render("Snake", True, preto)  
        tela.blit(texto, [40, 20])   
        texto = fonte3.render("Game", True, preto)
        tela.blit(texto, [80, 93]) 
        fonte4 = pygame.font.SysFont("Arial", 20)
        texto = fonte4.render("By:Miguel", True, preto)   
        tela.blit(texto, [200, 180]) 

        pygame.display.flip()
 
def tela_confg():
    global largura, altura, tela, dificuldade, quadrado, velocidade, dificuldade2
    largura, altura = 600, 400
    tela = pygame.display.set_mode((largura, altura))
    rodando = True
    dificuldade = 0
    dificuldade2 = 0
    voltar = pygame.Rect(10, 370, 70, 25)
    quadrado_d1 = pygame.Rect(60, 160, 100, 40)
    quadrado_d2 = pygame.Rect(60, 240, 100, 40)
    quadrado_d3 = pygame.Rect(60, 320, 100, 40)

    quadrado_d4 = pygame.Rect(280, 160, 100, 40)
    quadrado_d5 = pygame.Rect(280, 240, 100, 40)
    quadrado_d6 = pygame.Rect(280, 320, 100, 40)
    while rodando:
        desenhar_chao_xadrez()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if quadrado_d1.collidepoint(evento.pos):
                     dificuldade = 1
                     velocidade = 1
                if quadrado_d2.collidepoint(evento.pos):
                     dificuldade = 2
                     velocidade = 5
                if quadrado_d3.collidepoint(evento.pos):
                     dificuldade = 3
                     velocidade = 15

                if quadrado_d6.collidepoint(evento.pos):
                    dificuldade2 = 3
                    quadrado = 50
                if quadrado_d5.collidepoint(evento.pos):
                    dificuldade2 = 2
                    quadrado = 20
                if quadrado_d4.collidepoint(evento.pos):
                    dificuldade2 = 1
                    quadrado = 10

                if voltar.collidepoint(evento.pos):
                    tela_inicial()

        pygame.draw.rect(tela, cor_personalizada_azul2, quadrado_d1)
        pygame.draw.rect(tela, cor_personalizada_azul2, quadrado_d2)
        pygame.draw.rect(tela, cor_personalizada_azul2, quadrado_d3)


        pygame.draw.rect(tela, cor_personalizada_azul2, quadrado_d4)
        pygame.draw.rect(tela, cor_personalizada_azul2, quadrado_d5)
        pygame.draw.rect(tela, cor_personalizada_azul2, quadrado_d6)

        pygame.draw.rect(tela, cor_personalizada_vermelha, voltar)

        fonte1 = pygame.font.SysFont("Times New Roman", 40)
        texto = fonte1.render("Velocidade", True, preto)
        tela.blit(texto, [30, 70])
        texto = fonte1.render("do jogo", True, preto)
        tela.blit(texto, [60, 110])

        texto = fonte1.render("Vel.1", True, branco)
        tela.blit(texto, [65, 157])
        texto = fonte1.render("Vel.5", True, branco)
        tela.blit(texto, [65, 237])
        texto = fonte1.render("Vel.15", True, branco)
        tela.blit(texto, [59, 317])

        texto = fonte1.render("Dificuldade", True, preto)
        tela.blit(texto, [240, 90])

        texto = fonte1.render("Niv.1", True, branco)
        tela.blit(texto, [280, 157])
        texto = fonte1.render("Niv.2", True, branco)
        tela.blit(texto, [280, 237])
        texto = fonte1.render("Niv.3", True, branco)
        tela.blit(texto, [280, 317])

        fonte2 = pygame.font.SysFont("Times New Roman", 25)
        texto = fonte2.render("Voltar", True, branco)
        tela.blit(texto, [15, 368])

        pygame.display.update()
        pygame.display.flip()

tela_inicial()
