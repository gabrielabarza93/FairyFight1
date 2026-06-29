#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_GOLD, MENU_OPTION, COLOR_BLACK, COLOR_YELLOW, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/MenuBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self,):
        menu_option = 0
        pygame.mixer.music.load("./asset/menu.wav")
        pygame.mixer.music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(70, "Fairy", COLOR_GOLD, (WIN_WIDTH / 2, 70))
            self.menu_text(70, "Fight", COLOR_GOLD, (WIN_WIDTH / 2, 130))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(25, MENU_OPTION[i], COLOR_YELLOW, (WIN_WIDTH / 2, 220 + 40 * i))
                else:
                    self.menu_text(25, MENU_OPTION[i], COLOR_WHITE, (WIN_WIDTH / 2, 220 + 40 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: # ENTER
                        return MENU_OPTION[menu_option]

    def _draw_text_effect(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, font_path: str, outline_color=(20, 10, 30)):
        text_font: Font = pygame.font.Font(font_path, text_size)
        main_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        outline_surf: Surface = text_font.render(text, True, outline_color).convert_alpha()
        highlight_surf: Surface = text_font.render(text, True, (255, 255, 255)).convert_alpha()

        x, y = text_center_pos

        # borda
        outline_offsets = [
            (-2, 0), (2, 0), (0, -2), (0, 2),
            (-2, -2), (-2, 2), (2, -2), (2, 2),
        ]
        for dx, dy in outline_offsets:
            self.window.blit(source=outline_surf, dest=outline_surf.get_rect(center=(x + dx, y + dy)))

        # brilho / destaque
        highlight_surf.set_alpha(70)
        self.window.blit(source=highlight_surf, dest=highlight_surf.get_rect(center=(x - 2, y - 2)))

        # texto principal
        self.window.blit(source=main_surf, dest=main_surf.get_rect(center=text_center_pos))

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        self._draw_text_effect(
            text_size=text_size,
            text=text,
            text_color=text_color,
            text_center_pos=text_center_pos,
            font_path="./asset/PixeloidSans-Bold.ttf",
            outline_color=(0, 0, 0)
        )

    def game_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        self._draw_text_effect(
            text_size=text_size,
            text=text,
            text_color=text_color,
            text_center_pos=text_center_pos,
            font_path="./asset/PixeloidSans.ttf",
            outline_color=(255, 255, 255),
        )