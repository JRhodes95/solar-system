def update_velocity(current_velocity, acceleration, delta_t):
    next_velocity = current_velocity + acceleration * delta_t
    return next_velocity
