#第二批 第一題
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random
t = np.linspace(0,1,1000,endpoint=False)
x1 = 2 * np.cos (2 * np.pi * 5 * t)  #原始訊號 x1
x2 = 2 * np.cos (2 * np.pi * 10 * t)  #原始訊號 x2
x3 = 2 * np.cos (2 * np.pi * 15 * t)  #原始訊號 x3
x4 = x1+x2+x3               #訊號  x4 = x1+x2+x3

f, ax = plt.subplots(4,1,figsize=(10,11))

#圖一
ax[0].plot(t, x1 , color="yellow")  #畫圖 x1 顏色=黃色 
ax[0].set_xlabel('x')          #X軸標籤
ax[0].set_ylabel('y')          #Y軸標籤   
ax[0].set_title("x1")          #標題Title

#圖二
ax[1].plot(t, x2 , color="green")  #畫圖 x2 顏色=綠色 
ax[1].set_xlabel('x')          #X軸標籤
ax[1].set_ylabel('y')          #Y軸標籤   
ax[1].set_title("x2")          #標題Title

#圖三
ax[2].plot(t, x3 , color="blue")  #畫圖 x3 顏色=藍色
ax[2].set_xlabel('x')          #X軸標籤
ax[2].set_ylabel('y')          #Y軸標籤   
ax[2].set_title("x3")          #標題Title

#圖四
ax[3].plot(t, x1 , color="yellow")  #畫圖 x1 顏色=黃色
ax[3].plot(t, x2 , color="green")  #畫圖 x2 顏色=綠色
ax[3].plot(t, x3 , color="blue")  #畫圖 x3 顏色=藍色
ax[3].plot(t, x4 , color="red")  #畫圖 x4 顏色=紅色
ax[3].set_xlabel('x')          #X軸標籤
ax[3].set_ylabel('y')          #Y軸標籤   
ax[3].set_title("x4")          #標題Title

plt.tight_layout()
plt.show()   #把圖顯示出來都是加在最後一行 一定要加