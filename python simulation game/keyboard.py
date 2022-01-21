# from pynput import keyboard
import arcade

""" register с булеви изрази за цъкнат """


class Keyboard:
    moveLeft = False
    moveRight = False
    moveDown = False
    moveUp = False

    def movingLeft(self):
        self.moveLeft = True

    def movingRight(self):
        self.moveRight = True

    def movingUp(self):
        self.moveUp = True

    def movingDown(self):
        self.moveDown = True

    def movingNotLeft(self):
        self.moveLeft = False

    def movingNotRight(self):
        self.moveRight = False

    def movingNotUp(self):
        self.moveUp = False

    def movingNotDown(self):
        self.moveDown = False

    def on_press(self, key, modifier):
        try:
            # print('alphanumeric key {0} pressed'.format(key.char))
            # switcher = {
            #     arcade.key.A: self.movingLeft(),
            #     arcade.key.S: self.movingDown(),
            #     arcade.key.D: self.movingRight,
            #     arcade.key.W: self.movingUp
            # }
            # print(switcher.get(self, key))

            if key == arcade.key.A:
                self.movingLeft()
            elif key == arcade.key.D:
                self.movingRight()
            if key == arcade.key.S:
                self.movingDown()
            elif key == arcade.key.W:
                self.movingUp()

        except AttributeError:
            print('special key {0} pressed'.format(key))

    def on_release(self, key, modifier):
        # switcher = {
        #     arcade.key.A: self.movingNotLeft(),
        #     arcade.key.S: self.movingNotDown(),
        #     arcade.key.D: self.movingNotRight(),
        #     arcade.key.W: self.movingNotUp()
        # }
        if key == arcade.key.A:
            self.movingNotLeft()
        elif key == arcade.key.D:
            self.movingNotRight()
        if key == arcade.key.S:
            self.movingNotDown()
        elif key == arcade.key.W:
            self.movingNotUp()