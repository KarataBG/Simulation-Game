import arcade


class TownHall:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = arcade.Sprite("images/townHall.png", center_x=x, center_y=y, hit_box_algorithm="Simple")

    type = "townHall"
    cat = "struc"
