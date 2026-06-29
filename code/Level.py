#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface
from pygame import Rect
from pygame.font import Font
from code.Entity import Entity
from code.EntityFactory import EntityFactory

class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]) -> None:
        self.window = window
        self.name = name
        self.game_mode = game_mode # Game mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()