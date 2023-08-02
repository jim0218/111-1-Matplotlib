#第一批 第四題
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random

t = np.linspace(0,1,200,endpoint=False)
x = 20*np.cos(2*np.pi*5*t)  #原始訊號


a_noise1 = 5   # noise1的振幅大小
a_noise2 = 5   # noise2的振幅大小
a_noise3 = 5   # noise3的振幅大小

p_noise1 = 10  # noise1的10%雜訊
p_noise2 = 30  # noise2的30%雜訊
p_noise3 = 50  # noise3的50%雜訊

noise1 = np.zeros(x.size)   # noise1的10%脈衝雜訊
for i in range(x.size):      
  p1 = random.uniform(0,1)
  if p1 <= p_noise1/100 :    
    p2=random.uniform(0,1)
    if p2<0.5:
      noise1[i]= a_noise1
    else:
      noise1[i]= -a_noise1

y1 = x+noise1   #原始訊號+noise1的10%脈衝雜訊

noise2 = np.zeros(x.size)   # noise2的30%脈衝雜訊 
for i in range(x.size):    
  p1 = random.uniform(0,1)
  if p1 <= p_noise2/100 :    
    p2=random.uniform(0,1)
    if p2<0.5:
      noise2[i]= a_noise2
    else:
      noise2[i]= -a_noise2

y2 = x+noise2   #原始訊號+noise2的30%脈衝雜訊

noise3 = np.zeros(x.size)   # noise3的50%脈衝雜訊
for i in range(x.size):    
  p1 = random.uniform(0,1)
  if p1 <= p_noise3/100 :    
    p2=random.uniform(0,1)
    if p2<0.5:
      noise3[i]= a_noise3
    else:
      noise3[i]= -a_noise3

y3 = x+noise3   #原始訊號+noise3的50%脈衝雜訊


f, ax = plt.subplots(3,2,figsize=(10,8))

ax[0,0].plot(t,x)           #圖一 左上 原始訊號
ax[0,0].plot(t ,noise1 ,color="red") #圖一 左上 noise1 顏色=紅色   
ax[0,0].set_title("x , noise1")     
ax[0,0].set_xlabel("t(second)") 
ax[0,0].set_ylabel("Amplitude") 


ax[0,1].plot(t ,y1 ,color="green")    #圖二 右上  原始訊號+noise1 顏色=綠色
ax[0,1].set_title("x+noise1")      
ax[0,1].set_xlabel("t(second)") 
ax[0,1].set_ylabel("Amplitude") 

ax[1,0].plot(t,x)            #圖三 左中 原始訊號 
ax[1,0].plot(t ,noise2 ,color="red") #圖三 左中 noise2 顏色=紅色     
ax[1,0].set_title("x , noise2")    
ax[1,0].set_xlabel("t(second)") 
ax[1,0].set_ylabel("Amplitude") 

ax[1,1].plot(t ,y2 ,color="green")   #圖四 右中 原始訊號+noise2 顏色=綠色  
ax[1,1].set_title("x+noise2")      
ax[1,1].set_xlabel("t(second)") 
ax[1,1].set_ylabel("Amplitude")

ax[2,0].plot(t,x)             #圖五 左下  原始訊號
ax[2,0].plot(t ,noise3 ,color="red")  #圖五 左下   noise3 顏色=紅色   
ax[2,0].set_title("x , noise3")      
ax[2,0].set_xlabel("t(second)") 
ax[2,0].set_ylabel("Amplitude") 

ax[2,1].plot(t, y3 ,color="green")   #圖六 右下 原始訊號+noise3 顏色=綠色    
ax[2,1].set_title("x+noise3")     
ax[2,1].set_xlabel("t(second)") 
ax[2,1].set_ylabel("Amplitude")

plt.tight_layout()   #讓圖自動分開 不然標題會跟X軸擠在一起
plt.show()   #把圖顯示出來都是加在最後一行 一定要加