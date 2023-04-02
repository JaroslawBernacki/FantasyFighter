import pygame
class Player():
    def __init__(self,gracz,x,y,flip,dane,sprajt,kroki_animacji):
        self.gracz=gracz
        self.size=dane[0]
        self.image_scale=dane[1]
        self.offset=dane[2]
        self.flip=flip
        self.animation_list=self.load_images(sprajt,kroki_animacji)
        self.action=5
        self.frame_index=0
        self.image=self.animation_list[self.action][self.frame_index]
        self.update_time=pygame.time.get_ticks()
        self.rect=pygame.Rect((x,y,80,160))
        self.vel_y=0
        self.skok=False
        self.running=False
        self.typ_ataku=0
        self.attack_cooldown=0
        self.w_trakcie_ataku=False
        self.zdrowie=100
        self.alive=True
        self.trafienie=False
        
    def load_images(self,sprajt,kroki_animacji):
        animation_list=[]
        for y,animation in enumerate(kroki_animacji):
            temp_img_list=[]
            for i in range(animation):
                temp_img=sprajt[y].subsurface(i*self.size,0,self.size,self.size)

                temp_img_list.append(pygame.transform.scale(temp_img,(self.size*self.image_scale,self.size*self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list
    def move(self,szerokosc_okna,wysokosc_okna,surface,target,koniec_rundy):
        Speed = 10
        Grawitacja=2
        dx = 0
        dy = 0
        self.running=False
        self.typ_ataku=0
        #wychwyc wcisniety klawisz
        key=pygame.key.get_pressed()
        #tylko jesli nie atakuje
        if self.w_trakcie_ataku==False and self.alive==True and koniec_rundy==False:
            #sprawdz ktory gracz
            if self.gracz==1:
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
                
                if key[pygame.K_KP1] or key[pygame.K_KP2]:
                    self.attack(surface,target)
                    if key[pygame.K_KP1]:
                        self.typ_ataku=1
                    if key[pygame.K_KP2]:
                        self.typ_ataku=2

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
            elif self.typ_ataku==2:
                self.update_action(6)
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
                if self.action==5 or self.action==6:
                    self.w_trakcie_ataku=False
                    self.attack_cooldown=50
                if self.action==3:
                    self.trafienie=False
                    #jezeli gracz jest trafiony w trakcie animacji animacja jest przerwana
                    self.w_trakcie_ataku=False
                    self.attack_cooldown=50
        

    def attack(self,surface,target):
        if self.attack_cooldown==0 and self.trafienie==False:
            self.w_trakcie_ataku=True
            attacking_rect=pygame.Rect(self.rect.centerx-2*self.rect.width*self.flip,self.rect.y,2 * self.rect.width,self.rect.height)
            if attacking_rect.colliderect(target.rect):
                print("hit")
                target.zdrowie-=10
                target.trafienie=True
            pygame.draw.rect(surface,(0,255,0),attacking_rect)

    def update_action(self,new_action):
        if new_action != self.action:
            self.action=new_action
            self.frame_index=0
            self.update_time=pygame.time.get_ticks()

    def draw(self,surface):
        img=pygame.transform.flip(self.image,self.flip,False)
        #pygame.draw.rect(surface,(255,0,0),self.rect)
        surface.blit(img,(self.rect.x-self.offset[0]*self.image_scale,self.rect.y-self.offset[1]*self.image_scale))

