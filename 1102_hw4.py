import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,1,1000,endpoint=False)
x1 = 3 * np.cos(2 * np.pi * 10 * t + np.pi/4)
x2 = 4 * np.cos(2 * np.pi * 10 * t + 3 * np.pi/4)
x3 = x1+x2
x4 = 5 * np.cos(2 * np.pi * 10 * t + 1.7127) # P 2-16 x4=x3

f, ax = plt.subplots(2,2,sharey="row",sharex="col",figsize=(10,7))

ax[0,0].plot(t,x1)
ax[0,0].set_ylim(-6,6)
ax[0,0].set_title("x1")
ax[0,0].set_xlabel("t(second)")
ax[0,0].set_ylabel("Amplitude")

ax[0,1].plot(t,x2)
ax[0,1].set_title("x2")
ax[0,1].set_xlabel("t(second)")
ax[0,1].set_ylabel("Amplitude")

ax[1,0].plot(t,x3)
ax[1,0].set_ylim(-6,6)
ax[1,0].set_title("x3=x1+x2")
ax[1,0].set_xlabel("t(second)")
ax[1,0].set_ylabel("Amplitude")

ax[1,1].plot(t,x4)
ax[1,1].set_title(r"x4=5*cos(2$\pi$*10t+1.7127)")
ax[1,1].set_xlabel("t(second)")
ax[1,1].set_ylabel("Amplitude")

plt.tight_layout()
plt.show()