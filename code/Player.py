#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Entity import Entity

class Player(Entity):
    def __init__(self, name: str, postion: tuple):
        super().__init__(name, postion)

    def update(self, ):
        pass

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 1


        pass
