import arcade


class Worker:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite = arcade.Sprite("images/worker.png", center_x=x, center_y=y, hit_box_algorithm="Simple")

    workX = -1
    workY = -1
    workplace = ""
    isWorking = False
    type = "worker"
    cat = "human"

