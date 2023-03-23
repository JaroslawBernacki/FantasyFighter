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
gracz1tekstury=[]
gracz2tekstury=[]
lista_sprajtow=["Attack_1.png","Attack_2.png","Attack_3.png","Dead.png","Hurt.png","Idle.png","Jump.png","Protect.png","Run.png","Walk.png"]
for i in lista_sprajtow:
    sciezka="assets/images/characters/sprites/Samurai_warrior/"+i
    gracz1tekstura=pygame.image.load(sciezka).convert_alpha()
    gracz1tekstury.append(gracz1tekstura)
for i in lista_sprajtow:
    sciezka="assets/images/characters/sprites/Samurai_warrior/"+i
    gracz2tekstura=pygame.image.load(sciezka).convert_alpha()
    gracz2tekstury.append(gracz2tekstura)
#gracz2tekstura=pygame.image.load("assets/images/characters/sprites/Skeleton_warrior/Walk.png").convert_alpha()
#dane graczy
player1size=128
player1scale=4
player1offset=[72,56]
player2size=128
player2scale=4
player2offset=[72,56]
player1data=[player1size,player1scale,player1offset]
player2data=[player2size,player2scale,player2offset]
gracz1_kroki_animacji=[4,5,4,6,2,5,7,2,8,9]
gracz2_kroki_animacji=[4,5,4,6,2,5,7,2,8,9]
#Funkcje zwiazane z rysowaniem tekstur
def rysuj_tlo():
    tlo_przeskalowane=pygame.transform.scale(tlo,(Szerokosc_okna,Wysokosc_okna))
    okno.blit(tlo_przeskalowane,(0,0))
#Funkcje zwiazane z silnikiem gry
fighter_1=Player(1,200,310,False,player1data,gracz1tekstury,gracz1_kroki_animacji)
fighter_2=Player(2,700,310,True,player2data,gracz2tekstury,gracz2_kroki_animacji)
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
    fighter_2.move(Szerokosc_okna,Wysokosc_okna,okno,fighter_1)
    fighter_1.update()
    fighter_2.update()
    fighter_1.draw(okno)
    fighter_2.draw(okno)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    pygame.display.update()
pygame.quit()
