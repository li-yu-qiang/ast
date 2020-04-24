import numpy as np
import matplotlib.pyplot as plt
# 字体
# plt.rcParams['font.sans-serif']=['SimHei']

# 设置进行傅里叶变换之前正弦函数图片大小和坐标轴标签
plt.figure(figsize=(6,4)) 
plt.xlabel('x') 
plt.ylabel('y')
# plt.title('Before Fourier transform')

# 生成一列随机数，并叠加在三个正弦函数之和上
arr0=np.random.uniform(-1,1,1000)
x=np.linspace(-10,10,1000)
y=np.sin(x)+2*np.sin(3*x+np.pi/6)+3*np.sin(5*x+np.pi/3)+arr0
plt.plot(x,y,linewidth=1)

# 设置进行傅里叶变换之后正弦函数图片大小和坐标轴标签
plt.figure(figsize=(6,4)) 
plt.xlabel('frequency') 
plt.ylabel('y')
# plt.title('After Fourier transform')

# 进行快速傅里叶变换
freqs=np.fft.fftfreq(np.size(x),x[1]-x[0])
idx=np.argsort(freqs)
ps=np.abs(np.fft.fft(y))**2
plt.plot(freqs[idx],ps[idx])
plt.xlim(-6,6)

plt.show()
