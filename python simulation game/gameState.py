import arcade
import math
import random
from sprites import Sprites
from rockMenu import RockMenu
from walkingInstructions import WalkingInstructions
from Res.rock import Rock
from Res.tree import Tree
from Res.farm import Farm
from Structures.townHall import TownHall
from Structures.house import House
from Structures.medPost import MedPost
from Res.worker import Worker
from coords import resMenu
from coords import townHallMenu
from coords import menuList

"""за големина на игралното поле имам проверката w update() + големината на екрана"""

"""Трябва да изчистя целия код много коментари и без магически числа"""

"""Работници които съм нз"""

"""Когато махам работници да се вадят от рес листа и когато създавам хора да се създават"""

"""Може да направиш веднага да се вдигне броя работници на рес че да може и веднага да се махне работника"""
"""Нещо става проблем при три рес вторите не събираха нямаше дисплей работници едновременно се освободиха всички работници"""


# noinspection PyUnresolvedReferences
class gameStateR:
    xBorder = 1300
    yBorder = 600
    x = 800 / 2 - 40
    y = 600 / 2 - 70
    xOffset = 0
    yOffset = 0
    keyboard = 0
    sprites = Sprites()

    time = 0
    timeCounter = 0

    # workers
    usedWorkers = 0
    maxWorkers = 10

    # object quantities
    rocksNumber = 0
    treesNumber = 300
    foodNumber = 100
    medicalSpots = 0

    # consumable
    foodForWorker = 50

    # object + screen objects sprites
    resourcesSprites = arcade.SpriteList(True, 128, False)
    buildingSprites = arcade.SpriteList(True, 128, False)
    staticSprites = arcade.SpriteList(True, 128, True)

    # object render con
    shouldRenderResMenu = False
    shouldRenderBuildList = False
    shouldRenderBuildingsList = False

    # list iter objects
    resourceList = []
    buildingList = []
    workersList = []
    walkingInstructions = []
    rockMenu = RockMenu()

    # current object of iter list
    resClicked = 0
    buildClicked = 0

    # textures of menus
    menu = 0
    townHallMenu = 0
    buildingsBuildingsList = 0
    bblList = []

    # hovering texture
    hoveringTexture = 0

    # render con hovering texture
    shouldRenderHoveringTexture = False

    # constant sizes
    menuWidth = 200
    menuHeight = 150
    scaleFactor = 2.5

    buildingLeft = 20
    buildingRight = 130
    buildingUp = 60
    buildingDown = 30

    townHallCoordsx = 400
    townHallCoordsy = 400

    """Разбий staticSprites на отделните групи спрайтове спрайтовете"""

    def __init__(self, keyboard):
        self.keyboard = keyboard
        self.createRes()
        self.menuTextures()

    def menuTextures(self):
        self.menu = arcade.Texture("menu", self.sprites.menu)
        self.townHallMenu = arcade.Texture("townHallMenu", self.sprites.townHallMenu)
        self.buildingsBuildingsList = arcade.Texture("buildingsBuildingsList", self.sprites.buildingsBuildingsList)

        self.bblList.append(arcade.Texture("farm", self.sprites.farm))
        self.bblList.append(arcade.Texture("house1", self.sprites.house))
        self.bblList.append(arcade.Texture("medPost1", self.sprites.medPost1))

    def createRes(self):
        # създаване на обектите
        rock1 = Rock(50, 600)
        rock2 = Rock(250, 600)
        rock3 = Rock(150, 600)
        rock4 = Rock(350, 600)

        tree1 = Tree(1200, 230)
        tree2 = Tree(1200, 280)
        tree3 = Tree(1200, 330)
        tree4 = Tree(1200, 380)

        townHall = TownHall(self.townHallCoordsx, self.townHallCoordsy)
        for i in range(self.maxWorkers):
            self.createWorker()

        # добавяне в iter list
        self.resourceList.append(rock1)
        self.resourceList.append(rock2)
        self.resourceList.append(rock3)
        self.resourceList.append(rock4)

        self.resourceList.append(tree1)
        self.resourceList.append(tree2)
        self.resourceList.append(tree3)
        self.resourceList.append(tree4)

        self.buildingList.append(townHall)

        # добавяне в spriteList
        self.resourcesSprites.append(rock1.sprite)
        self.resourcesSprites.append(rock2.sprite)
        self.resourcesSprites.append(rock3.sprite)
        self.resourcesSprites.append(rock4.sprite)

        self.resourcesSprites.append(tree4.sprite)
        self.resourcesSprites.append(tree3.sprite)
        self.resourcesSprites.append(tree2.sprite)
        self.resourcesSprites.append(tree1.sprite)

        self.buildingSprites.append(townHall.sprite)

        self.staticSprites.append(self.sprites.x2)
        self.staticSprites.append(self.sprites.y2)

    def createWorker(self):
        self.workersList.append(Worker(self.townHallCoordsx, self.townHallCoordsy))

    """Ако рисува менюто да не взима цъкване на нещо под него 
               или само за нещата които могат да се цъкнат"""  # ДА
    """Мога да имам два спрайта на координатите на плюсовите и минусите 
        ако менюто трябва да се рисува да провери и ако е над интерак да не гледа за другите масиви"""  # ДА

    def render(self):
        """Res draw"""
        self.resourcesSprites.draw()
        self.buildingSprites.draw()
        """Res draw"""

        """Worker draw"""
        for i in self.workersList:
            i.sprite.draw()
        """"""

        # горна лента
        arcade.draw_text(
            "Workers: " + str(self.usedWorkers) + " / " + str(self.maxWorkers) + " Wood: " + str(self.treesNumber) +
            " Rocks: " + str(self.rocksNumber) + " Food: " + str(self.foodNumber),
            0, 800, arcade.color.BLACK, 16, 0, "center", "Trebuchet", False, False, "left")

        # долна лента
        # първи обект
        arcade.draw_lrtb_rectangle_filled(self.buildingLeft, self.buildingRight, self.buildingUp, self.buildingDown,
                                          arcade.color.SMALT)
        arcade.draw_text("Buildings", self.buildingLeft, self.buildingDown, arcade.color.WHITE, 22, 0, "center",
                         "Cousine", False, False, "left")

        # проверка на render con
        if self.shouldRenderResMenu:
            self.menu.draw_scaled(self.menuWidth / 2 * self.scaleFactor, self.menuHeight / 2 * self.scaleFactor,
                                  self.scaleFactor)

            arcade.draw_text(str(self.resClicked.workers), 158 * self.scaleFactor, 20 * self.scaleFactor,
                             arcade.color.WHITE, 20, 0, "left",
                             "grg", False, False, "center")
            arcade.draw_text(str(self.resClicked.resources), 158 * self.scaleFactor, 45 * self.scaleFactor,
                             arcade.color.WHITE, 20, 0, "left",
                             "grg", False, False, "center")

        if self.shouldRenderBuildList:
            self.townHallMenu.draw_scaled(self.menuWidth / 2 * self.scaleFactor, self.menuHeight / 2 * self.scaleFactor,
                                          self.scaleFactor)

        if self.shouldRenderHoveringTexture:
            self.hoveringTexture.draw_scaled(self.x, self.y)

        if self.shouldRenderBuildingsList:
            self.buildingsBuildingsList.draw_scaled(300 / 2, 900 / 2)
            x = 0
            y = 900
            for i in self.bblList:
                i.draw_scaled(x + 50, y - 50)
                x += 100
                if x == 300:
                    x = 0
                    y -= 100

        pass

    def update(self, deltaTime):
        """conc updates"""
        self.time += deltaTime
        """conc updates"""

        """"""
        if self.xOffset > 0:
            if self.keyboard.moveLeft:
                self.xOffset -= 10
        if self.xOffset < 500:
            if self.keyboard.moveRight:
                self.xOffset += 10
        if self.yOffset > 0:
            if self.keyboard.moveDown:
                self.yOffset -= 10
        if self.yOffset < 700:
            if self.keyboard.moveUp:
                self.yOffset += 10

        for i in self.resourceList:
            i.sprite.set_position(i.x - self.xOffset,
                                  i.y - self.yOffset)
        for i in self.buildingList:
            i.sprite.set_position(i.x - self.xOffset,
                                  i.y - self.yOffset)
        for i in self.workersList:
            i.sprite.set_position(i.x - self.xOffset,
                                  i.y - self.yOffset)

        for inst in self.walkingInstructions:
            if inst.entity.x == inst.object.x and inst.entity.y == inst.object.y:
                self.resClicked.workers += 1
                self.usedWorkers += 1
                self.walkingInstructions.remove(inst)
            else:
                if inst.entity.x > inst.object.x:
                    inst.entity.x -= 1
                elif inst.entity.x < inst.object.x:
                    inst.entity.x += 1
                if inst.entity.y > inst.object.y:
                    inst.entity.y -= 1
                elif inst.entity.y < inst.object.y:
                    inst.entity.y += 1

        for i in self.workersList:

            """ako ima destinacia ili nqma"""
            if i.workplace != "":
                pass
            else:
                a = random.randint(1, 4)
                switcher = {
                    1: 1,
                    2: -1,
                    3: 0,
                    4: 0
                }

                switcher1 = {
                    1: 0,
                    2: 0,
                    3: 1,
                    4: -1
                }

                if i.x < self.townHallCoordsx + 200 or i.x > self.townHallCoordsx - 200:
                    i.x += switcher.get(a)
                if i.y < self.townHallCoordsy + 200 or i.y > self.townHallCoordsy - 200:
                    i.y += switcher1.get(a)

        if self.time >= 0.1:
            """Всяко нещо, което се прави десет пъти на секунда"""
            self.timeCounter += 1
            self.time = 0

        if self.timeCounter >= 10:
            self.timeCounter = 0
            """Всяко нещо, което се прави веднъж на секунда"""
            """Сериозен редезайн"""
            for i in self.resourceList:
                i.resources -= i.workers
                if i.type == "rock":
                    self.rocksNumber += i.workers
                elif i.type == "tree":
                    self.treesNumber += i.workers
                elif i.type == "farm":
                    self.foodNumber += i.workers

                """Когато свърши ресурса"""
                if i.resources <= 0:
                    """Направи код който тука да нулира workplace на съответните работници"""
                    self.usedWorkers -= i.workers
                    self.resourceList.remove(i)
                    self.resourcesSprites.remove(i.sprite)

                    """Da izchisti wsichki rabotnici koito imat rabota i"""

                    for worker in i.workersList:
                        worker.workplace = ""

                    """Възстановяване на негативните ресурси при надвишаване на лимита на ресурса"""
                    if i.type == "rock":
                        self.rocksNumber += i.resources
                    elif i.type == "tree":
                        self.treesNumber += i.resources
                    elif i.type == "farm":
                        self.foodNumber += i.resources

                    """Ако не отворен текущо ресурса няма нужда да се затваря менюто заради него"""
                    if i == self.resClicked:
                        self.shouldRenderResMenu = False
            pass

    def mouseClick(self, x, y, button):
        sad = True

        """При десен бутон прекратява слагането на избрана сграда от менюто със сгради"""
        if button == arcade.MOUSE_BUTTON_RIGHT:
            self.shouldRenderHoveringTexture = False
            self.hoveringTexture = 0
        # Всички обекти над игралната карта
        # print(arcade.get_sprites_at_point([x, y], self.resourcesSprites), "AA")

        elif self.shouldRenderHoveringTexture:
            """Слагане на нова сграда"""
            build = 0
            name = self.hoveringTexture.name

            collision = True

            tempSprite = arcade.Sprite(self.sprites.getLinkByName(self.hoveringTexture.name), center_x=x, center_y=y,
                                       hit_box_algorithm="Simple")
            """Проверка в списъците за дали на желаното място вече има обект"""
            if collision:
                for i in self.resourcesSprites:
                    if arcade.check_for_collision(tempSprite, i):
                        collision = False
                        break
            if collision:
                for i in self.buildingSprites:
                    if arcade.check_for_collision(tempSprite, i):
                        collision = False
                        break

            """Кода за какво става когато трябва да се сложи обекта и се създава обекта"""
            if collision:
                if name == "farm":
                    if self.treesNumber >= 5:
                        self.treesNumber -= 5
                        build = Farm(self.x, self.y)
                    else:
                        collision = False
                if name == "house1":
                    if self.treesNumber >= 20:
                        self.treesNumber -= 20
                        self.maxWorkers += 5
                        for i in range(5):
                            self.createWorker()
                        build = House(self.x, self.y)
                    else:
                        collision = False
                if name == "medPost1":
                    if self.treesNumber >= 10:
                        self.treesNumber -= 10
                        self.medicalSpots += 10
                        build = MedPost(self.x, self.y)
                    else:
                        collision = False

            """След като е създаден обекта за слагане се слага в листовете за обновяване и рисуване"""
            if collision:
                if build.cat == "res":
                    self.resourceList.append(build)
                    self.resourcesSprites.append(build.sprite)
                elif build.cat == "struc":
                    self.buildingList.append(build)
                    self.buildingSprites.append(build.sprite)

            sad = False

            """Ако съм отворил някой ресурс"""
        elif self.shouldRenderResMenu:
            """RES MENU"""
            # for i in range(len(self.staticSprites)):
            # if arcade.check_for_collision(self.sprites.cursorSprite, self.staticSprites[i]):
            if resMenu[0] < y < resMenu[1]:
                if resMenu[2] < x < resMenu[3]:
                    sad = False
                    if self.resClicked.workers > 0:
                        """Kod za zaqwka da se mahne ili sloji rabotnik"""
                        self.resClicked.workers -= 1
                        self.usedWorkers -= 1
                        self.resClicked.workersList[0].workplace = ""
                        self.resClicked.workersList.pop(0)
                elif resMenu[4] < x < resMenu[5]:
                    sad = False
                    if self.usedWorkers < self.maxWorkers:
                        for i in self.workersList:
                            if i.workplace == "":  # swoboden rabotnik
                                self.resClicked.workersList.append(i)
                                i.workplace = self.resClicked.type
                                self.walkingInstructions.append(WalkingInstructions(i, self.resClicked))

                                break
        # asd
        # Ако съм отворил някоя сграда
        elif self.shouldRenderBuildList:
            """Buildings MENU"""
            """Това няма как да работи ако добавя втора сграда"""
            for i in range(len(self.buildingList)):
                # if arcade.check_for_collision(self.sprites.cursorSprite, self.buildingSprites[i]):
                if self.buildingList[i].type == "townHall":
                    if townHallMenu[0] < x < townHallMenu[1] and townHallMenu[2] < y < townHallMenu[3]:
                        sad = False
                        if self.foodNumber > self.foodForWorker - 1:
                            self.createWorker()
                            self.maxWorkers += 1
                            self.foodNumber -= self.foodForWorker

        elif self.shouldRenderBuildingsList:
            buildClicked = math.ceil(x / 100) + (math.floor(9 - y / 100) * 3)

            if buildClicked <= len(self.bblList):
                name = self.bblList[buildClicked - 1].name

                self.shouldRenderHoveringTexture = True
                self.hoveringTexture = arcade.Texture(name, self.sprites.getImageByName(name))
            else:
                self.shouldRenderHoveringTexture = False
                self.hoveringTexture = 0
            sad = False

        """Дефиниращи дали ще се рисува"""

        """За сега ферми добавих къща"""
        """Бутони на долна лента"""
        if menuList[0] < x < menuList[1] and menuList[2] < y < menuList[3]:
            self.shouldRenderBuildingsList = True
            sad = False
        else:
            self.shouldRenderBuildingsList = False

        """Всички обекти на картата като ресурси, сгради, (хора и врагове) """
        if sad:
            for i in self.resourceList:
                if arcade.check_for_collision(self.sprites.cursorSprite, i.sprite):
                    self.resClicked = i
                    self.rockMenu.setCurrentRock(i)
                    self.shouldRenderResMenu = True
                    sad = False
                    break
                else:
                    self.shouldRenderResMenu = False
                    # self.resClicked = 0
        if sad:
            for i in self.buildingList:
                if i.type == "townHall":
                    if arcade.check_for_collision(self.sprites.cursorSprite, i.sprite):
                        self.buildClicked = i
                        self.shouldRenderBuildList = True
                        break
                    else:
                        self.shouldRenderBuildList = False

    def updateMouse(self, x, y):
        self.sprites.cursorSprite.set_position(x, y)
        self.x = x
        self.y = y

    def draw_pine_tree(self):
        # Draw the triangle on top of the trunk
        arcade.draw_triangle_filled(
            self.x + 40, self.y + 100, self.x, self.y + 40, self.x + 80, self.y + 40, arcade.color.DARK_GREEN)

        # Draw the trunk
        arcade.draw_lrtb_rectangle_filled(
            self.x + 30, self.x + 50, self.y + 40, self.y, arcade.color.DARK_BROWN)

    def drawPines(self, x, y):
        arcade.draw_triangle_filled(
            x + 40 - self.xOffset, y + 100 - self.yOffset, x - self.xOffset, y + 40 - self.yOffset,
            x + 80 - self.xOffset, y + 40 - self.yOffset, arcade.color.DARK_GREEN)

        # Draw the trunk
        arcade.draw_lrtb_rectangle_filled(
            x + 30 - self.xOffset, x + 50 - self.xOffset, y + 40 - self.yOffset, y - self.yOffset,
            arcade.color.DARK_BROWN)

    def drawBorders(self):
        # Down border 0 do 1300
        # thickness = 200

        # arcade.draw_rectangle_filled(self.xBorder / 2 - self.xOffset, thickness / 2 - self.yOffset, self.xBorder,
        #                              thickness, arcade.color.GOLD)
        arcade.draw_lrtb_rectangle_filled(0 - self.xOffset, self.xBorder - self.xOffset, 0 - self.yOffset,
                                          -200 - self.yOffset, arcade.color.GOLD)
