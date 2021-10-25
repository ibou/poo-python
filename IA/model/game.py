import pygame


def run():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()


class Game:
    def __init__(self):
        pygame.display.set_mode((800, 600))
        pygame.display.set_caption("PyGame - Aventure")
