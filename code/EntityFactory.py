from code.Background import Background
from code.Const import WIN_WIDTH
from code.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case "Level1Bg":
                list_bg = []
                ordem = [0, 5, 6, 1, 4,3]
                for i in ordem:
                    list_bg.append(Background(f"Level1Bg{i}", (0, 0)))
                    list_bg.append(Background(f"Level1Bg{i}", (WIN_WIDTH, 0)))
                return list_bg

            case "Player1":
                return Player("Player1", position)