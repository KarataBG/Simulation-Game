import arcade


class Rock:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = arcade.Sprite("images/rock.png", center_x=x, center_y=y, hit_box_algorithm="Simple")

    workersList = []
    resources = 65
    workers = 0
    type = "rock"
    cat = "res"

# class Rock(Objects.objects):
#
#     def __init__(self):
#         x = 500
