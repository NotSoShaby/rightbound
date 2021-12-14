import random
import time

START_TIME = 1639412439


def make_id():
    t = int(time.time() * 1000) - START_TIME
    u = random.SystemRandom().getrandbits(23)
    _id = (t << 23) | u
    return _id


def reverse_id(_id):
    t = _id >> 23
    return t + START_TIME

