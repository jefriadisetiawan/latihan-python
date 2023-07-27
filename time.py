import numpy as np 
import matplotlib.pyplot as plt 


def glbb(waktu,kecepatan_awal,percepatan):
	t=np.arange(0,waktu,0.1)
	vt=kecepatan_awal+percepatan*t
	return t,vt

x,y=glbb(5,0,9.8)
plt.plot(x,y)
plt.show()