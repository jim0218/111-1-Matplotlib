import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random

t = np.linspace(0,1,200,endpoint=False)
x1 = 30*np.cos(2*np.pi*5*t)
x2 = 10*np.cos(2*np.pi*5*t)

noise = random.normal(0,2,200)  #高斯雜訊(平均值,標準差,個數)

y1 = x1 + noise
y2 = x2 + noise

f, ax = plt.subplots(3,2,figsize=(10,9))

ax[0,0].plot(t,x1)
ax[0,0].set_title("x1=30cos(2*pi*5*t)")
ax[0,0].set_xlabel("t(second)")
ax[0,0].set_ylabel("Amplitude")

ax[0,1].plot(t,x2)
ax[0,1].set_title("x2=10cos(2*pi*5*t)")
ax[0,1].set_xlabel("t(second)")
ax[0,1].set_ylabel("Amplitude")

ax[1,0].plot(t,noise)
ax[1,0].set_title("noise")
ax[1,0].set_xlabel("t(second)")
ax[1,0].set_ylabel("Amplitude")
ax[1,0].set_ylim(-6,6)

ax[1,1].plot(t,noise)
ax[1,1].set_title("noise")
ax[1,1].set_xlabel("t(second)")
ax[1,1].set_ylabel("Amplitude")
ax[1,1].set_ylim(-6,6)

ax[2,0].plot(t,y1)
ax[2,0].set_title("y1=x1+noise")
ax[2,0].set_xlabel("t(second)")
ax[2,0].set_ylabel("Amplitude")
ax[2,0].set_ylim(-35,35)

ax[2,1].plot(t,y2)
ax[2,1].set_title("y2=x2+noise")
ax[2,1].set_xlabel("t(second)")
ax[2,1].set_ylabel("Amplitude")
ax[2,1].set_ylim(-15,15)

plt.tight_layout()
plt.show()