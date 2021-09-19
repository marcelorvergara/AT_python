import threading

import pygame
import pygame.time
import random


class Questao6(threading.Thread):
    pygame.init()

    def quadrado_amarelo(self, tela):
        pygame.draw.rect(tela, (255, 255, 0), pygame.Rect(random.randint(1, 800), random.randint(1, 600), 50, 50))

    def __init__(self):
        super().__init__()
        tela = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()
        terminou = False
        while not terminou:
            pygame.display.update()
            clock.tick(60)
            # checar os eventos do mouse
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    terminou = True
                # quadrado amarelo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.quadrado_amarelo(pygame.display.set_mode((800, 600)))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    self.quadrado_amarelo(pygame.display.set_mode((800, 600)))
            pygame.display.update()

        pygame.display.quit()

        pygame.quit()
