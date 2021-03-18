import numpy as np


def calc_psi(t, N, pulse_time):

    psi_list = []

    for i in range(N):
        psi = []

        for time in t:
            flag = 0

            for m in range(len(pulse_time[i])-1):
                if pulse_time[i][m] < time < pulse_time[i][m+1]:
                    psi.append(2*np.pi*m + 2*np.pi*(time-pulse_time[i][m])/(pulse_time[i][m+1]-pulse_time[i][m]))

                    flag = 1

                    break

            if flag == 0:
                psi.append(0)

        psi_list.append(psi)

    return psi_list


def calc_r(t, N, pulse_time):
    """
    Calculate the synchronization rate R(t).

    Parameters
    ----------
    t : list of time

    N : number of neurons

    pulse_time : list of time of pulse

    Returns
    -------
    r_list : list of R(t)
    """
    psi_list = calc_psi(t, N, pulse_time)

    r_list = []

    for t_n in range(len(t)):
        r = 0

        for i in range(N):
            r += np.exp(1j*psi_list[i][t_n])
        
        r_list.append(abs(r/N))

    return r_list
