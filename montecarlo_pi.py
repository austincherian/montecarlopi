import random
import math

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

counts= 1000000

in_circ= 0
in_sq= 0

for i in range(0 ,  counts):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)

        sqdistorg = math.sqrt(x**2 + y**2)

        if sqdistorg < 1:
                in_circ+=1
        in_sq+=1
        pi = (float(in_circ)/ in_sq) * 4

print "estimated vlaue of Pi = %.10f" % (pi)
