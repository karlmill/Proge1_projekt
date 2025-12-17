import pygame

labürint = [
 [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
 [0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1],
 [1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1],
 [1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1],
 [1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1],
 [1,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1],
 [1,0,1,1,1,1,1,1,1,0,1,0,1,1,0,1],
 [1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
 [1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1],
 [1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1],
 [1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1],
 [1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1],
 [1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1],
 [1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],
 [1,0,1,1,1,1,1,0,1,1,1,1,0,0,0,0],
 [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]
]

ühiku_suurus = 40

takistused = []

for i, rida in enumerate(labürint):
    for j, ühik in enumerate(rida):
        if ühik == 1:
            x_pos = j * ühiku_suurus
            y_pos = i * ühiku_suurus
            takistused.append(pygame.Rect(x_pos, y_pos, 20, 20))


def level_3(screen, x_alg, y_alg, elud_alg, tegelase_pildid, font, kell, delta, tegelase_kiirus, tegelase_suurus, süda, südame_suurus):
    x = 0
    y = 0

    #tegelase animatsiooni muutujad
    animatsiooni_indeks = 0
    animatsiooni_kiirus = 10
    viimane_aeg = 0
    suund = "parem"

    elud = elud_alg
    level_running = True
    moving_right = moving_left = moving_up = moving_down = False
    
    while level_running:
        screen.fill((255, 255, 255)) #mängutaust valgeks
        #alguse ja lõpu ristkülikud(asukoht, suurus), lisatud ekraanile
        algus = pygame.Rect(0, 0, 75, 75) 
        lõpp = pygame.Rect(570, 570, 100, 100)
        pygame.draw.rect(screen, (255, 0, 0), algus)
        pygame.draw.rect(screen, (255, 0, 0), lõpp)
        praegune_aeg = pygame.time.get_ticks()

        if moving_right or moving_left:
            if praegune_aeg - viimane_aeg > 1000 // animatsiooni_kiirus:
                animatsiooni_indeks = (animatsiooni_indeks + 1) % len(tegelase_pildid)
                viimane_aeg = praegune_aeg
        else:
            animatsiooni_indeks = 0  # seisab

        tegelase_pilt = tegelase_pildid[animatsiooni_indeks]

        # vasakule liikumisel peegeldame pildi
        if suund == "vasak":
            tegelase_pilt = pygame.transform.flip(tegelase_pilt, True, False)
        screen.blit(tegelase_pilt, (x, y))

    
        tegelase_rect = pygame.Rect(x, y, tegelase_suurus, tegelase_suurus)

        #takistused ekraanile joonistatud
        for t in takistused:
            pygame.draw.rect(screen, (0, 0, 0), t)

        #tekstid ja kirjutame ekraanile
        tekst = font.render('Algus', True, (0, 0, 0))
        tekst1 = font.render('Lõpp', True, (0, 0, 0))
        tekst2 = font.render('Tubli! Said hakkama!', True, (0, 0, 0))
        tekst3 = font.render('Jõua 3. leveli lõppu! Edu!', True, (0, 0, 0))
        screen.blit(tekst, (0, 0))
        screen.blit(tekst1, (570, 570))
        
        # elude ekraanile kuvamine 
        for i in range(elud):
            screen.blit(süda, (580 - i * (südame_suurus + 5), 10))

        #olukorrakontroll
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #kui ekraan pannakse ristist kinni, siis mäng lõpetab töö
                level_running = False
                return "QUIT", x, y, elud
            #kui mõni nooleklahv on all vajutatud, siis sõltuvalt kindlast nupust hakkab tegelane liikuma
            if event.type == pygame.KEYDOWN:

                # tegelase suuna määramine
                if event.key == pygame.K_RIGHT:
                    moving_right = True
                    suund = "parem"

                if event.key == pygame.K_LEFT:
                    moving_left = True
                    suund = "vasak"


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
            x += tegelase_kiirus * delta
        if moving_left:
            x -= tegelase_kiirus * delta
        if moving_down:
            y += tegelase_kiirus * delta
        if moving_up:
            y -= tegelase_kiirus * delta
        
        # Kokkupõrke kontroll ja elu vähendamine
        collision_detected = False
        for t in takistused:
            if tegelase_rect.colliderect(t):
                collision_detected = True
                break

        if collision_detected:
            elud -= 1       
            x = 0
            y = 0
            pygame.time.wait(200)

            if elud <= 0:
                level_running = False # Kui elud otsas, paneb mängu kinni
                return "QUIT", x, y, elud
        #alguse ja lõpu tekstide kuvamine
        if x > 570 and y > 570:
            screen.blit(tekst2, (320, 320))
            return "LEVEL_4",  x, y, elud
        if x < 75 and y < 75:
            screen.blit(tekst3, (90, 40))
        #loogika, et tegelane ekraanilt välja ei läheks
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
