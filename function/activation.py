import numpy as np


alpha_n = lambda V: (0.01*V+0.55) / (1-np.exp(-0.1*V-5.5))

beta_n = lambda V: 0.125*np.exp((-V-65)/80)

alpha_m = lambda V: (0.1*V+4) / (1-np.exp(-0.1*V-4))

beta_m = lambda V: 4*np.exp((-V-65)/18)

alpha_h = lambda V: 0.07*np.exp((-V-65)/20)

beta_h = lambda V: 1 / (1+np.exp(-0.1*V-3.5))
