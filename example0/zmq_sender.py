#!/usr/bin/env python

import json
import math
import time
import zmq


def GymObservation(low, high, value):
    """Converts value in range low high to the format of a GymObservation.

    """
    return [{'min': low, 'max': high, 'value': value, 'ts': time.time()}]


ctx = zmq.Context()

pub = ctx.socket(zmq.PUB)
pub.bind('tcp://*:5556')

t_max = 10.
t = 0
dt = 0.01

print('start sending')

while t < t_max:
    msg = json.dumps(GymObservation(-1., 1., math.sin(2 * math.pi * t)))
    pub.send(msg.encode())
    time.sleep(dt)

    t += dt

print('stop sending')