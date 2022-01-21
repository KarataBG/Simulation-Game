
import arcade


class WalkingInstructions:

    def __init__(self, entity, destination):
        self.entity = entity
        self.object = destination
        self.entityX = entity.x
        self.entityY = entity.y
        self.objectX = destination.y
        self.objectY = destination.y

    # entity = 0
    entityX = 0
    entityY = 0

    # object = 0
    objectX = 0
    objectY = 0
