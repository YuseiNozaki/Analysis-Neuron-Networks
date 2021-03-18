import numpy as np


def runge_kutta(func, x0, time):
    """
    This function uses RK4 to find solutions to equations for differential equations in any number of variables.

    Parameters
    ----------
    func : [f1, f2, ..., fn]; dxn/dt = fn(t, x); x = [x1, x2, ..., xn]

    x0 : [x1(t0), x2(t0), ..., xn(t0)]; initial value of parameters

    time : list of time

    Returns
    -------
    val : [x(t0), x(t1), x(t2), ..., x(tfin)]; shape(len(time), len(x))

    Requirement
    -----------
    Numpy
    """
    dt = time[1] - time[0]
    x = np.array(x0)
    val = []

    for t in time:
        val.append(x)

        k1 = np.array([f(t, x) for f in func])
        k2 = np.array([f(t+dt/2, x+dt*k1/2) for f in func])
        k3 = np.array([f(t+dt/2, x+dt*k2/2) for f in func])
        k4 = np.array([f(t+dt, x+dt*k3) for f in func])

        x = x + dt*(k1 + 2*k2 + 2*k3 + k4)/6

    return val
