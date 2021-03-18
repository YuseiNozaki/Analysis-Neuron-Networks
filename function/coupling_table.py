import numpy as np


def coupling_table(N, p):
    """
    This function generates a table of coupling strengths.

    Parameters
    ----------
    N : number of neurons

    p : propability of generate coupling; 0<=p<=1

    Returns
    -------
    epsilon : shape(N, N); epsilon[i][j] is coupling strength of j -> i

    Requirement
    -----------
    Numpy
    """

    epsilon = np.zeros((N, N))

    for i in range(N):
        for j in range(i, N):
            if i == j:
                epsilon[i][j] = 0
                epsilon[j][i] = 0

            else:
                if np.random.rand() <= p:
                    if np.random.randint(0, 2) == 0:
                        epsilon[i][j] = np.random.normal(0.1, 0.02)
                        epsilon[j][i] = 0
                
                    else:
                        epsilon[i][j] = 0
                        epsilon[j][i] = np.random.normal(0.1, 0.02)

                else:
                    epsilon[i][j] = 0
                    epsilon[j][i] = 0
    
    return epsilon
