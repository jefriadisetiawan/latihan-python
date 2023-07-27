# Assalamualaikum, percobaan membuat 3 grafik

import numpy as np
import matplotlib.pyplot as plt

def grafik():
	x=np.arange(0,4,0.1)
	y=np.sin(np.deg2rad(x))
	return x,y

fig=plt.figure()
ax1=fig.add_subplot(221)
ax2=fig.add_subplot(222)
ax3=fig.add_subplot(223)

x1,y1=grafik()
ax1.plot(x1,y1)

x2,y2=grafik()
ax2.plot(x2,y2)

x3,y3=grafik()
ax3.plot(x3,y3)

plt.show()
