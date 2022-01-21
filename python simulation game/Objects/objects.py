import arcade


class Objects:

    def __init__(self, x, y, typer, cat, imageLoc):
        self.x = x
        self.y = y
        self.sprite = arcade.Sprite(imageLoc, center_x=x, center_y=y, hit_box_algorithm="Simple")
        # self.sprite = arcade.Sprite()
        self.type = typer
        self.cat = cat

    # type = "house"
    # cat = "struc"
