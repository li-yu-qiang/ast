from scipy.stats import ks_2samp
from scipy.stats import kstest
import numpy as np
import scipy.stats as spstat
import matplotlib.pyplot as plt
# 字体
plt.rcParams['font.sans-serif']=['Heiti']

# 生成100个随机整数
n1=100
norm=np.random.randint(0,10,size=n1)
am=np.mean(norm)
ss=np.std(norm)
cdf=spstat.cumfreq(norm,numbins=100)
x1=np.arange(cdf[1],n1*cdf[2]+cdf[1],cdf[2])
y1=cdf[0]/n1

# 由上面生成的随机整数的构成生成10000个随机数
n2=10000
beta=ss*np.random.randn(n2)+am
cdf=spstat.cumfreq(beta,numbins=1000)
x2=np.arange(cdf[1],1000*cdf[2]+cdf[1],cdf[2])
y2=cdf[0]/n2

print(ks_2samp(norm,beta))

plt.plot(x1,y1,label='norm')
plt.plot(x2,y2,'--',label='beta')
# plt.title('两个分布的相关性')

plt.legend()
plt.show()