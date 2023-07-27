from tkinter import *
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



	
	

class Window():

	def __init__(self,root):
		self.amplitudo=0
		slider_frekuensi=0
		self.theta=0
		self.root=root
		self.root.geometry('600x700')
		self.root.title('percobaan')
		self.judul=Label(self.root,text='aplikasi gelombang',font=('arial bold',14))
		self.judul.grid(row=0,column=0,pady=2)
		self.slider_amplitudo=Scale(self.root,from_=0,to=5,width=20,orient=HORIZONTAL,
			font=('arial ',12),length=300,tickinterval=0.25,label='Amplitudo',command=self.update)
		self.slider_amplitudo.grid(row=1,column=0,pady=2,padx=2)
		self.slider_frekuensi=Scale(self.root,from_=0,to=5,width=20,orient=HORIZONTAL,
			font=('arial ',12),length=300,tickinterval=0.25,label='Frekuensi',command=self.update)
		self.slider_frekuensi.grid(row=2,column=0,pady=2,padx=2)
		self.slider_theta=Scale(self.root,from_=0,to=5,width=20,orient=HORIZONTAL,
			font=('arial ',12),length=300,tickinterval=0.25,label='Sudut Theta',command=self.update)
		self.slider_theta.grid(row=3,column=0,pady=2,padx=2)
		self.root.mainloop()
		self.plot_hasil()
		

	def update(self,event):
		self.amplitudo=float(self.slider_amplitudo.get())
		self.frekuensi=float(self.slider_frekuensi.get())
		self.theta=float(self.slider_theta.get())
		self.plot_hasil()

	def plot_hasil(self):
		x=np.arange(0,4,0.1)
		y=self.amplitudo*np.sin((2*self.frekuensi*x)+np.deg2rad(self.theta*30))
		figure=plt.figure(figsize=(5,4),dpi=100)
		figure.add_subplot(111).plot(x,y)
		grafik=FigureCanvasTkAgg(figure,self.root)
		grafik.get_tk_widget().grid(row=4,column=0,padx=2,pady=2)
		plt.grid

if __name__=='__main__':
	gui=Tk()
	Window(gui)