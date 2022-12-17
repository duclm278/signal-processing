import matplotlib.pyplot as plt
import numpy as np

a = 0.87
x = np.linspace(0, 2, 256)
w = x * np.pi
h = 1 / (1 - a * np.exp(1j * -w))
plt.grid(True)
plt.xticks(np.arange(0, 2.5, 0.5))
plt.yticks(np.arange(0, 10, 2))
plt.xlabel("frequency in units of pi")
plt.ylabel("$|H(e^{i \omega})|$" ,rotation=0)
plt.title("Magnitude Part, a = 0.87")
plt.plot(x, abs(h))

plt.show()
