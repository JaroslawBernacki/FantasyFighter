import pygame
from characters import Mage,Samurai_warrior,Samurai_commander,Skeleton_warrior
import character_sprites2
def battle(okno,postac1,postac2,tlo):
    pygame.init()
    #Okno
    Szerokosc_okna,Wysokosc_okna=okno.get_size()
    #Framerate
    clock=pygame.time.Clock()
    FPS=60
    #Deklaracja tekstur
    #tlo=pygame.image.load("assets/images/background/Battleground2/Pale/Battleground2.png").convert_alpha()
    #deklaracja czcionki
    czcionka_odliczania=pygame.font.Font("assets/fonts/Planes_ValMore.ttf",80)
    czcionka_punktow=pygame.font.Font("assets/fonts/Planes_ValMore.ttf",35)
    #ekran wygranej
    wygrana_prompt=pygame.image.load("assets/images/icons/victory.png").convert_alpha()
    wygrana_gracz_1=pygame.image.load("assets/images/icons/Player_1_won.png").convert_alpha()
    wygrana_gracz_2=pygame.image.load("assets/images/icons/Player_2_won.png").convert_alpha()
    #dane graczy
    gracz_1_dane=character_sprites2.check_hero_chosen(postac1,1)
    gracz_2_dane=character_sprites2.check_hero_chosen(postac2,2)
    #Funkcje zwiazane z rysowaniem tekstur
    def rysuj_tlo():
        tlo_przeskalowane=pygame.transform.scale(tlo,(Szerokosc_okna,Wysokosc_okna))
        okno.blit(tlo_przeskalowane,(0,0))
    #Funkcje zwiazane z silnikiem gry
    def fighter1_creation(postac1):
        if postac1==0:
            fighter_1=Samurai_commander(1,200,450,False,gracz_1_dane[0],gracz_1_dane[1],gracz_1_dane[2])
        elif postac1==1:
            fighter_1=Samurai_warrior(1,200,450,False,gracz_1_dane[0],gracz_1_dane[1],gracz_1_dane[2])
        elif postac1==2:
            fighter_1=Mage(1,200,450,False,gracz_1_dane[0],gracz_1_dane[1],gracz_1_dane[2])
        elif postac1==3:
            fighter_1=Skeleton_warrior(1,200,450,False,gracz_1_dane[0],gracz_1_dane[1],gracz_1_dane[2])
        return fighter_1
    def fighter2_creation(postac2):
        if postac2==0:
            fighter_2=Samurai_commander(2,950,450,True,gracz_2_dane[0],gracz_2_dane[1],gracz_2_dane[2])
        elif postac2==1:
            fighter_2=Samurai_warrior(2,950,450,True,gracz_2_dane[0],gracz_2_dane[1],gracz_2_dane[2])
        elif postac2==2:
            fighter_2=Mage(2,950,450,True,gracz_2_dane[0],gracz_2_dane[1],gracz_2_dane[2])
        elif postac2==3:
            fighter_2=Skeleton_warrior(2,950,450,True,gracz_2_dane[0],gracz_2_dane[1],gracz_2_dane[2])
        return fighter_2
    fighter_1=fighter1_creation(postac1)
    fighter_2=fighter2_creation(postac2)
    #fighter_2=Mage(2,950,450,True,gracz_2_dane[0],gracz_2_dane[1],gracz_2_dane[2])
    #Rysowanie paskow zdrowia
    def rysuj_pasek_zdrowia(zdrowie,x,y):
        ratio= zdrowie/100
        pygame.draw.rect(okno,(255,255,255),(x-3,y-3,406,36))
        pygame.draw.rect(okno,(255,0,0),(x,y,400,30))
        pygame.draw.rect(okno,(0,255,255),(x,y,400*ratio,30))
    #rysowanie odliczania
    def rysuj_tekst(text,font,text_color,x,y):
        img=font.render(text,True,text_color)
        okno.blit(img,(x,y))
     #zmienne gry
    odliczanie_rundy=3
    ostatni_update_odliczania=pygame.time.get_ticks()
    wygrane=[0,0] #punkty [gracz 1, gracz 2]
    koniec_rundy=False
    round_over_cooldown=2000
    #music handling
    soundtrack=pygame.mixer.music.load("assets/sound/soundtrack.mp3")
    pygame.mixer.music.play(-1)
    #Petla gry
    run=True
    while run:
        clock.tick(FPS)
        rysuj_tlo()
        rysuj_pasek_zdrowia(fighter_1.zdrowie,20,20)
        rysuj_pasek_zdrowia(fighter_2.zdrowie,760,20)
        rysuj_tekst("P1: "+str(wygrane[0]),czcionka_punktow,(255,0,0),20,60)
        rysuj_tekst("P2: "+str(wygrane[1]),czcionka_punktow,(255,0,0),760,60)
        if odliczanie_rundy<=0:
            fighter_1.move(Szerokosc_okna,Wysokosc_okna,okno,fighter_2,koniec_rundy)
            fighter_2.move(Szerokosc_okna,Wysokosc_okna,okno,fighter_1,koniec_rundy)
        else:
            #wyswietl licznik
            rysuj_tekst(str(odliczanie_rundy),czcionka_odliczania,(0,0,0),Szerokosc_okna/2,Wysokosc_okna/3)
            #updatuj licznik
            if(pygame.time.get_ticks()-ostatni_update_odliczania)>=1000:
                odliczanie_rundy-=1
                ostatni_update_odliczania=pygame.time.get_ticks()
        fighter_1.update()
        fighter_2.update()
        fighter_1.draw(okno)
        fighter_2.draw(okno)
        #gracz przegral
        if koniec_rundy==False:
            if fighter_1.alive==False:
                wygrane[1]+=1
                koniec_rundy=True
                round_over_time=pygame.time.get_ticks()
            elif fighter_2.alive==False:
                wygrane[0]+=1
                koniec_rundy=True
                round_over_time=pygame.time.get_ticks()
        else:
            if wygrane[1]==2:
                okno.blit(wygrana_gracz_2,(100,50))
                if pygame.time.get_ticks()-round_over_time>round_over_cooldown:
                    return 1
            elif wygrane[0]==2:
                okno.blit(wygrana_gracz_1,(100,0))
                if pygame.time.get_ticks()-round_over_time>round_over_cooldown:
                    return 1
            else:
                okno.blit(wygrana_prompt,(375,350))
                if pygame.time.get_ticks()-round_over_time>round_over_cooldown:
                    koniec_rundy=False
                    odliczanie_rundy=3
                    fighter_1=fighter1_creation(postac1)
                    fighter_2=fighter2_creation(postac2)
                    #fighter_1=Player(1,200,450,False,gracz_1_dane[0],gracz_1_dane[1],gracz_1_dane[2])
                    #fighter_2=Player(2,950,450,True,gracz_2_dane[0],gracz_2_dane[1],gracz_2_dane[2])
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        pygame.display.update()
    pygame.quit()
    return 0
