from update_velocity import update_velocity
import numpy as np


def test_1d_update():
    # creating test case
    current_velocity = np.array([0])
    acceleration = np.array([1])
    delta_t = 1

    # call the function to get a result
    result = update_velocity(current_velocity, acceleration, delta_t)

    assert result == np.array(
        [1]), "given a 1d problem, it should return the the velocity vector after a step delta_t"


def test_2d_update():
    # creating test case
    current_velocity = np.array([0, 1])
    acceleration = np.array([1, 2])
    delta_t = 1

    # call the function to get a result
    result = update_velocity(current_velocity, acceleration, delta_t)

    np.testing.assert_array_equal(result, np.array(
        [1, 3]), "given a 2d problem, it should return the the velocity vector after a step delta_t")
