import numpy as np
from models.Particle import Particle

# Create a particle to model a cannonball
cannonball = Particle(
    'cannonball', 3, velocity=np.array([10, 5, 3], dtype=float), position=np.array([0, 0, 0], dtype=float))

# Set delta_t to 0.01 seconds for Euler approximations
delta_t = 0.01

# create a list to record position over time
trajectory = [cannonball.position]

# run the simulation
while (cannonball.position[2] >= 0):
    cannonball.update(delta_t, "EULER")
    trajectory.append(cannonball.position)


summary = '{0} travelled {1}m.'.format(cannonball.name, cannonball.position[0])

print(summary)
print('Attempting to write to file')

file_contents = np.asarray(trajectory)
np.savetxt('trajectory.csv', file_contents, delimiter=',')

print('File saved successfully')
