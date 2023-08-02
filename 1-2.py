#第一批 第二題
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,1,1000,endpoint=False)
x1 = 3 * np.cos(2 * np.pi * 10 * t + np.pi/4)     #原始訊號 x1
x2 = 4 * np.cos(2 * np.pi * 10 * t + 3 * np.pi/4)  #原始訊號 x2
x3 = 5 * np.cos(2 * np.pi * 10 * t )          #原始訊號 x3
x4 = x1 + x2 + x3                      #訊號   x4=x1+x2+x3

f, ax = plt.subplots(2,2,figsize=(10,7)) #,sharey="row",sharex="col"

ax[0,0].plot(t,x1)         #圖一 左上
ax[0,0].set_title("x1")     
ax[0,0].set_xlabel("t(second)")
ax[0,0].set_ylabel("Amplitude")
 
ax[0,1].plot(t,x3)         #圖二 右上
ax[0,1].set_title("x3")
ax[0,1].set_xlabel("t(second)")
ax[0,1].set_ylabel("Amplitude")

ax[1,0].plot(t,x2)         #圖三 左下
ax[1,0].set_title("x2")
ax[1,0].set_xlabel("t(second)")
ax[1,0].set_ylabel("Amplitude")

ax[1,1].plot(t,x4)         #圖四 右下
ax[1,1].set_title("x4 = x1 + x2 + x3")
ax[1,1].set_xlabel("t(second)")
ax[1,1].set_ylabel("Amplitude")


x_1 = complex(3 * np.cos(np.pi/4)  ,3 * np.sin(np.pi/4))     # x1 = 3cosπ/4 + 3sinπ/4
x_2 = complex(4 * np.cos(3*np.pi/4) ,3 * np.sin(3*np.pi/4))    # x2 = 4cos3π/4 + 4sin3π/4
x_3 = complex(5 * np.cos(0)  ,5 * np.sin(0) )          # x3 = 5cos0 + 5sin0
x_4 = x_1 + x_2 + x_3                        

A = abs(x_4)            #  x4絕對值=A
x4_angle = np.angle(x_4)      # x4的角度
phi = x4_angle * 3.14 / 180   #  x4的角度*π/180 = Φ 

print("f=10HZ")          #同原始訊號的頻率 2πft 所以f=20/2=10
print("A=",A)           #印出 A
print("Φ=",phi)         #印出 Φ
print("|X4|=",x_4)        #印出 |X4|

plt.tight_layout()  #讓圖自動分開 不然X3、X4的標題會跟X1、X2的X軸座標擠在一起 
plt.show()   #把圖顯示出來都是加在最後一行 一定要加