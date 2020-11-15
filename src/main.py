import numpy as np
from models.Particle import Particle


cannonball = Particle(
    'cannonball', 3, velocity=np.array([10, 5], dtype=float))

print(cannonball)

delta_t = 0.01

cannonball.update(delta_t)

while (cannonball.position[1] > 0):
    cannonball.update(delta_t)
    print(cannonball)

summary = '{0} travelled {1}m.'.format(cannonball.name, cannonball.position[0])
print(summary)
