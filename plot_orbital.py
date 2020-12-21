import matplotlib.pylab as plt
import numpy as np

r0 = 10
e = 1
t = np.array([i / 100 for i in range(4000)])
r = r0 + e * np.cos(4 / 3 * t)
theta = t

ax1 = plt.subplot(111, projection="polar")
ax1.plot(theta, r, color="black")
plt.xticks([])
plt.title("orbital")
plt.axis("off")
plt.savefig("orbital.pdf")
plt.show()