# Assalamualaikum, percobaan membuat grafik dinamis dengan matplotlib python

import matplotlib.pyplot as plt 
import numpy as np 
import time

def jarak_glbb(kec_awal,percepatan,waktu):
	x=np.arange(0,waktu,0.1)
	# rumus s = v0.t + 0,5.a.t^2
	y=(kec_awal*x)+(0.5*percepatan*(x**2))
	return x,y

kec_awal=0
percepatan=2
waktu=1

for i in range(1,10):
	x1,y1=jarak_glbb(kec_awal,percepatan,waktu)
	waktu=waktu+i
	plt.plot(x1,y1)
	plt.show()
	time.sleep(1)
	plt.close(1)
'''
masih belum jadi
'''