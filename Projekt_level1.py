import pygame

labürint = [
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1],
    [1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,0,0,1,0,0,1,0,1,0,1],
    [1,0,1,0,1,1,1,0,1,0,1,1,0,0,0,1],
    [1,0,1,0,0,0,0,0,1,0,0,0,0,1,1,1],
    [1,0,1,1,1,1,0,1,1,1,1,1,1,1,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

ühiku_suurus = 40

takistused = []

for i, rida in enumerate(labürint):
    for j, ühik in enumerate(rida):
        if ühik == 1:
            x_pos = j * ühiku_suurus
            y_pos = i * ühiku_suurus
            takistused.append(pygame.Rect(x_pos, y_pos, 20, 20))


def level_1(screen, x_alg, y_alg, elud_alg, hiir, font, kell, delta):

    x = x_alg
    y = y_alg
    hiire_suurus = 30
    kiirus = 35
    elud = elud_alg
    level_running = True
    moving_right = moving_left = moving_up = moving_down = False
    while level_running:
        screen.fill((255, 255, 255)) #mängutaust valgeks
        screen.blit(hiir, (x, y)) #hiir mänguekraanile
        #alguse ja lõpu ristkülikud(asukoht, suurus), lisatud ekraanile
        algus = pygame.Rect(0, 0, 75, 75) 
        lõpp = pygame.Rect(570, 570, 100, 100)
        pygame.draw.rect(screen, (255, 0, 0), algus)
        pygame.draw.rect(screen, (255, 0, 0), lõpp)
    
        hiir_rect = pygame.Rect(x, y, hiire_suurus, hiire_suurus)

        #takistused ekraanile joonistatud
        for t in takistused:
            pygame.draw.rect(screen, (0, 0, 0), t)

        #tekstid ja kirjutame ekraanile
        tekst = font.render('Algus', True, (0, 0, 0))
        tekst1 = font.render('Lõpp', True, (0, 0, 0))
        tekst2 = font.render('Tubli! Said hakkama!', True, (0, 0, 0))
        tekst3 = font.render('Jõua lõppu! Edu!', True, (0, 0, 0))
        screen.blit(tekst, (0, 0))
        screen.blit(tekst1, (570, 570))
        
        # elude ekraanile kuvamine 
        elud_tekst = font.render(f'Elusid: {elud}', True, (0, 0, 255))
        screen.blit(elud_tekst, (540, 10)) # Asukoht üleval paremal
        #olukorrakontroll
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #kui ekraan pannakse ristist kinni, siis mäng lõpetab töö
                level_running = False
                return "QUIT", x, y, elud
            #kui mõni nooleklahv on all vajutatud, siis sõltuvalt kindlast nupust hakkab hiir liikuma
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moving_right = True
                if event.key == pygame.K_LEFT:
                    moving_left = True
                if event.key == pygame.K_UP:
                    moving_up = True
                if event.key == pygame.K_DOWN:
                    moving_down = True  
            #kui nupp lahti lastud, siis liikumine on False ja liikumine lõpeb
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    moving_right = False
                if event.key == pygame.K_LEFT:
                    moving_left = False
                if event.key == pygame.K_UP:
                    moving_up = False
                if event.key == pygame.K_DOWN:
                    moving_down = False
        #liikumise loogika
        if moving_right:
            x += kiirus * delta
        if moving_left:
            x -= kiirus * delta
        if moving_down:
            y += kiirus * delta
        if moving_up:
            y -= kiirus * delta
        
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
                level_running = False
                return "QUIT", x, y, elud # Kui elud otsas, paneb mängu kinni
        #alguse ja lõpu tekstide kuvamine
        if x > 570 and y > 570:
            screen.blit(tekst2, (320, 320))
            return "LEVEL_2", x, y, elud
        if x < 75 and y < 75:
            screen.blit(tekst3, (90, 40))
        #loogika, et hiir ekraanilt välja ei läheks
        if x < 2:
            x += 20
        elif x > 610:
            x -= 20
        
        if y < 2:
            y += 20
        elif y > 610:
            y -= 20

        pygame.display.flip() #värskendab ala, mis on muutunud, mitte tervet ekraani.
        delta_aeg = kell.tick(60) / 1000 #kahekaadri vaheline aeg millisekundites
        delta_aeg = max(0.001, min(0.1, delta_aeg))