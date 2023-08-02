#第一批  第一題
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random

t = np.linspace(0,1,200,endpoint=False)
x = 10 * np.cos(2 * np.pi * 3 * t)  #原始訊號

a_noise1 = 3  # noise1的振幅大小
a_noise2 = 3  # noise1的振幅大小

p_noise1 = 30  # noise1的30%雜訊
p_noise2 = 30  # noise2的30%雜訊
p_noise3 = 30  # noise3的30%雜訊

a_noise3 = 0   # noise3的平均值
s_noise3 = 1.5  # noise3的標準差

noise1 = np.zeros(x.size)  # 30%均勻雜訊
for i in range(x.size):
  p1 = random.uniform(0,1)
  if p1 <= p_noise1/100 :
    noise1[i] = random.uniform(-a_noise1,a_noise1,1)

y1 = x+noise1    #原始訊號+30%均勻雜訊

noise2 = np.zeros(x.size)   # 30%脈衝雜訊
for i in range(x.size):    
  p1 = random.uniform(0,1)
  if p1 <= p_noise2/100 :    
    p2=random.uniform(0,1)
    if p2<0.5:
      noise2[i]= a_noise2
    else:
      noise2[i]= -a_noise2

y2 = x+noise2   #原始訊號+30%脈衝雜訊


noise3 = np.zeros(x.size)   # 30%高斯雜訊
for i in range(x.size):    
  p1 = random.uniform(0,1)
  if p1 <= p_noise3/100 :    
    noise3[i] = random.normal(a_noise3 , s_noise3 , 1)   #高斯雜訊(平均值,標準差,個數)

y3 = x+noise3  #原始訊號+30%高斯雜訊

f, ax = plt.subplots(4,1,figsize=(10,11))


ax[0].plot(t,x)  #圖一 原始訊號
ax[0].set_title("x") #標題Title
ax[0].set_xlabel("t(second)")  #X軸標籤
ax[0].set_ylabel("Amplitude")  #Y軸標籤


#圖二 紅色:30%均勻雜訊   藍色:原始訊號+30%均勻雜訊
ax[1].plot(t,noise1,label="noise1",color="red")  #圖二 紅色:30%均勻雜訊
ax[1].plot(t,y1,label="x+noise1")         #圖二 藍色:原始訊號+30%均勻雜訊
ax[1].legend(loc="upper left")          #圖例位置 左上
ax[1].set_title("noise1")               #標題Title
ax[1].set_xlabel("t(second)")             #X軸標籤
ax[1].set_ylabel("Amplitude")             #Y軸標籤

#圖三 紅色:30%脈衝雜訊  藍色:原始訊號+30%脈衝雜訊
ax[2].plot(t,noise2,label="noise2",color="red") #圖三 紅色:30%脈衝雜訊
ax[2].plot(t,y2,label="x+noise2")        #圖三 藍色:原始訊號+30%脈衝雜訊 
ax[2].legend(loc="upper left")         #圖例位置 左上
ax[2].set_title("noise2")              #標題Title
ax[2].set_xlabel("t(second)")            #X軸標籤
ax[2].set_ylabel("Amplitude")            #Y軸標籤

#圖四 紅色:30%高斯雜訊 藍色:原始訊號+30%高斯雜訊
ax[3].plot(t,noise3,label="noise3",color="red")  #圖四 紅色:30%高斯雜訊
ax[3].plot(t,y3,label="x+noise3")         #圖四 藍色:原始訊號+30%高斯雜訊
ax[3].legend(loc="upper left")          #圖例位置 左上
ax[3].set_title("noise3")               #標題Title
ax[3].set_xlabel("t(second)")             #X軸標籤
ax[3].set_ylabel("Amplitude")             #Y軸標籤

plt.tight_layout()  #讓圖自動分開
plt.show()      #把圖顯示出來都是加在最後一行 一定要加