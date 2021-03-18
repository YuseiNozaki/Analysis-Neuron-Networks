import numpy as np
import matplotlib.pyplot as plt

from const import V0, n0, m0, h0
from function.hodgkin_huxley import hodgkin_huxley, I
from function.runge_kutta import runge_kutta


time = np.arange(0, 100, 0.01)

x0 = [V0, n0, m0, h0]

val = runge_kutta(hodgkin_huxley, x0, time)

V = [v[0] for v in val]
n = [v[1] for v in val]
m = [v[2] for v in val]
h = [v[3] for v in val]


plt.figure()
plt.plot(time, [I(t) for t in time])
plt.xlabel('time')
plt.ylabel('input current')

plt.figure()
plt.plot(time, V)
plt.xlabel('time')
plt.ylabel('membrane potential')

plt.figure()
plt.plot(time, n, label='n')
plt.plot(time, m, label='m')
plt.plot(time, h, label='h')
plt.xlabel('time')
plt.ylabel('gate')
plt.legend()

plt.show()
