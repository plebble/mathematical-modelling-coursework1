from turtle import position
import numpy as np

class PhysicsObject:
    
    force = np.array([0.0,9.81])

    def __init__(self, position, velocity, mass):
        self.position = position
        self.velocity = velocity
        self.mass = mass

    def physicsTimestep(self,timestep=0.05):
        
        # use a = F/m in order to figure out how much it should accelerate.
        acceleration = self.force / self.mass

        # calculate all the new velocities/positions first, and then update them after.
        # this is to stop objects from having their timesteps calculated based on objects in the future.

        self.new_velocity = self.velocity + (acceleration * timestep) # this could probably be done better with trapesium

        self.new_position = self.position + (self.new_velocity * timestep)

    def applyTimestep(self):
        self.position = np.copy(self.new_position)
        self.velocity = np.copy(self.new_velocity)

    
