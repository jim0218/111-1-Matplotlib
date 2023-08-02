import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,1,1000,endpoint=False)
r = 1 *np.cos (2 * np.pi * 2 * t)

f, ax = plt.subplots(1,3,sharey="row")

ax[0].plot(t,r)
ax[0].set_title("cos(4" + r'$\pi$'+"t)" )
ax[0].set_xlabel("t(second)")
ax[0].set_ylabel("Amplitude")

ax[1].plot(t,r*2)
ax[1].set_title("2cos(4"+ r'$\pi$'+"t)")
ax[1].set_xlabel("t(second)")
ax[1].set_ylabel("Amplitude")

ax[2].plot(t,r*4)
ax[2].set_title("4cos(4"+ r'$\pi$'+"t)")
ax[2].set_xlabel("t(second)")
ax[2].set_ylabel("Amplitude")

plt.show()


#---------------------------

t = np.linspace(0,1,1000,endpoint=False)
r = 1 *np.cos (2 * np.pi * 2 * t)

f, ax = plt.subplots(1,3,sharey="row",figsize=(15,4))

ax[0].plot(t,r)
ax[0].set_title("cos(4" + r'$\pi$'+"t)")
ax[0].set_xlabel("t(second)")
ax[0].set_ylabel("Amplitude")
ax[0].axhline(0,linestyle="--",color="k")

ax[1].plot(t,r*2)
ax[1].set_title("2cos(4"+ r'$\pi$'+"t)")
ax[1].set_xlabel("t(second)")
ax[1].set_ylabel("Amplitude")
ax[1].axhline(0,linestyle="--",color="k")

ax[2].plot(t,r*4)
ax[2].set_title("4cos(4"+ r'$\pi$'+"t)")
ax[2].set_xlabel("t(second)")
ax[2].set_ylabel("Amplitude")
ax[2].axhline(0,linestyle="--",color="k")

plt.show()