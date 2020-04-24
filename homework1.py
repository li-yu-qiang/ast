import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
# 字体
plt.rcParams['font.sans-serif']=['SimHei']

# 设置图片大小和坐标轴标签
plt.figure(figsize=(8, 4)) 
plt.xlabel('测量次数n')  
plt.ylabel('n 次测量的误差')

# 生成随机数并存入数组
n=200
arr=np.zeros(n)
sigma=np.zeros(n)
for i in range(n):
    for j in range(n):
        r=np.random.randn(1,i)
        arr[j]=np.mean(r)
    sigma[i]=np.std(arr)
    arr=np.zeros(n)

x=np.arange(n)
y=sigma**2/x
xs=x[1::]
ys=sigma[1::]

# 画出生成随机数误差随生成次数变化的关系
plt.scatter(xs,ys,s=20,c='blue',label='data')
# print(xs)
# print(ys)

# 拟合生成随机数误差随生成次数变化的关系
def func(x,c):
    return x**(c)

result=curve_fit(func,xs[0:10:],ys[0:10:])
# print(result[0])
c=result[0]

# 画出生成随机数误差随生成次数变化的关系并给出对应的函数
y0 = xs**(c)
plt.plot(xs, y0,"r-",label='$y=x^{%5.3f}$'%tuple(c))

plt.legend()
plt.show()
