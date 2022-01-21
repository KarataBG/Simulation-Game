import arcade

import gameState
import keyboard

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

keys = keyboard.Keyboard()
currentState = gameState.gameStateR(keys)
currentMenu = 0


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.LIGHT_BLUE)

    def setup(self):
        # Set up your game here
        pass

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # BEGIN

        if currentState != 0:
            currentState.render()

        # print(currentMenu)

        # rockMenuR.render()

        # print(RockMenu.)

        # END
        arcade.finish_render()

    def update(self, delta_time):
        currentState.update(delta_time)

        pass

    def on_key_press(self, symbol: int, modifiers: int):
        keys.on_press(symbol, modifiers)

    def on_key_release(self, symbol: int, modifiers: int):
        keys.on_release(symbol, modifiers)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        currentState.mouseClick(x, y, button)
        pass

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        currentState.updateMouse(x, y)
        pass


""" може Всеки стадии да си има свои контролери за мишка и клавиатура """


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
