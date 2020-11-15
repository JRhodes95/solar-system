import numpy as np


class Particle:
    """
    Class to model a particle in Earth's gravity
    """

    def __init__(
        self, name, mass, position=np.array([0, 0], dtype=float), velocity=np.array([0, 0], dtype=float),
    ):
        self.name = name
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.LOWER_G = -9.81
        self.acceleration = np.array([0, self.LOWER_G])

    def __str__(self):
        return "Particle: {0}, mass: {1:.3e}, position {2}, velocity {3}, acceleration {4}".format(
            self.name, self.mass, self.position, self.velocity, self.acceleration
        )

    def update(self, delta_t):
        next_position = self.position + self.velocity * delta_t
        self.position = next_position
        next_velocity = self.velocity + self.acceleration * delta_t
        self.velocity = next_velocity
