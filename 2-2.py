#第二批 第二題
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random
t = np.linspace(0,1,200,endpoint=False)
x = 10*np.cos(2*np.pi*5*t)         # 原始訊號

p_noise1 = 30   # noise1的 30% 雜訊
p_noise2 = 30   # noise2的 30% 雜訊
p_noise3 = 30   # noise3的 30% 雜訊

a_noise1 = 1    #noise1的振幅
a_noise2 = 3    #noise2的振幅
a_noise3 = 5    #noise3的振幅

noise1 = np.zeros(x.size)   # noise1 振幅1  30%的均勻雜訊  
for i in range(x.size):
  p1 = random.uniform(0,1)
  if p1 <= p_noise1/100:
    noise1[i] = random.uniform(-a_noise1,a_noise1,1)

y1 = x+noise1        # 原始訊號 + noise1  

noise2 = np.zeros(x.size)   # noise2 振幅3  30%的均勻雜訊
for i in range(x.size):
  p1 = random.uniform(0,1)
  if p1 <= p_noise2/100:
    noise2[i] = random.uniform(-a_noise2,a_noise2,1)

y2 = x+noise2       # 原始訊號 + noise2  

noise3 = np.zeros(x.size)  # noise3 振幅5  30%的均勻雜訊
for i in range(x.size):
  p1 = random.uniform(0,1)
  if p1 <= p_noise3/100:
    noise3[i] = random.uniform(-a_noise3,a_noise3,1) 

y3 = x+noise3       # 原始訊號 + noise3 

f, ax = plt.subplots(3,3,figsize=(10,9),sharey="row") #(高,寬)figsiz設定圖大小可不加

ax[0,1].plot(t,x,color="red")     #圖一 上中 原始訊號 顏色=紅色 
ax[0,1].set_title("x")         #設定標題
ax[0,1].set_xlabel("t(second)")    #設定X軸標題
ax[0,1].set_ylabel("Amplitude")    #設定Y軸標題

ax[1,0].plot(t,noise1,color="green") #圖二 中左 noise1 顏色=綠色 
ax[1,0].set_title("noise1")      #設定標題
ax[1,0].set_xlabel("t(second)")    #設定X軸標題
ax[1,0].set_ylabel("Amplitude")    #設定Y軸標題

ax[1,1].plot(t,noise2,color="green") #圖三 中中 noise2 顏色=綠色
ax[1,1].set_title("noise2")      #設定標題
ax[1,1].set_xlabel("t(second)")    #設定X軸標題
ax[1,1].set_ylabel("Amplitude")    #設定Y軸標題

ax[1,2].plot(t,noise3,color="green") #圖四 中右 noise3 顏色=綠色
ax[1,2].set_title("noise3")      #設定標題
ax[1,2].set_xlabel("t(second)")    #設定X軸標題
ax[1,2].set_ylabel("Amplitude")    #設定Y軸標題

ax[2,0].plot(t,y1)          #圖五 下左 原始訊號+noise1
ax[2,0].set_title("x+noise1")     #設定標題
ax[2,0].set_xlabel("t(second)")    #設定X軸標題
ax[2,0].set_ylabel("Amplitude")    #設定Y軸標題

ax[2,1].plot(t,y2)          #圖六 下中 原始訊號+noise2
ax[2,1].set_title("x+noise2")     #設定標題
ax[2,1].set_xlabel("t(second)")    #設定X軸標題
ax[2,1].set_ylabel("Amplitude")    #設定Y軸標題

ax[2,2].plot(t,y3)          #圖七 下右 原始訊號+noise3
ax[2,2].set_title("x+noise3")     #設定標題
ax[2,2].set_xlabel("t(second)")    #設定X軸標題
ax[2,2].set_ylabel("Amplitude")    #設定Y軸標題

plt.tight_layout()   #讓圖自動分開 不然X3、X4的標題會跟X1、X2的X軸座標擠在一起
plt.show()   #把圖顯示出來都是加在最後一行 一定要加