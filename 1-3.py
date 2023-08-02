#第一批 第三題
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,1,1000,endpoint=False)
x1 = np.cos (2 * np.pi * 3 * t)  #原始訊號 x1
x2 = np.cos (2 * np.pi * 6 * t)  #原始訊號 x2
x3 = np.cos (2 * np.pi * 9 * t)  #原始訊號 x3
x4 = x1+x2+x3               #訊號  x4 = x1+x2+x3  

f, ax = plt.subplots(2,1,figsize=(10,7))

#圖一
ax[0].plot(t, x1 , color="yellow" ,label = "x1")  #圖一 x1 顏色=黃色 圖例=x1
ax[0].plot(t, x2 , color="green" ,label = "x2")  #圖一 x2 顏色=綠色 圖例=x2
ax[0].plot(t, x3 , color="blue" ,label = "x3")  #圖一 x3 顏色=藍色 圖例=x3
ax[0].legend(loc="upper left")            #圖例位置  左上
ax[0].set_xlabel('x')          #X軸標籤
ax[0].set_ylabel('y')          #Y軸標籤   
ax[0].set_title("x1,x2,x3")      #標題Title

#圖二
ax[1].plot(t, x4, color = "red" )  #圖二 x4 顏色=紅色 
ax[1].set_label('x')       #X軸標籤
ax[1].set_ylabel('y')       #Y軸標籤
ax[1].set_title("x4")       #標題Title

plt.tight_layout()
plt.show()  #把圖顯示出來都是加在最後一行 一定要加