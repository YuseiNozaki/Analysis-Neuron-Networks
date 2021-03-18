def convert_pulse_time(V, t):
    """
    Convert the list of V to a list of pulse time.

    Parameters
    ----------
    V : shape(N, t); N is number of neuron.

    t : list of time

    Returns
    -------
    pulse_time : list of pulse time
    """

    pulse_time = [t[i+1] for i in range(len(V)-1) if V[i] < 0 and 0 <= V[i+1]]

    return pulse_time
