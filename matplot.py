# Assalamualaikum, belajar matplotlib
# sekarang kita tambahkan waktu supaya grafik dinamis

import matplotlib.pyplot as plt 
import numpy as np 
import time


def sinusoidal(amplitudo,frekuensi,waktu,theta):
	# rumusnya y =  A sin(2wt+theta)
	x=np.arange(0,waktu,0.1)
	y=amplitudo*np.sin(2*frekuensi*x+np.deg2rad(theta))
	return x,y

waktu=6
frekuensi=1
amplitudo=1
theta=0


x1,y1=sinusoidal(amplitudo,frekuensi,waktu,theta)
x2,y2=sinusoidal(amplitudo,frekuensi,waktu,theta+90)
x3=x1
y3=y1+y2
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.plot(x3,y3)
waktu+=1
plt.title('Grafik Sinusoidal')
plt.xlabel('waktu (s)')
plt.ylabel('amplitudo (m)')

plt.show()

