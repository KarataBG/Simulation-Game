import arcade


class House:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = arcade.Sprite("images/house1.png", center_x=x, center_y=y, hit_box_algorithm="Simple")

    type = "house"
    cat = "struc"
