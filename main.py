import pygame
from fighter import Player
pygame.init()
#Okno
Szerokosc_okna=1200
Wysokosc_okna=800
okno=pygame.display.set_mode((Szerokosc_okna,Wysokosc_okna))
pygame.display.set_caption("Fantasy Fighter")
#Framerate
clock=pygame.time.Clock()
FPS=60
#Deklaracja tekstur
tlo=pygame.image.load("assets/images/background/tlo_tiles.png").convert_alpha()
#Funkcje zwiazane z rysowaniem tekstur
def rysuj_tlo():
    tlo_przeskalowane=pygame.transform.scale(tlo,(Szerokosc_okna,Wysokosc_okna))
    okno.blit(tlo_przeskalowane,(0,0))
#Funkcje zwiazane z silnikiem gry
fighter_1=Player(200,310)
fighter_2=Player(700,310)
#Rysowanie paskow zdrowia
def rysuj_pasek_zdrowia(zdrowie,x,y):
    ratio= zdrowie/100
    pygame.draw.rect(okno,(255,255,255),(x-3,y-3,406,36))
    pygame.draw.rect(okno,(255,0,0),(x,y,400,30))
    pygame.draw.rect(okno,(0,255,255),(x,y,400*ratio,30))

#Petla gry
run=True
while run:
    clock.tick(FPS)
    rysuj_tlo()
    rysuj_pasek_zdrowia(fighter_1.zdrowie,20,20)
    rysuj_pasek_zdrowia(fighter_2.zdrowie,620,20)
    fighter_1.move(Szerokosc_okna,Wysokosc_okna,okno,fighter_2)
    #fighter_2.move(Szerokosc_okna,Wysokosc_okna,okno,fighter_1)
    fighter_1.draw(okno)
    fighter_2.draw(okno)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()
