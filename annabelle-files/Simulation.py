import numpy as np
from Particle import Particle

earthMass = 5.97237e24     # https://en.wikipedia.org/wiki/Earth
earthRadius = 63710 * 1e3  # https://en.wikipedia.org/wiki/Earth
Earth = Particle(
    position=np.array([0, 0, 0], dtype=float),
    velocity=np.array([0, 0, 0], dtype=float),
    acceleration=np.array([0, 0, 0], dtype=float),
    name="Earth",
    mass=earthMass
)
satPosition = earthRadius + (35786 * 1e3)
# from centrifugal force = gravitational force
satVelocity = np.sqrt(Earth.G * Earth.mass / satPosition)
Satellite = Particle(
    position=np.array([satPosition, 0, 0], dtype=float),
    velocity=np.array([0, satVelocity, 0], dtype=float),
    acceleration=np.array([0, 0, 0], dtype=float),
    name="Satellite",
    mass=100.
)

for n in range(0, 2000):
    Satellite.updateGravitationalAcceleration(Earth)
    Earth.updateGravitationalAcceleration(Satellite)
    Earth.update(6)
    Satellite.update(6)

print(
    "The Earth and Satellites Location after {0} seconds is:".format((2000*6)))
for particle in [Earth, Satellite]:
    print("  Particle: {}".format(particle.name))
    print("    Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("    {}: {}".format(attribute, particle.__getattribute__(
            attribute) + 0.0))  # add 0.0 to avoid negative zeros!
