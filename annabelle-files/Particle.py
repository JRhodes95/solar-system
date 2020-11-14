import math
import numpy as np
from scipy.spatial import distance


class Particle:
    def __init__(
        self,
        position=np.array([0, 0, 0], dtype=float),
        velocity=np.array([0, 0, 0], dtype=float),
        acceleration=np.array([0, -10, 0], dtype=float),
        name='Ball',
        mass=1.0,
        G=6.67408E-11
    ):

        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)
        self.name = name
        self.mass = mass
        self.G = G

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass, self.position, self.velocity, self.acceleration
        )

    def update(self, deltaT):
        deltaT = 6
        NextPosition = np.array(
            (self.position + (self.velocity * deltaT)), dtype=float)
        """Checking before  using acceleration"""
        print("="*80)
        print(self.velocity, deltaT, self.acceleration)
        print("="*80)
        NextVelocity = np.array(
            (self.velocity + (self.acceleration * deltaT)), dtype=float)
        self.position = NextPosition
        self.velocity = NextVelocity

    def updateGravitationalAcceleration(self, body):
        Y = distance.euclidean(self.position, body.position)
        X = body.position - self.position
        G = 6.67408E-11
        GravMass = G * body.mass * X
        is_all_zero = np.all((X == 0))
        if is_all_zero:
            print('Distance between bodies is 0')
        else:
            a = GravMass/Y**3
        self.acceleration = a
