# INSTALAR O PYGAME ( pip install pygame )
import pygame
import random

# INICIALIZAÇÃO
pygame.init()

# Definindo tamanho da tela
LARGURA_TELA, ALTURA_TELA = 600, 400
FPS = 10
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA), 0, 32)
relogio = pygame.time.Clock()

# Definindo placar
placar = 0

# Criação da Surface para movimentos
area_movimento = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
area_movimento = area_movimento.convert()

# Constantes de cores
BRANCO = "white"
VERDE  = "green"
VERMELHO = "red"
PRETO = "black"

# Tamanho da Grade do Jogo
GRADE_TAMANHO = 20
GRADE_LARGURA = LARGURA_TELA // GRADE_TAMANHO
GRADE_ALTURA = ALTURA_TELA // GRADE_TAMANHO

# Direcionais
CIMA = (0, -1)
BAIXO = (0, 1)
ESQUERDA = (-1, 0)
DIREITA = (1, 0)

# ----- inicio da classe COBRA ---------
class Cobra: 
    def __init__(self, tela):
        self.tamanho = 1
        self.posicao = [
            ((LARGURA_TELA // 2, ALTURA_TELA // 2))
        ]
        self.direcao = random.choice([CIMA, BAIXO, ESQUERDA, DIREITA])
        self.cor = VERDE
        self.tela = tela
    
    def pega_direcao_cobra(self):
        return self.posicao[0]
    
    def virar(self, direcao):
        if self.tamanho > 1  and (
            (direcao[0] * - 1, direcao[1] * - 1) == self.direcao
        ):
            return
        else:
            self.direcao = direcao
    
    def mover(self):
        posicao_atual = self.pega_direcao_cobra()
        eixo_x, eixo_y = self.direcao
        nova_direcao = (
            ((posicao_atual[0] + (eixo_x * GRADE_TAMANHO)) % LARGURA_TELA),
            ((posicao_atual[1] + (eixo_y * GRADE_TAMANHO)) % ALTURA_TELA)
        )
        
        # Regra de colisão contra o corpo
        if len(self.posicao) > 2 and nova_direcao in self.posicao[2:]:
            quit()
        else:
            # Inserindo novo corpo
            self.posicao.insert(0, nova_direcao)
            if len(self.posicao) > self.tamanho:
                self.posicao.pop()
        
    def controlar_teclas(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            self.virar(CIMA)
        elif teclas[pygame.K_DOWN]:
            self.virar(BAIXO)
        elif teclas[pygame.K_LEFT]:
            self.virar(ESQUERDA)
        elif teclas[pygame.K_RIGHT]:
            self.virar(DIREITA)
    
    def desenhar(self, area_movimento):
        for pos in self.posicao:
            quadrado = pygame.Rect(
                (pos[0], pos[1]),
                (GRADE_TAMANHO, GRADE_TAMANHO)
            )
            pygame.draw.rect(area_movimento, self.cor, quadrado)
            pygame.draw.rect(area_movimento, PRETO, quadrado, 1)
        
# ------ fim da classe COBRA -------

# ----- inicio da classe COMIDA ---------
class Comida:
    def __init__(self, snake):
        self.posicao = (0, 0)
        self.cor = VERMELHO
        self.cobra = snake
        self.posicao_aleatoria()
        
    def posicao_aleatoria(self):
        while True:
            # Gerar a posicao aleatória do meu objeto Comida
            self.posicao = (
                random.randint(0, GRADE_LARGURA - 1) * GRADE_TAMANHO,
                random.randint(0, GRADE_ALTURA - 1) * GRADE_TAMANHO
            )

            # Verificar se a comida não está no corpo da cobra
            if self.posicao not in self.cobra.posicao:
                break
        
    def desenhar(self, area_movimento):
        quadrado = pygame.Rect((self.posicao[0], self.posicao[1]), (GRADE_TAMANHO, GRADE_TAMANHO))
        pygame.draw.rect(area_movimento, self.cor, quadrado)
        pygame.draw.rect(area_movimento, PRETO, quadrado, 1)
# ----- fim da classe COMIDA ---------

cobra = Cobra(tela)
food = Comida(cobra)

# LOOP PRINCIPAL
while True:
    # EVENTOS
    # -------- inicio do for --------
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
    # --------- fim do for ---------


    # ATUALIZAÇÃO
    cobra.controlar_teclas()
    cobra.mover()
    
    if cobra.pega_direcao_cobra() == food.posicao:
        cobra.tamanho += 1
        food.posicao_aleatoria()
        placar += 1
    
    area_movimento.fill(BRANCO)
    
    cobra.desenhar(area_movimento)
    food.desenhar(area_movimento)
    
    # Exibi o placar
    fonte = pygame.font.Font(None, 36)
    texto = fonte.render(f"Placar: {placar}", True, PRETO)
    area_movimento.blit(texto, (10, 10))

    tela.fill(BRANCO)

    # RENDERIZAÇÃO
    tela.blit(area_movimento, (0, 0))
    pygame.display.update()
    relogio.tick(FPS)
