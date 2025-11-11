import pygame
pygame.init()

screen=pygame.display.set_mode((640, 640))

hiir = pygame.image.load('hiir.png').convert()
hiir = pygame.transform.scale(hiir, (50, 50))
hiir.set_colorkey((0, 0, 0))
running = True
x = y = 10
kell = pygame.time.Clock()
delta = 0.1
font = pygame.font.Font(None, size=30)
moving_right = moving_left = moving_up = moving_down = False

while running:
    screen.fill((255, 255, 255))
    screen.blit(hiir, (x, y))
    algus = pygame.Rect(0, 0, 75, 75)
    lõpp = pygame.Rect(570, 570, 100, 100)
    pygame.draw.rect(screen, (255, 0, 0), algus)
    pygame.draw.rect(screen, (255, 0, 0), lõpp)
    takistus1 = pygame.Rect(200, 100, 100, 100)
    takistus2 = pygame.Rect(75, 150, 30, 70)
    takistus3 = pygame.Rect(300, 400, 30, 70)
    takistus4 = pygame.Rect(250, 100, 100, 100)
    takistus5 = pygame.Rect(400, 150, 150, 70)
    takistus6 = pygame.Rect(450, 400, 100, 200)
    takistus7 = pygame.Rect(100, 300, 200, 50)
    pygame.draw.rect(screen, (0, 0, 0), takistus1)
    pygame.draw.rect(screen, (0, 0, 0), takistus2)
    pygame.draw.rect(screen, (0, 0, 0), takistus3)
    pygame.draw.rect(screen, (0, 0, 0), takistus4)
    pygame.draw.rect(screen, (0, 0, 0), takistus5)
    pygame.draw.rect(screen, (0, 0, 0), takistus6)
    pygame.draw.rect(screen, (0, 0, 0), takistus7)



    tekst = font.render('Algus', True, (0, 0, 0))
    tekst1 = font.render('Lõpp', True, (0, 0, 0))
    screen.blit(tekst, (0, 0))
    screen.blit(tekst1, (570, 570))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_UP:
                moving_up = True
            if event.key == pygame.K_DOWN:
                moving_down = True  

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_UP:
                moving_up = False
            if event.key == pygame.K_DOWN:
                moving_down = False    

    if moving_right:
        x += 50 * delta
    if moving_left:
        x -= 50 * delta
    if moving_down:
        y += 50 * delta
    if moving_up:
        y -= 50 * delta

    pygame.display.flip()
    delta_aeg = kell.tick(60) / 1000
    delta_aeg = max(0.001, min(0.1, delta_aeg))
pygame.quit() 