import numpy as np
from models.Particle import Particle


cannonball = Particle(
    'cannonball', 3, velocity=np.array([10, 5, 3], dtype=float), position=np.array([0, 0, 0], dtype=float))


delta_t = 0.01


while (cannonball.position[2] >= 0):
    cannonball.update(delta_t, "EULER")
    print(cannonball)

summary = '{0} travelled {1}m.'.format(cannonball.name, cannonball.position[0])
print(summary)
