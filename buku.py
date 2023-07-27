# Assalamualaikum, percobaan membuat kembali aplikasi CRUD python tkinter dengan SQLite
# program membuat aplikasi inventory buku sederhana

from tkinter import *
from tkinter import ttk
import sqlite3


# membuat GUI program

root=Tk()
root.title('inventory buku')
root.geometry('530x420')

# membuat fungsi

def hapus_entry():
	no_reg_entry.delete(0,END)
	judul_buku_entry.delete(0,END)
	penulis_entry.delete(0,END)

def koneksi_db():
	koneksi=sqlite3.connect('data_buku.db')
	kursor=koneksi.cursor()
	query='CREATE TABLE IF NOT EXISTS buku(no_reg text(5),judul text(20),penulis text(20))'
	kursor.execute(query)

def hapus_tampilan():
	for item in tree_view.get_children():
		tree_view.delete(item)

def tampilkan_data():
	hapus_tampilan()
	koneksi=sqlite3.connect('data_buku.db')
	kursor=koneksi.cursor()
	hasil=kursor.execute('SELECT * FROM buku').fetchall()
	for item in hasil:
		tree_view.insert(parent="",index=END,values=(item[0],item[1],item[2]))
	jumlah_data=kursor.execute('SELECT COUNT(*) FROM buku').fetchall()
	jumlah_data_label['text']='jumlah data = '+str(jumlah_data[0][0])
	koneksi.commit()
	koneksi.close()

def input_data():
	no_reg=no_reg_entry.get()
	judul=judul_buku_entry.get()
	penulis=penulis_entry.get()
	koneksi=sqlite3.connect('data_buku.db')
	kursor=koneksi.cursor()
	query="INSERT INTO buku VALUES(?,?,?)"
	nilai=(no_reg,judul,penulis)
	kursor.execute(query,nilai)
	koneksi.commit()
	koneksi.close()
	tampilkan_data()
	hapus_entry()

def seleksi_tree(event):
	hapus_entry()
	for seleksi in tree_view.selection():
		item=tree_view.item(seleksi)
		no_reg_entry.insert(0,item['values'][0])
		judul_buku_entry.insert(0,item['values'][1])
		penulis_entry.insert(0,item['values'][2])
	no_reg_entry['state']='disabled'

def update_data():
	koneksi=sqlite3.connect('data_buku.db')
	kursor=koneksi.cursor()
	query="UPDATE buku SET judul=?,penulis=? WHERE no_reg=?"
	#no_reg=no_reg_entry.get()
	#judul=judul_buku_entry.get()
	#penulis=penulis_entry.get()
	#nilai=(judul,penulis,no_reg)
	nilai=(judul_buku_entry.get(),penulis_entry.get(),no_reg_entry.get())
	kursor.execute(query,nilai)
	koneksi.commit()
	koneksi.close()
	tampilkan_data()
	no_reg_entry['state']='normal'
	hapus_entry()
	

def delete_data():
	koneksi=sqlite3.connect('data_buku.db')
	kursor=koneksi.cursor()
	query="DELETE from buku WHERE no_reg="
	nilai=no_reg_entry.get()
	kursor.execute(query+nilai)
	koneksi.commit()
	koneksi.close()
	tampilkan_data()
	no_reg_entry['state']='normal'
	hapus_entry()
	
def batal():
	no_reg_entry['state']='normal'
	hapus_entry()

# membuat label judul dan lainnya

judul=Label(root, text='Inventory Buku Sederhana', font=('arial bold',16),anchor=CENTER)
no_reg_label=Label(root,text='No. Registrasi', font=('arial bold',13),anchor='w')
judul_buku_label=Label(root,text='Judul Buku', font=('arial bold',13),anchor='w')
penulis_label=Label(root,text='Penulis', font=('arial bold',13),anchor='w')
no_reg_entry=Entry(root,width=20,font=('arial bold',13),bg='white',fg='black')
judul_buku_entry=Entry(root,width=20,font=('arial bold',13),bg='white',fg='black')
penulis_entry=Entry(root,width=20,font=('arial bold',13),bg='white',fg='black')
input_tombol=Button(root,text="Input Data",font=('arial bold',13),width=10,command=input_data)
update_tombol=Button(root,text="Update Data",font=('arial bold',13),width=10,command=update_data)
delete_tombol=Button(root,text="Delete Data",font=('arial bold',13),width=10,command=delete_data)
batal_tombol=Button(root,text="batal",font=('arial bold',13),width=10,command=batal)
tree_view=ttk.Treeview(root)
jumlah_data_label=Label(root, text='jumlah data = ', font=('arial',13))

# mengatur treeview
tree_view['columns']=("No. Reg","Judul Buku","Penulis")
tree_view.column("#0",width=0,stretch=NO)
tree_view.column("No. Reg",width=100)
tree_view.column("Judul Buku",width=200)
tree_view.column("Penulis",width=200)
tree_view.heading("No. Reg",text='No. Reg')
tree_view.heading("Judul Buku",text='Judul Buku')
tree_view.heading("Penulis",text='Penulis')

judul.grid(row=0,column=0,padx=4,pady=2,columnspan=3)
no_reg_label.grid(row=1,column=0,padx=4,pady=2,sticky=W)
judul_buku_label.grid(row=2,column=0,padx=4,pady=2,sticky=W)
penulis_label.grid(row=3,column=0,padx=4,pady=2,sticky=W)
no_reg_entry.grid(row=1,column=1,padx=4,pady=2,sticky=W)
judul_buku_entry.grid(row=2,column=1,padx=4,pady=2,sticky=W)
penulis_entry.grid(row=3,column=1,padx=4,pady=2,sticky=W)
input_tombol.grid(row=1,column=2,padx=4,pady=2,sticky=W)
update_tombol.grid(row=2,column=2,padx=4,pady=2,sticky=W)
delete_tombol.grid(row=3,column=2,padx=4,pady=2,sticky=W)
tree_view.grid(row=4,column=0,pady=2,columnspan=3)
batal_tombol.grid(row=5,column=0,padx=4,pady=2,sticky=W)
jumlah_data_label.grid(row=5,column=1,padx=4,pady=2,columnspan=2)



tampilkan_data()

# memilih salah satu data dalam treeview
tree_view.bind('<Double-1>',seleksi_tree) # data dalam treevies di klik kiri satu kali




# menjalankan program

root.mainloop()

