import matplotlib.pyplot as plt
import numpy as np


x=np.arange(0,4,0.1)
#print(x)
y1=np.sin(x)
y2=np.cos(x)
y3=np.sin(x**2)
y4=np.cos((2*x)**3)
plt.subplot(221).plot(x,y1,color='red')
plt.subplot(222).plot(x,y2)
plt.subplot(223).plot(x,y3,color='red')
plt.subplot(224).plot(x,y3)

plt.tight_layout()
plt.show()