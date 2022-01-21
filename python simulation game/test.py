import arcade
import Res.rock
from Res import rock


class Shark:
    # Class variables
    abg = "A"
    animal_type = "fish"
    location = "ocean"
    x = 0
    y = 0
    sp = arcade.Sprite("images/rock.png", center_x=x, center_y=y, hit_box_algorithm="Simple")
    rock1 = rock.Rock(50, 600)

    # Constructor method with instance variables name and age
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.sp = arcade.Sprite("images/rock.png", center_x=x, center_y=y, hit_box_algorithm="Simple")

    # Method with instance variable followers
    def set_followers(self, followers):
        print("This user has " + str(followers) + " followers")


def main():
    # First object, set up instance variables of constructor method

    sammy = Shark(5, 5)
    stevie = Shark(88, 8)

    print(sammy.rock1)
    print(sammy.rock1.workers)
    print(stevie.rock1)
    print(stevie.rock1.workers)

    stevie.rock1.workers = "70"

    print(sammy.rock1)
    print(sammy.rock1.workers)
    print(stevie.rock1)
    print(stevie.rock1.workers)

    # stevie.sp =
    # print(sammy.sp)
    # print(stevie.sp)


if __name__ == "__main__":
    main()
