import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

# 标准正态分布
# 产生10000组1000个在0-100的随机数列，并求平均值
ave1=np.zeros(10000)
for i in range(10000):
    data1=np.random.randn(1000)
    ave1[i]=np.mean(data1)

# 分别把10个随机数列、100个随机数列、1000个随机数列、10000个随机数列的均值分布直方图画出来
plt.figure(figsize=(8, 6))
plt.suptitle('正态分布分布')
ax1_1=plt.subplot(2,2,1)
ax1_2=plt.subplot(2,2,2)
ax1_3=plt.subplot(2,2,3)
ax1_4=plt.subplot(2,2,4)

ax1_1.hist(ave1[0:10],bins=100)
ax1_1.set_title(r'Histogram of N=10')
ax1_2.hist(ave1[0:100],bins=100)
ax1_2.set_title(r'Histogram of N=100')
ax1_3.hist(ave1[0:1000],bins=100)
ax1_3.set_title(r'Histogram of N=1000')
ax1_4.hist(ave1[0:10000],bins=100)
ax1_4.set_title(r'Histogram of N=10000')

# 随机分布
# 产生10000组1000个在0-100的随机数列，并求平均值
ave2=np.zeros(10000)
for i in range(10000):
    data2=np.random.rand(1000)
    ave2[i]=np.mean(data2)

# 分别把10个随机数列、100个随机数列、1000个随机数列、10000个随机数列的均值分布直方图画出来
plt.figure(figsize=(8, 6))
plt.suptitle('随机分布')
ax2_1=plt.subplot(2,2,1)
ax2_2=plt.subplot(2,2,2)
ax2_3=plt.subplot(2,2,3)
ax2_4=plt.subplot(2,2,4)

ax2_1.hist(ave2[0:10],bins=100)
ax2_1.set_title(r'Histogram of N=10')
ax2_2.hist(ave2[0:100],bins=100)
ax2_2.set_title(r'Histogram of N=100')
ax2_3.hist(ave2[0:1000],bins=100)
ax2_3.set_title(r'Histogram of N=1000')
ax2_4.hist(ave2[0:10000],bins=100)
ax2_4.set_title(r'Histogram of N=10000')

# gamma分布
# 产生10000组1000个在0-100的随机数列，并求平均值
ave3=np.zeros(10000)
for i in range(10000):
    data3=np.random.gamma(2,2,1000)
    ave3[i]=np.mean(data3)

# 分别把10个随机数列、100个随机数列、1000个随机数列、10000个随机数列的均值分布直方图画出来
plt.figure(figsize=(8, 6))
plt.suptitle('gamma分布')
ax3_1=plt.subplot(2,2,1)
ax3_2=plt.subplot(2,2,2)
ax3_3=plt.subplot(2,2,3)
ax3_4=plt.subplot(2,2,4)

ax3_1.hist(ave3[0:10],bins=100)
ax3_1.set_title(r'Histogram of N=10')
ax3_2.hist(ave3[0:100],bins=100)
ax3_2.set_title(r'Histogram of N=100')
ax3_3.hist(ave3[0:1000],bins=100)
ax3_3.set_title(r'Histogram of N=1000')
ax3_4.hist(ave3[0:10000],bins=100)
ax3_4.set_title(r'Histogram of N=10000')

# 指数分布
# 产生10000组1000个在0-100的随机数列，并求平均值
ave4=np.zeros(10000)
for i in range(10000):
    data4=np.random.exponential(1,1000)
    ave4[i]=np.mean(data4)

# 分别把10个随机数列、100个随机数列、1000个随机数列、10000个随机数列的均值分布直方图画出来
plt.figure(figsize=(8, 6))
plt.suptitle('指数分布')
ax4_1=plt.subplot(2,2,1)
ax4_2=plt.subplot(2,2,2)
ax4_3=plt.subplot(2,2,3)
ax4_4=plt.subplot(2,2,4)

ax4_1.hist(ave4[0:10],bins=100)
ax4_1.set_title(r'Histogram of N=10')
ax4_2.hist(ave4[0:100],bins=100)
ax4_2.set_title(r'Histogram of N=100')
ax4_3.hist(ave4[0:1000],bins=100)
ax4_3.set_title(r'Histogram of N=1000')
ax4_4.hist(ave4[0:10000],bins=100)
ax4_4.set_title(r'Histogram of N=10000')

# poisson分布
# 产生10000组1000个在0-100的随机数列，并求平均值
ave5=np.zeros(10000)
for i in range(10000):
    data5=np.random.poisson(10,size=1000)
    ave5[i]=np.mean(data5)

# 分别把10个随机数列、100个随机数列、1000个随机数列、10000个随机数列的均值分布直方图画出来
plt.figure(figsize=(8, 6))
plt.suptitle('poisson分布')
ax5_1=plt.subplot(2,2,1)
ax5_2=plt.subplot(2,2,2)
ax5_3=plt.subplot(2,2,3)
ax5_4=plt.subplot(2,2,4)

ax5_1.hist(ave5[0:10],bins=100)
ax5_1.set_title(r'Histogram of N=10')
ax5_2.hist(ave5[0:100],bins=100)
ax5_2.set_title(r'Histogram of N=100')
ax5_3.hist(ave5[0:1000],bins=100)
ax5_3.set_title(r'Histogram of N=1000')
ax5_4.hist(ave5[0:10000],bins=100)
ax5_4.set_title(r'Histogram of N=10000')

# beta分布
# 产生10000组1000个在0-100的随机数列，并求平均值
ave6=np.zeros(10000)
for i in range(10000):
    data6=np.random.beta(0.5,0.5,1000)
    ave6[i]=np.mean(data6)

# 分别把10个随机数列、100个随机数列、1000个随机数列、10000个随机数列的均值分布直方图画出来
plt.figure(figsize=(8, 6))
plt.suptitle('beta分布')
ax6_1=plt.subplot(2,2,1)
ax6_2=plt.subplot(2,2,2)
ax6_3=plt.subplot(2,2,3)
ax6_4=plt.subplot(2,2,4)

ax6_1.hist(ave6[0:10],bins=100)
ax6_1.set_title(r'Histogram of N=10')
ax6_2.hist(ave6[0:100],bins=100)
ax6_2.set_title(r'Histogram of N=100')
ax6_3.hist(ave6[0:1000],bins=100)
ax6_3.set_title(r'Histogram of N=1000')
ax6_4.hist(ave6[0:10000],bins=100)
ax6_4.set_title(r'Histogram of N=10000')

# 不同的分布
plt.figure(figsize=(8, 6))
plt.suptitle('不同的分布')
ax1=plt.subplot(2,3,1)
ax2=plt.subplot(2,3,2)
ax3=plt.subplot(2,3,3)
ax4=plt.subplot(2,3,4)
ax5=plt.subplot(2,3,5)
ax6=plt.subplot(2,3,6)

ax1.hist(data1,bins=100)
ax1.set_title(r'正态分布')
ax2.hist(data2,bins=100)
ax2.set_title(r'随机分布')
ax3.hist(data3,bins=100)
ax3.set_title(r'gamma分布')
ax4.hist(data4,bins=100)
ax4.set_title(r'指数分布')
ax5.hist(data5,bins=100)
ax5.set_title(r'poisson分布')
ax6.hist(data6,bins=100)
ax6.set_title(r'beta分布')

plt.show()
