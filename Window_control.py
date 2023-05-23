import pygame
import menu_test_version
import battle_test
pygame.init()
#Parametry okna
Szerokosc_okna=1200
Wysokosc_okna=800
#Deklaracja okna
okno=pygame.display.set_mode((Szerokosc_okna,Wysokosc_okna))
pygame.display.set_caption("Fantasy Fighter")
#ograniczenie fps
clock=pygame.time.Clock()
FPS=60
gamestate=0
run=True
while run:
    if gamestate==0:
        menu_data=menu_test_version.Menu(Szerokosc_okna,Wysokosc_okna,okno)
        run=menu_data[0]
        chosen_heroes=menu_data[1]
        gamestate+=1
    if gamestate==1:
        battle=battle_test.battle(okno,chosen_heroes[0],chosen_heroes[1])
        gamestate+=1
    else:
        print(chosen_heroes[0],chosen_heroes[1])
        run=False