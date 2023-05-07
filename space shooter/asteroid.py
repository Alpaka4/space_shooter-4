from settings import *
import pygame
import random
class Asteroid(pygame.sprite.Sprite):
    def __init__(self,screen,image_list):
        pygame.sprite.Sprite.__init__(self)
        image_original = random.choice(image_list)
        image_original.set_colorkey(BLACK)
        self.image = image_original.copy()
        self.screen=screen
        self.rect = self.image.get_rect()
        self.rect.bottom = random.randint(-80,0)
        self.rect.left = random.randint(0,SCREEN_WIDTH - 40)
        self.speedy= random.randint(1,5)
        self.speedx= random.randint(-2,2)
        if self.rect.width > 80:
            self.damage = 50
        if self.rect.width < 80 and self.rect.width>40:
            self.damage = 30
        if self.rect.width < 40 and self.rect.width>20:
            self.damage = 10
        if self.rect.width < 20 and self.rect.width>10:
            self.damage = 5
    def update(self):
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if self.rect.right<LEFT_BORDER:
            self.rect.bottom = random.randint(-80,0)
            self.rect.left = random.randint(0,SCREEN_WIDTH - 40)
        if self.rect.left>RIGHT_BORDER:
            self.rect.bottom = random.randint(-80,0)
            self.rect.left = random.randint(0,SCREEN_WIDTH - 40)
    def draw(self):
        self.screen.blit(self.image, self.rect)
