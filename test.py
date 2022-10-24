from physics_object_class import PhysicsObject
import numpy as np

wheel = PhysicsObject(np.array([0,0]),np.array([20,0]),5)

for i in range(0,20):
    wheel.physicsTimestep(0.05)
    wheel.applyTimestep()
    print(wheel.position)