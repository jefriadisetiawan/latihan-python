from tkinter import *

class Main():
	
	def __init__(self):
		self=Tk()
		self.title('ini adalah judul')
		label1=Label(self,text='ini adalah teks').pack()
		tombol=Button(self,text='proses',command=ubah).pack()
		self.mainloop()

	def ubah(self):
		label1['text']='teks telah berubah'

if __name__=='__main__':
	Main()
