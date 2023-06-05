import pygame
import fighter
#import projectile
class Mage(fighter.Player):
   def __init__(self,gracz,x,y,flip,dane,sprajt,kroki_animacji):
        super().__init__(gracz,x,y,flip,dane,sprajt,kroki_animacji)
        #attack sounds
        self.strike_one_sfx=pygame.mixer.Sound("assets/sound/staffStrike.mp3")
        self.strike_two_sfx=pygame.mixer.Sound("assets/sound/staffSwipe.mp3")
        self.strike_three_sfx=pygame.mixer.Sound("assets/sound/swoosh.mp3")
   def move(self,szerokosc_okna,wysokosc_okna,surface,target,koniec_rundy):
        Speed = 10
        Grawitacja=2
        dx = 0
        dy = 0
        #self.shot=False
        self.running=False
        self.typ_ataku=0

        #wychwyc wcisniety klawisz
        key=pygame.key.get_pressed()
        #tylko jesli nie atakuje
        if self.w_trakcie_ataku==False and self.alive==True and koniec_rundy==False:
            #sprawdz ktory gracz
            if self.gracz==1:
                #atak
                if key[pygame.K_r] or key[pygame.K_t] or key[pygame.K_y]:
                    self.attack(surface,target)
                    if key[pygame.K_r]:
                        self.typ_ataku=1
                    if key[pygame.K_t]:
                        self.typ_ataku=2
                    if key[pygame.K_y]:
                        self.typ_ataku=3
                       # self.shot=True

                #ruch graczy
                if key[pygame.K_a]:
                    dx=-Speed
                    self.running=True
                if key[pygame.K_d]:
                    dx=Speed
                    self.running=True
                #skok
                if key[pygame.K_w] and self.skok==False:
                    self.skok=True
                    self.vel_y=-30

            elif self.gracz==2:
                #atak
                
                if key[pygame.K_KP1] or key[pygame.K_KP2] or key[pygame.K_KP3]:
                    self.attack(surface,target)
                    if key[pygame.K_KP1]:
                        self.typ_ataku=1
                    if key[pygame.K_KP2]:
                        self.typ_ataku=2
                    if key[pygame.K_KP3]:
                        self.typ_ataku=3
                     #   self.projectile(surface,target)

                #ruch graczy
                if key[pygame.K_LEFT]:
                    dx=-Speed
                    self.running=True
                if key[pygame.K_RIGHT]:
                    dx=Speed
                    self.running=True
                #skok
                if key[pygame.K_UP] and self.skok==False:
                    self.skok=True
                    self.vel_y=-30
        self.vel_y+=Grawitacja
        dy += self.vel_y
        #pozycja gracza
        if self.rect.left+dx<0:
            dx=-self.rect.left
        if self.rect.right+dx>szerokosc_okna:
            dx=szerokosc_okna-self.rect.right
        if self.rect.bottom+dy>=wysokosc_okna-180:
            self.vel_y=0
            self.skok=False
            dy=wysokosc_okna-180-self.rect.bottom
        if self.flip==False and self.rect.colliderect(target.rect):
            self.rect.right=target.rect.left+1
        if self.flip==True and self.rect.colliderect(target.rect):
            self.rect.left=target.rect.right-1
        #kierunek gracza
        if target.rect.centerx>self.rect.centerx:
            self.flip=False
        else:
            self.flip=True
        self.rect.x+=dx
        self.rect.y+=dy
        #cooldown ataku
        if self.attack_cooldown>0:
            self.attack_cooldown-=1

   def update(self):
        #Jezeli zdrowie jest rowne lub mniejsze 0 gracz umiera
        if self.zdrowie<=0:
            self.zdrowie=0
            self.alive=False
            self.update_action(4)
        #wybor animacji
        elif self.trafienie==True:
            self.update_action(3)
        elif self.w_trakcie_ataku==True:
            if self.typ_ataku==1:
                self.update_action(5)
                self.strike_one_sfx.play()
            elif self.typ_ataku==2:
                self.update_action(6)
                self.strike_two_sfx.play()
            elif self.typ_ataku==3:
                self.update_action(8)
                self.strike_three_sfx.play()
        elif self.skok==True:
            self.update_action(7)
        elif self.running==True:
            self.update_action(2)
        else:
            self.update_action(0)

        animation_cooldown=100
        #wyswietl wybrana animacje
        self.image=self.animation_list[self.action][self.frame_index]
        #zmiana klatki animacji
        if pygame.time.get_ticks()-self.update_time>animation_cooldown:
            self.frame_index += 1
            self.update_time=pygame.time.get_ticks()
        #sprawdz czy animacja sie skonczyla
        if self.frame_index>=len(self.animation_list[self.action]):
            #jezeli gracz umarl zakoncz animacje na ostatniej klatce
            if self.alive==False:
                self.frame_index=len(self.animation_list[self.action])-1
            else:
                self.frame_index=0
                #obsluga cooldowna ataku
                if self.action==5 or self.action==6 or self.action==8:
                    self.w_trakcie_ataku=False
                    self.attack_cooldown=50
                if self.action==3:
                    self.trafienie=False
                    #jezeli gracz jest trafiony w trakcie animacji animacja jest przerwana
                    self.w_trakcie_ataku=False
                    self.attack_cooldown=50
   #def projectile(self,surface,target):
    #    if self.shot==True:
     #       self.missle=projectile.Projectile(self.gracz,self.rect.centerx-2*self.rect.width,self.rect.y,2 * self.rect.width,self.flip,self.dane,self.animation_list[9])
      #      self.shot=False
class Samurai_warrior(fighter.Player):
    pass
class Samurai_commander(fighter.Player):
   def __init__(self,gracz,x,y,flip,dane,sprajt,kroki_animacji):
        super().__init__(gracz,x,y,flip,dane,sprajt,kroki_animacji)
class Skeleton_warrior(fighter.Player):
   def __init__(self,gracz,x,y,flip,dane,sprajt,kroki_animacji):
        super().__init__(gracz,x,y,flip,dane,sprajt,kroki_animacji)