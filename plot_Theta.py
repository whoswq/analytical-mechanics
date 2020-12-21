import numpy as np
from scipy import integrate
import matplotlib.pylab as plt

r0 = np.array([i / 1000 for i in range(5000)])
s = np.sqrt(r0**2 - r0**2 / (1.2 * (1 + r0)))


def phi(u, r0, s):
    return 2 * s * (1 / np.sqrt((1 - u / (1.2 *
                                          (u + r0))) * r0**2 - s**2 * u**2))


theta = []
cnt = 0
for r0_, s_ in zip(r0, s):
    theta_ = np.pi - integrate.quad(phi, 0, 1, args=(r0_, s_))[0]
    theta.append(theta_)
    cnt += 1

dd = []
for i in range(4999):
    dd_ = np.abs((s[i + 1] - s[i]) / (theta[i + 1] - theta[i]))
    dd.append(s[i + 1] / np.sin(theta[i + 1]) * dd_)

plt.plot(theta[1:254] + theta[258:], dd[:253] + dd[257:], color="black")
plt.xlabel("Theta")
plt.ylabel("sigma")
plt.savefig("differential.pdf")
plt.show()
