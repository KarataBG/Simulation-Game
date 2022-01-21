import arcade

"""за големина на игралното поле имам проверката w update() + големината на екрана"""


class TreeMenu:
    currentTree = 0

    def __init__(self):
        pass

    def render(self):
        arcade.draw_lrtb_rectangle_filled(0, 300, 200, 0, arcade.color.SAND)
        pass

    def update(self):
        pass

    def setCurrentRock(self, tree):
        self.currentTree = tree

    def mouseClick(self, x, y):
        pass

    def updateMouse(self, x, y):
        pass
