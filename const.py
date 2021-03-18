import numpy as np


t_init = 0
t_fin = 100
dt = 0.01
t = np.arange(t_init, t_fin, dt)

Cm = 1

gl = 0.3
gK = 36
gNa = 120

El = -54.4
EK = -77
ENa = 50
Esyn = 0

V0 = -65
n0 = 0.32
m0 = 0.05
h0 = 0.6
s0 = 0.1

N = 100
ommega = 1
Vr = 20
