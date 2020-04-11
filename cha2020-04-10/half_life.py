from math import log

def half_life(initial, remaining, time):
    return time/log(remaining/initial, 0.5)
