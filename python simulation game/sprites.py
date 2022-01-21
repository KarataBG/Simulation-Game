import arcade
from Res import rock
from PIL import Image


class Sprites:
    # coords = [300, -200 / 2, -200 / 2, 600, 600, 1300 * 1 + 200 / 2, 1300 * 2 + 200 / 2, 600]
    # spriteWall = arcade.Sprite("images/border1300x200.png", center_x=100, center_y=100)
    # spriteWall1 = arcade.Sprite("images/border1300x200.png", center_x=100, center_y=100)
    # spriteWall2 = arcade.Sprite("images/border1300x200.png", center_x=100, center_y=100)
    # spriteWall3 = arcade.Sprite("images/border1300x200.png", center_x=100, center_y=100)

    x2 = arcade.SpriteCircle(12, arcade.color.AO, False)
    y2 = arcade.SpriteCircle(12, arcade.color.AO, False)
    # yy = arcade.SpriteSolidColor()

    x2.set_position(131 * 2.3, 26 * 2.3)
    y2.set_position(186 * 2.3, 26 * 2.3)

    #
    # rockCoords = [50, 1250]
    # spriteRock = arcade.Sprite("images/rock.png", center_x=50, center_y=1250, hit_box_algorithm="Simple")

    # rock1 = rock.Rock(50, 1250)
    #

    # resourcesSprites = arcade.SpriteList(True, 128, False)
    # resourcesSprites.append(rock1.spriteRock)

    # playerCoords = []
    # player = arcade.Sprite("images/player.png")

    # wallsSprites = arcade.SpriteList(True, 128, False)
    # wallsSprites.append(spriteWall)
    # wallsSprites.append(spriteWall1)
    # wallsSprites.append(spriteWall2)
    # wallsSprites.append(spriteWall3)

    # spriteWall1.turn_left(90)
    # spriteWall3.turn_right(90)

    # numbers = [
    #     arcade.Texture("num0", Image.open("images/0.png")),
    #     arcade.Texture("num1", Image.open("images/1.png")),
    #     arcade.Texture("num2", Image.open("images/2.png")),
    #     arcade.Texture("num3", Image.open("images/3.png")),
    #     arcade.Texture("num4", Image.open("images/4.png")),
    #     arcade.Texture("num5", Image.open("images/5.png")),
    #     arcade.Texture("num6", Image.open("images/6.png")),
    #     arcade.Texture("num7", Image.open("images/7.png")),
    #     arcade.Texture("num8", Image.open("images/7.png")),
    #     arcade.Texture("num9", Image.open("images/9.png"))]

    # num2 = Image.open("images/2.png")
    # num3 = Image.open("images/3.png")
    # num4 = Image.open("images/4.png")
    # num5 = Image.open("images/5.png")
    # num6 = Image.open("images/6.png")
    # num7 = Image.open("images/7.png")
    # num8 = Image.open("images/8.png")
    # num9 = Image.open("images/9.png")

    menu = Image.open("images/menu.png")
    townHallMenu = Image.open("images/townHallMenu.png")
    buildingsBuildingsList = Image.open("images/buildingsBuildingsListMenu.png")

    """Buildings buildings list"""
    farm = Image.open("images/farm.png")
    house1 = Image.open("images/house1.png")
    house = Image.open("images/house.png")
    medPost1 = Image.open("images/medPost.png")
    medPost = Image.open("images/medPost1.png")


    # minus = Image.open("images/border100x200.png")

    # color = (0, 0, 0, 100)

    cursorSprite = arcade.SpriteCircle(10, arcade.color.AO, False)

    @staticmethod
    def getImageByName(name):
        return Image.open("images/" + name + ".png")

    @staticmethod
    def getLinkByName(name):
        return "images/" + name + ".png"
