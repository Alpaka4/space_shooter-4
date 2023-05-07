from settings import *
import pygame
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(BULLET_NAME).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedy=10
    def update(self):
        self.rect.y-=self.speedy
        if self.rect.y < 0:
            self.kill()
        
