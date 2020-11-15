from update_velocity import update_velocity
import numpy as np


def test_1d_update():
    current_velocity = np.array([0])
    acceleration = np.array([1])
    delta_t = 1

    result = update_velocity(current_velocity, acceleration, delta_t)
    #  should be [1]

    assert result == np.array(
        [1]), "given a 1d problem, it should return the the velocity vector after a step delta_t"


def test_2d_update():
    current_velocity = np.array([0, 0])
    acceleration = np.array([1, 1])
    delta_t = 1

    result = update_velocity(current_velocity, acceleration, delta_t)
    #  should be [1, 1]

    np.testing.assert_array_equal(result, [
        1, 1]), "given a 2d problem, it should return the the velocity vector after a step delta_t"
