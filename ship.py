# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 21:32:50 2018

@author: Oliver
"""
import pygame
class Ship():
    def __init__(self,screen):
        self.screen = screen
        
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
