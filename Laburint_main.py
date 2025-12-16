#https://www.pygame.org/docs/
#Projekt Bive, Lilii-Ann Older, Karl Miller
#Mängu mängimiseks (programmi käivitamiseks) on vajalik alla laadida pygame.
#Allalaadimseks vaja terminali sisestada käsk "pip3 install pygame"
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

hiire_suurus = 30
hiir = pygame.image.load('hiir.png').convert()
hiir = pygame.transform.scale(hiir, (hiire_suurus, hiire_suurus))
hiir.set_colorkey((0, 0, 0))

running = True
hetke_x = 10 
hetke_y = 10
kell = pygame.time.Clock()
delta = 0.1
font = pygame.font.Font(None, size=30)
moving_right = moving_left = moving_up = moving_down = False
vaade_horis = vaade_vert = False
elud = 3
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
        järgmine_state, hetke_x, hetke_y, elud = praeguselevelifunktsioon(screen, hetke_x, hetke_y, elud, hiir, font, kell, delta)
        mängu_faas = järgmine_state
    
    else:
        print(mängu_faas)
        print("Viga!!!")
        running = False

pygame.quit()
sys.exit()