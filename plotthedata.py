__author__ = 'BisharaKorkor'

import numpy as np
import matplotlib.pyplot as plt
import funcfitter as ff
from random import uniform
from math import pi


data = np.genfromtxt("100x.csv", delimiter=',')

time = [i[0] for i in data]
value = [i[1] for i in data]

box = 10

bcvalue = [np.mean(value[i:i+box]) for i in range(len(value)-box)]
timeforbc = [i+box-1 for i in range(len(data)-box)]

frontmodels = []

for i in range(10000):
    frontmodels += [ff.fitter(timeforbc[0:600], bcvalue[0:600], m=uniform(1., 6.), y0=uniform(7000., 8500.),
                              amp=uniform(200., 750.), omega=uniform(2. * pi / 50., 2. * pi / 150.),
                              phi=uniform(0, 2*pi))]

frontbestfit = frontmodels[0]

for i in frontmodels:
    if i[0] < frontbestfit[0]:
        frontbestfit = i

backmodels = []

for i in range(10000):
    backmodels += [ff.fitter(timeforbc[601:998], bcvalue[601:998], m=uniform(-1., -6.), y0=uniform(7000., 13000.),
                             amp=uniform(200., 750.), omega=uniform(2. * pi / 50., 2. * pi / 150.), phi=uniform(0, 2*pi))]

backbestfit = backmodels[0]
for i in backmodels:
    if i[0] < backbestfit[0]:
        backbestfit = i

print ff.linearplussine(1200., backbestfit[1], backbestfit[2], backbestfit[3], backbestfit[4], backbestfit[5])

plt.plot(timeforbc, bcvalue)
plt.plot(timeforbc[0:600], [ff.linearplussine(i, frontbestfit[1], frontbestfit[2], frontbestfit[3], frontbestfit[4],
                                              frontbestfit[5]) for i in timeforbc[0:600]])
plt.plot(timeforbc[601:998], [ff.linearplussine(i, backbestfit[1], backbestfit[2], backbestfit[3], backbestfit[4],
                                              backbestfit[5]) for i in timeforbc[601:998]])
# plt.plot(time, value)

plt.show()
