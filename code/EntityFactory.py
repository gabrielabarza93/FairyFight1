import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case "Level1Bg":
                list_bg = []
                order = [0, 5, 6, 1, 4,3]
                for i in order: # imagens level 1 in the right order
                    list_bg.append(Background(f"Level1Bg{i}", (0, 0)))
                    list_bg.append(Background(f"Level1Bg{i}", (WIN_WIDTH, 0)))
                return list_bg
            case "Level2Bg":
                list_bg = []
                order = [5, 3, 0, 7, 4, 1, 6]
                for i in order: # imagens level 2 in the right order
                    list_bg.append(Background(f"Level2Bg{i}", (0, 0)))
                    list_bg.append(Background(f"Level2Bg{i}", (WIN_WIDTH, 0)))
                return list_bg
            case "Player1":
                return Player('Player1', position=(10, WIN_HEIGHT/2))
            case "Player2":
                return Player('Player2', position=(10, WIN_HEIGHT/2 + 80))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))