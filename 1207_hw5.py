import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random
t = np.linspace(0,1,200,endpoint=False)
x = 10*np.cos(2*np.pi*5*t)

a = int(input("請輸入雜訊振福大小:"))
p = int(input("請輸入雜訊比例:"))

# a = 6
# p = 5

noise = np.zeros(x.size)

for i in range(x.size):
  p1 = random.uniform(0,1)
  if p1 <= p/100 :
    p2=random.uniform(0,1)
    if p2<0.5:
      noise[i]= a
    else:
      noise[i]= -a


u_noise = np.zeros(x.size)
for i in range(x.size):
  p1 = random.uniform(0,1)
  if p1 <= p/100 :
    u_noise[i] = random.uniform(-a,a,1)

y1 = x+u_noise
y2 = x+noise

f, ax = plt.subplots(3,2,figsize=(10,8))

ax[0,0].plot(t,x)
ax[0,0].set_title("x")
ax[0,0].set_xlabel("t(second)")
ax[0,0].set_ylabel("Amplitude")

ax[1,0].plot(t,u_noise)
ax[1,0].set_title("uniform_noise")
ax[1,0].set_xlabel("t(second)")
ax[1,0].set_ylabel("Amplitude")
ax[1,0].set_ylim(-a,a)

ax[1,1].plot(t,noise)
ax[1,1].set_title("noise")
ax[1,1].set_xlabel("t(second)")
ax[1,1].set_ylabel("Amplitude")
ax[1,1].set_ylim(-a,a)

ax[2,0].plot(t,y1)
ax[2,0].set_title("y1=x+uniform_noise")
ax[2,0].set_xlabel("t(second)")
ax[2,0].set_ylabel("Amplitude")

ax[2,1].plot(t,y2)
ax[2,1].set_title("y2=x+noise")
ax[2,1].set_xlabel("t(second)")
ax[2,1].set_ylabel("Amplitude")
ax[2,1].set_ylim(-15,15)

plt.tight_layout()
plt.show()