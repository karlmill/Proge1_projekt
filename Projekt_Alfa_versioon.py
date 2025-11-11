import pygame
pygame.init()

screen=pygame.display.set_mode((640, 640))

hiir = pygame.image.load('hiir.png').convert()
hiir = pygame.transform.scale(hiir, (50, 50))
hiir.set_colorkey((0, 0, 0))
running = True
x = 0
kell = pygame.time.Clock()
delta = 0.1

while running:
    screen.fill((255, 255, 255))
    screen.blit(hiir, (x, 0))
    x += 50 * delta

    for event in pygame.event.get():
        if event.type == pygame.quit:
           running = False
    pygame.display.flip()
    delta_aeg = kell.tick(60) / 1000
    delta_aeg = max(0.001, min(0.1, delta_aeg))
pygame.quit() 