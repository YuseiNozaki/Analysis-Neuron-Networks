from const import Cm, gl, gK, gNa, El, EK, ENa
from function.activation import alpha_n, alpha_m, alpha_h, beta_n, beta_m, beta_h


I = lambda t: 10
# I = lambda t: 10 if t<=40 or 90<=t<=91 else 5 if 40<t<60 else 0


def dVdt(t, x):
    V, n, m, h = x
    return (-gl*(V-El) - gK*(n**4)*(V-EK) - gNa*(m**3)*h*(V-ENa) + I(t)) / Cm

def dndt(t, x):
    V, n, m, h = x
    return alpha_n(V)*(1-n) - beta_n(V)*n

def dmdt(t, x):
    V, n, m, h = x
    return alpha_m(V)*(1-m) - beta_m(V)*m

def dhdt(t, x):
    V, n, m, h = x
    return alpha_h(V)*(1-h) - beta_h(V)*h


hodgkin_huxley = [dVdt, dndt, dmdt, dhdt]
