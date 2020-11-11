import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 10000)
y = 1/(3*np.pi) * (1 + np.cos(x)**2)
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("P(x)")
plt.title("Probability Density")
plt.show()


def Reject_S(samples):
    #samples can be derived in the function by the following code
    #we found it more efficient to move the code
    #N = 10**5
    #samples = []
    #for i in range(N):
        #x = np.random.uniform(0, 2*np.pi)
        #p = np.random.uniform(0, 2/(3*np.pi))
        #if p < 1/(3*np.pi) * (1 + np.cos(x)**2):
            #samples.append(x)
    lent = len(samples)
    n = np.random.randint(0, lent - 1)
    return samples[n]