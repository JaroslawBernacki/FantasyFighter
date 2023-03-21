import pygame
class Player():
    def __init__(self,x,y):
        self.flip=False
        self.rect=pygame.Rect((x,y,80,160))
        self.vel_y=0
        self.skok=False
        self.typ_ataku=0
        self.attack_cooldown=False
        self.zdrowie=100

        
    def move(self,szerokosc_okna,wysokosc_okna,surface,target):
        Speed = 10
        Grawitacja=2
        dx = 0
        dy = 0
        #wychwyc wcisniety klawisz
        key=pygame.key.get_pressed()
        #tylko jesli nie atakuje
        if self.attack_cooldown==False:
        #atak
            if key[pygame.K_r] or key[pygame.K_t]:
                self.attack(surface,target)
                if key[pygame.K_r]:
                    self.typ_ataku=1
                if key[pygame.K_t]:
                    self.typ_ataku=2

            #ruch graczy
            if key[pygame.K_a]:
                dx=-Speed
            if key[pygame.K_d]:
                dx=Speed
            #skok
            if key[pygame.K_w] and self.skok==False:
                self.skok=True
                self.vel_y=-30
        self.vel_y+=Grawitacja
        dy += self.vel_y
        #pozycja gracza
        if self.rect.left+dx<0:
            dx=-self.rect.left
        if self.rect.right+dx>szerokosc_okna:
            dx=szerokosc_okna-self.rect.right
        if self.rect.bottom+dy>=wysokosc_okna-110:
            self.vel_y=0
            self.skok=False
            dy=wysokosc_okna-110-self.rect.bottom
        #kierunek gracza
        if target.rect.centerx>self.rect.centerx:
            self.flip=False
        else:
            self.flip=True
        self.rect.x+=dx
        self.rect.y+=dy
    def attack(self,surface,target):
        self.attack_cooldown=True
        attacking_rect=pygame.Rect(self.rect.centerx-2*self.rect.width*self.flip,self.rect.y,2 * self.rect.width,self.rect.height)
        if attacking_rect.colliderect(target.rect):
            print("hit")
            target.zdrowie-=10
        pygame.draw.rect(surface,(0,255,0),attacking_rect)
    def draw(self,surface):
        pygame.draw.rect(surface,(255,0,0),self.rect)

