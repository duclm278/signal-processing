import matplotlib.pyplot as plt
import numpy as np

plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.5,
                    hspace=0.5)

# Unit Sequence
x1 = np.arange(-5, 5)
y1 = np.zeros(10)
y1[5] = 1
plt.subplot(2, 2, 1)
plt.grid(True)
plt.xticks(x1)
plt.xlabel("n")
plt.title("Unit Sequence")
plt.stem(x1, y1)

# Unit Step Sequence
x2 = np.arange(-5, 5)
y2 = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
plt.subplot(2, 2, 2)
plt.grid(True)
plt.xticks(x2)
plt.xlabel("n")
plt.title("Unit Step Sequence")
plt.stem(x2, y2)

# Exponential Sequence
x3 = np.arange(-5, 5)
y3 = np.array(0.7 ** x3)
plt.subplot(2, 2, 3)
plt.grid(True)
plt.xticks(x3)
plt.xlabel("n")
plt.title("Exponential Sequence")
plt.stem(x3, y3)

# Sinusoidal Sequence
x4 = np.arange(-10, 10)
y4 = np.array(np.sin(x4))
plt.subplot(2, 2, 4)
plt.grid(True)
plt.xticks(x4)
plt.xlabel("n")
plt.title("Sinusoidal Sequence")
plt.stem(x4, y4)

plt.show()
