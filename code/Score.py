import sys
from datetime import datetime


import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font


from code.Const import COLOR_YELLOW, SCORE_POS, MENU_OPTION, COLOR_WHITE, COLOR_GOLD, COLOR_BLACK
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/ScoreBg.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/score.wav')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!!', COLOR_YELLOW, SCORE_POS['Title'])
            text = 'Enter Player 1 name (4 characters):'
            score = player_score[0]
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
            if game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter Team name (4 characters):'
            if game_mode == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                else:
                    score = player_score[1]
                    text = 'Enter Player 2 name (4 characters):'
            self.score_text(20, text, COLOR_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(20, name, COLOR_WHITE, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./asset/score.wav')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)

        # Título
        self.score_text(50, 'TOP 10 SCORE', COLOR_GOLD, SCORE_POS['Title'])

        # Posição das Colunas
        NAME_X = 200
        SCORE_X = 400
        DATE_X = 600

        HEADER_Y = 120
        FIRST_ROW_Y = 155
        ROW_SPACING = 25

        # Cabeçalho
        self.score_text(25, 'NAME', COLOR_WHITE, (NAME_X, HEADER_Y))
        self.score_text(25, 'SCORE', COLOR_WHITE, (SCORE_X, HEADER_Y))
        self.score_text(25, 'DATE', COLOR_WHITE, (DATE_X, HEADER_Y))

        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        y = FIRST_ROW_Y

        for player_score in list_score:
            id_, name, score, date = player_score

            self.score_text(15, name, COLOR_YELLOW, (NAME_X, y))
            self.score_text(15, f'{score:05d}', COLOR_YELLOW, (SCORE_X, y))
            self.score_text(15, date, COLOR_YELLOW, (DATE_X, y))

            y += ROW_SPACING

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple,
                   text_pos: tuple, align='center'):

        text_font = pygame.font.Font(
            "./asset/PixeloidSans-Bold.ttf",
            text_size
        )

        text_surf = text_font.render(text, True, text_color).convert_alpha()

        if align == 'center':
            text_rect = text_surf.get_rect(center=text_pos)
        elif align == 'left':
            text_rect = text_surf.get_rect(midleft=text_pos)
        elif align == 'right':
            text_rect = text_surf.get_rect(midright=text_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_date = current_datetime.strftime("%d/%m")
    current_time = current_datetime.strftime("%H:%M")
    return f'{current_date} - {current_time}'
