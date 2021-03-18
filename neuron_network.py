import sys, os
sys.path.append(os.pardir)

import numpy as np

from tqdm import tqdm

from function.activation import alpha_n, alpha_m, alpha_h, beta_n, beta_m, beta_h
from const import *
from function.coupling_table import coupling_table
from function.convert_pulse_time import convert_pulse_time
from function.calc_r import calc_r


def main(gamma, plasticity):
    """
    gamma : int
    plasticity : bool
    """

    r_ave_list = []

    p_list = np.arange(0, 1.1, 0.1)

    for p in p_list:

        epsilon = coupling_table(N, p)


        V, n, m, h, s = [], [], [], [], []


        for i in range(N):
            V.append([V0])
            n.append([n0])
            m.append([m0])
            h.append([h0])
            s.append([s0])

        I = []
        for i in range(N):
            I.append(np.random.rand() + 9)

        last_puls_time = np.zeros(N)

        for time in tqdm(range(len(t)-1)):
            for i in range(N):
                Il = gl*(V[i][time]-El)
                IK = gK*(n[i][time]**4)*(V[i][time]-EK)
                INa = gNa*(m[i][time]**3)*h[i][time]*(V[i][time]-ENa)
                connect = sum([epsilon[i][j]*s[j][time] for j in range(N)]) * (Vr-V[i][time])/ommega
                #gamma = 0 if np.random.rand() > (time%1400)/1400 else gamma
                gamma = 0 if np.random.rand() > 0.01/14 else gamma

                V[i].append(V[i][time] + ((-Il - IK - INa + I[i] + connect + gamma)/Cm) * dt)
                n[i].append(n[i][time] + (alpha_n(V[i][time])*(1-n[i][time]) - beta_n(V[i][time])*n[i][time]) * dt)
                m[i].append(m[i][time] + (alpha_m(V[i][time])*(1-m[i][time]) - beta_m(V[i][time])*m[i][time]) * dt)
                h[i].append(h[i][time] + (alpha_h(V[i][time])*(1-h[i][time]) - beta_h(V[i][time])*h[i][time]) * dt)
                s[i].append(s[i][time] + (5*(1-s[i][time])/(1+np.exp(-(V[i][time]+3)/8)) - s[i][time]) * dt)

                if plasticity:
                    if V[i][-2] < 0 < V[i][-1]:
                        last_puls_time[i] = time/0.01

                    for j in range(N):
                        if epsilon[i][j] != 0:
                            delta_t = last_puls_time[i] - last_puls_time[j]

                            if delta_t >= 0:
                                delta_epsilon = np.exp(-delta_t/1.8)
                            if delta_t < 0:
                                delta_epsilon = -0.5*np.exp(delta_t/6)

                            epsilon[i][j] += 0.001 * delta_epsilon


        puls_time = [convert_pulse_time(i, t) for i in V]

        r_list = calc_r(t, N, puls_time)

        r_ave = sum(r_list)/len(r_list)

        r_ave_list.append(r_ave)


    return p_list, r_ave_list
