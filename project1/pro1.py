'''
project aplikasi python pertama yang bernama ....
1) 6-11-2022 membuat window dan menu
'''
from tkinter import *
from tkinter import messagebox

class MainWindow:
	
	def __init__(self,root):
		self.root=Tk()
		self.root.title('project aplikasi 1')
		self.root.geometry('600x400')
		self.mymenu=Menu(self.root,font=('arial',12))
		self.root.config(menu=self.mymenu)
		# membuat daftar menu
		self.data=Menu(self.mymenu)
		self.plot=Menu(self.mymenu)
		self.about=Menu(self.mymenu)
		self.mymenu.add_cascade(label='Data',menu=self.data)
		self.mymenu.add_cascade(label='Plot',menu=self.plot)
		self.mymenu.add_cascade(label='About',menu=self.about)

		self.data.add_command(label='Tampilkan data',command=self.about)
		self.data.add_command(label='Input data',command=self.about)
		self.data.add_command(label='Hapus data data',command=self.about)


		# Label selamat datang
		buka_label=Label(self.root,text='Selamat datang di aplikasi\nPerhitungan Gerak Lurus Berubah Beraturan (GLBB)',
			font=('arial bold',14)).pack(fill='both',pady=5)
		self.root.mainloop()

		def about(self):
			messagebox.showinfo('ini adalah informasi')
	

if __name__ == '__main__':
	MainWindow()