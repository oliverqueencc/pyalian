# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:49:31 2018

@author: Oliver
"""
import sys
import pygame
from settings  import Settings
from ship import Ship
import game_function as gf
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_heigh))
    pygame.display.set_caption("Alien")

    ship = Ship(screen)
    while True:
        gf.check_events()
        gf.update_screen(ai_settings,screen,ship)
        
run_game()
