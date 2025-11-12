import pygame
pygame.init()
import time

screen=pygame.display.set_mode((640, 640))
pygame.display.set_caption('labürint Alfa')

hiir = pygame.image.load('hiir.png').convert()
hiir = pygame.transform.scale(hiir, (50, 50))
hiir.set_colorkey((0, 0, 0))
running = True
x = y = 10
kell = pygame.time.Clock()
delta = 0.1
font = pygame.font.Font(None, size=30)
moving_right = moving_left = moving_up = moving_down = False
# elud
elud = 3


while running:
    screen.fill((255, 255, 255))
    screen.blit(hiir, (x, y))
    algus = pygame.Rect(0, 0, 75, 75)
    lõpp = pygame.Rect(570, 570, 100, 100)
    pygame.draw.rect(screen, (255, 0, 0), algus)
    pygame.draw.rect(screen, (255, 0, 0), lõpp)
    takistused = [
        pygame.Rect(200, 100, 100, 100),
        pygame.Rect(75, 150, 30, 70),
        pygame.Rect(300, 400, 30, 70),
        pygame.Rect(250, 100, 100, 100),
        pygame.Rect(400, 150, 150, 70),
        pygame.Rect(450, 400, 100, 200),
        pygame.Rect(100, 300, 200, 50)
    ]
    hiir_rect = pygame.Rect(x, y, 50, 50)


    for t in takistused:
        pygame.draw.rect(screen, (0, 0, 0), t)


    tekst = font.render('Algus', True, (0, 0, 0))
    tekst1 = font.render('Lõpp', True, (0, 0, 0))
    tekst2 = font.render('Tubli! Said hakkama!', True, (0, 0, 0))
    tekst3 = font.render('Jõua lõppu! Edu!', True, (0, 0, 0))
    screen.blit(tekst, (0, 0))
    screen.blit(tekst1, (570, 570))
    
    # elude ekraanile kuvamine 
    elud_tekst = font.render(f'Elusid: {elud}', True, (0, 0, 255))
    screen.blit(elud_tekst, (540, 10)) # Asukoht üleval paremal

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
    
    # Kokkupõrke kontroll ja elu vähendamine
    collision_detected = False
    for t in takistused:
        if hiir_rect.colliderect(t):
            collision_detected = True
            break

    if collision_detected:
        elud -= 1       
        x = 0
        y = 0
        pygame.time.wait(200)

        if elud <= 0:
            running = False # Kui elud otsas, paneb mängu kinni

    if x > 570 and y > 570:
        screen.blit(tekst2, (320, 320))
    if x < 75 and y < 75:
        screen.blit(tekst3, (90, 40))

    if x < 2:
        x += 20
    elif x > 610:
        x -= 20
    
    if y < 2:
        y += 20
    elif y > 610:
        y -= 20

    pygame.display.flip()
    delta_aeg = kell.tick(60) / 1000
    delta_aeg = max(0.001, min(0.1, delta_aeg))
pygame.quit()