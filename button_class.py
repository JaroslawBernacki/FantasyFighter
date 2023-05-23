import pygame
class button():
    def __init__(self,x,y,image,scale,hero_number):
        width=image.get_width()
        height=image.get_height()
        self.image=pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked=False
        self.hero_number=hero_number
    def draw(self,okno):
        okno.blit(self.image,(self.rect.x,self.rect.y))
    def select(self,player):

        pass




