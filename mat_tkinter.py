from tkinter import *
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as tkg

root=Tk()
root.title('sinusoidal')
root.geometry('650x800')

def tampil_plot():
	amplitudo=float(slider_amplitudo.get())
	frekuensi=float(slider_frekuensi.get())
	theta=float(slider_theta.get())
	x=np.arange(0,5,0.1)
	y=amplitudo*np.sin((2*frekuensi*x)+np.deg2rad(theta*36))
	figure=plt.figure(figsize=(5,4),dpi=100)
	figure.add_subplot(111).plot(x,y)
	grafik=tkg(figure,root)
	grafik.get_tk_widget().grid(row=5,column=0,padx=5,pady=5)
	plt.grid()



judul=Label(root,text='GRAFIK SINUSOIDAL',font=('arial bold',14))
judul.grid(row=0,column=0,padx=5,pady=5)

# slider amplitudo
slider_amplitudo=Scale(root,from_=0,to=5,width=20,length=300,orient=HORIZONTAL,label='Amplitudo (cm)')
slider_amplitudo.grid(row=1,column=0,padx=5,pady=5)

# slider frekuensi
slider_frekuensi=Scale(root,from_=0,to=5,width=20,length=300,orient=HORIZONTAL,label='Frekuensi (Hz)')
slider_frekuensi.grid(row=2,column=0,padx=5,pady=5)

# slider theta
slider_theta=Scale(root,from_=0,to=5,width=20,length=300,orient=HORIZONTAL,label='sudut theta (derajat)')
slider_theta.grid(row=3,column=0,padx=5,pady=5)

# tombol proses
proses=Button(root,text='proses',font=('arial bold',14),command=tampil_plot)
proses.grid(row=4,column=0,padx=5,pady=5)

root.mainloop()