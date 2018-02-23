# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 22:04:37 2018

@author: Oliver
"""
import sys
import pygame
#from settings import Settings
#from ship import Ship
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)   
    ship.blitme()
        
    pygame.display.flip()
