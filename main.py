import matplotlib.pyplot as plt

import neuron_network


p1, r1 = neuron_network.main(10, False)
p2, r2 = neuron_network.main(10, True)


plt.figure()
plt.xlabel('probability of connection')
plt.ylabel('avarage of synchronisation order')
plt.plot(p1, r1, color='b')
plt.plot(p2, r2, color='r')

plt.show()
