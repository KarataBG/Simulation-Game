import arcade


class Tree:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = arcade.Sprite("images/tree.png", center_x=x, center_y=y, hit_box_algorithm="Simple")

    workersList = []
    resources = 25
    workers = 0
    type = "tree"
    cat = "res"
