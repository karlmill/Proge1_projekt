#https://www.pygame.org/docs/
#Projekt Bive, Lilii-Ann Older, Karl Miller
#Mängu mängimiseks (programmi käivitamiseks) on vajalik alla laadida pygame.
#Allalaadimseks vaja terminali sisestada käsk "pip3 install pygame"
#mängu mängimiseks käivitada 'Laburint_main.py' 
import pygame
import time
import sys
from Projekt_level1 import level_1
from Projekt_level2 import level_2
from Projekt_level3 import level_3
from Projekt_level4 import level_4
from Projekt_level5 import level_5


pygame.init()
screen=pygame.display.set_mode((640, 640))
pygame.display.set_caption('Proge projekt')

tegelase_suurus = 40
tegelase_kiirus = 35
tegelase_pildid = []

# Laeme tegelase pildid ja muudame nende suurust
# Tegelase pildid saadud lingilt https://www.gameart2d.com/cat-and-dog-free-sprites.html
for i in range(1, 11): #pildid 1-10
    pilt = pygame.image.load(f'mängu_tegelane/Walk ({i}).png').convert()
    pilt = pygame.transform.scale(pilt, (tegelase_suurus, tegelase_suurus))
    pilt.set_colorkey((0, 0, 0))
    tegelase_pildid.append(pilt)

# Südame pildi muutujad
südame_suurus = 30
süda = pygame.image.load("süda.png").convert_alpha()
süda = pygame.transform.scale(süda, (südame_suurus, südame_suurus))

# Seina pildi muutujad
seina_pilt_suurus = 40
seina_pilt = pygame.image.load("grass.png").convert_alpha()
seina_pilt = pygame.transform.scale(seina_pilt, (20, 20))

running = True
hetke_x = 0 
hetke_y = 0
kell = pygame.time.Clock()
delta = 0.1
font = pygame.font.Font(None, size=30)
moving_right = moving_left = moving_up = moving_down = False
vaade_horis = vaade_vert = False
elud = 5
mängu_faas = "algus"

LEVELID = {
    "LEVEL_1" : level_1,
    "LEVEL_2" : level_2,
    "LEVEL_3" : level_3,
    "LEVEL_4" : level_4,
    "LEVEL_5" : level_5
}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #kui ekraan pannakse ristist kinni, siis mäng lõpetab töö
            running = False
    if mängu_faas == "QUIT":
        running = False
    elif mängu_faas == "algus":
        print("Tere!")
        mängu_faas = "LEVEL_1"
    elif mängu_faas in LEVELID:
        print(mängu_faas)
        praeguselevelifunktsioon = LEVELID[mängu_faas]
        järgmine_state, hetke_x, hetke_y, elud = praeguselevelifunktsioon(screen, hetke_x, hetke_y, elud, tegelase_pildid, font, kell, delta, tegelase_kiirus, tegelase_suurus, süda, südame_suurus, seina_pilt)
        mängu_faas = järgmine_state
    
    else:
        print(mängu_faas)
        print("Viga!!!")
        running = False

pygame.quit()
sys.exit()