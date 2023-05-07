from settings import *
import pygame
class Sky(pygame.sprite.Sprite):
    def __init__(self,filename, screen,x,y):
        self.screen=screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image=pygame.transform.scale(self.image,(1000,1005))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y= y
        self.speedy=2
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.y>SCREEN_HEIGHT:
            self.rect.y=-1000
    def draw(self):
        self.screen.blit(self.image, self.rect)
