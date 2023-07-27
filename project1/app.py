from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3



class MainWindow:

	
	def __init__(self,root):
		self.root=root
		self.root.title('aplikasi coba')
		#self.root.geometry('600x400')
		self.my_menu=Menu(self.root,font=('arial',12))
		self.root.config(menu=self.my_menu)
		self.data=Menu(self.my_menu,font=('arial',12))
		self.grafik=Menu(self.my_menu,font=('arial',12))
		self.informasi=Menu(self.my_menu,font=('arial',12))
		# isi menu item
		self.my_menu.add_cascade(label='Data',menu=self.data)
		self.data.add_command(label='Tampilkan data',command=self.info)
		self.data.add_separator()
		self.data.add_command(label='Input data',command=self.info)
		self.data.add_command(label='Ubah data',command=self.info)

		self.my_menu.add_cascade(label='Grafik',menu=self.grafik)
		self.my_menu.add_cascade(label='Informasi',menu=self.informasi)

		# isi program
		self.judul_label=Label(self.root,text='DAFTAR NILAI SISWA',font=('arial bold',13),anchor='center').grid(row=0,column=0,columnspan=3,padx=5,pady=5)
		self.nama_label=Label(self.root,text='Nama Siswa',font=('arial',12)).grid(row=1,column=0,padx=5,pady=5,sticky=W)
		self.induk_label=Label(self.root,text='No. Induk',font=('arial',12)).grid(row=2,column=0,padx=5,pady=5,sticky=W)
		self.IPA_label=Label(self.root,text='Nilai IPA',font=('arial',12)).grid(row=3,column=0,padx=5,pady=5,sticky=W)
		self.MTK_label=Label(self.root,text='Nilai Matematika',font=('arial',12)).grid(row=4,column=0,padx=5,pady=5,sticky=W)
		self.BIN_label=Label(self.root,text='Nilai Bahasa Indonesia',font=('arial',12)).grid(row=5,column=0,padx=5,pady=5,sticky=W)
		self.BIG_label=Label(self.root,text='Nilai Bahasa Inggris',font=('arial',12)).grid(row=6,column=0,padx=5,pady=5,sticky=W)
		self.nama_entry=Entry(root,width=20,font=('arial',12),bg='white',fg='black').grid(row=1,column=1,padx=5,pady=5,sticky=W)
		self.induk_entry=Entry(root,width=20,font=('arial',12),bg='white',fg='black').grid(row=2,column=1,padx=5,pady=5,sticky=W)
		self.IPA_entry=Entry(root,width=20,font=('arial',12),bg='white',fg='black').grid(row=3,column=1,padx=5,pady=5,sticky=W)
		self.MTK_entry=Entry(root,width=20,font=('arial',12),bg='white',fg='black').grid(row=4,column=1,padx=5,pady=5,sticky=W)
		self.BIN_entry=Entry(root,width=20,font=('arial',12),bg='white',fg='black').grid(row=5,column=1,padx=5,pady=5,sticky=W)
		self.BIG_entry=Entry(root,width=20,font=('arial',12),bg='white',fg='black').grid(row=6,column=1,padx=5,pady=5,sticky=W)
		kolom=['Nama','No.Induk','Nilai IPA','Nilai Matematika','Nilai Bahasa Indonesia','Nilai Bahasa Inggris']
		self.tree=ttk.Treeview(self.root,columns=kolom,show='headings').grid(row=7,column=0,columnspan=3,padx=5,pady=5,sticky=W+E)
		#self.tree['columns']=("Nama","No.Induk","Nilai IPA","Nilai Matematika","Nilai Bahasa Indonesia","Nilai Bahasa Inggris")
		#self.tree.column("#0",width=0,stretch=NO)
		for item in kolom:
			print(item)
			#self.tree(item,width=75)
			self.tree.heading(item,text=item)


		self.root.mainloop()

	def info(self):
		messagebox.showinfo(title='ini adalah info',message='terima kasih, aplikasi sederhana\nJefri Adi Setiawan')
	




if __name__=='__main__':
	app=Tk()
	MainWindow(app)
	