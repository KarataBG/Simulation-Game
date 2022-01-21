import arcade


class Farm:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = arcade.Sprite("images/farm.png", center_x=x, center_y=y, hit_box_algorithm="Simple")

    workersList = []
    resources = 500
    workers = 0
    type = "farm"
    cat = "res"
