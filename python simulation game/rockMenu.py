import arcade

"""за големина на игралното поле имам проверката w update() + големината на екрана"""


class RockMenu:
    # xBorder = 1300
    # yBorder = 600
    # x = 800 / 2 - 40
    # y = 600 / 2 - 70
    # xOffset = 0
    # yOffset = 0
    # keyboard = 0

    # sprites = Sprites()

    currentRock = 0

    def __init__(self):
        # self.currentRock = rock
        pass

    def render(self):
        arcade.draw_lrtb_rectangle_filled(0, 300, 200, 0, arcade.color.SAND)
        pass

    def update(self):
        pass

    def setCurrentRock(self, rock):
        self.currentRock = rock

    def mouseClick(self, x, y):
        pass

    def updateMouse(self, x, y):
        pass
