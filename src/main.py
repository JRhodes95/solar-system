import numpy as np
from models.Particle import Particle


cannonball = Particle('cannonball', 10, velocity=np.array([3, 5], dtype=float))

print(cannonball)

delta_t = 0.01

cannonball.update(delta_t)

while (cannonball.position[1] > 0):
    cannonball.update(delta_t)
    print(cannonball)
