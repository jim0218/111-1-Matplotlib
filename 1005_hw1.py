import matplotlib.pyplot as plt
import numpy as np
t=np.arange(0., 5., 0.2)
print("t= " + str(t))
# t= [ 0. 0.2 0.4 0.6 0.8 1. 1.2 1.4 1.6 1.8 2. 2.2 2.4 2.6 2.8 3. 3.2 3.4 3.6 3.8 4. # 4.2 4.4 4.6 4.8]
plt.plot(t, t, 'r--', t, t**2, 'gs', t, t**3, 'b^')
plt.legend(["t","t**2","t**3"],loc="upper left")
plt.xlabel('x')
plt.ylabel('y')
plt.title("t,t**2,t**3")
plt.show()