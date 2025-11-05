import pygame
import sys

# Initialisation
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projet Tuteuré - Pygame")

clock = pygame.time.Clock()
running = True

# Couleurs
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)

# Boucle principale du jeu
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLUE)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
