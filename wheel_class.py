from physics_object_class import PhysicsObject

class Wheel(PhysicsObject):

    def __init__(self, position, velocity, mass, ground):
        super().__init__(position, velocity, mass)
        self.ground = ground

    # when calculating physics, should check where the ground is and calculate the reaction force