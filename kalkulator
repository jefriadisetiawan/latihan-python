# Assalamualaikum wr wb, pada cideo ini kita mencoba membuat aplikasi kalkulator sederhana

from tkinter import *

# definisi
window=Tk()
window.title("aplikasi kalkulator")

# membuat fungsi

def angka(n):
	layar.insert(END,n)

def tambah():
	global temp1
	temp1=int(float(layar.get()))
	global opr
	opr=1
	layar.delete(0,END)

def kurang():
	global temp1
	temp1=int(float(layar.get()))
	global opr
	opr=2
	layar.delete(0,END)

def kali():
	global temp1
	temp1=int(float(layar.get()))
	global opr
	opr=3
	layar.delete(0,END)

def bagi():
	global temp1
	temp1=int(float(layar.get()))
	global opr
	opr=4
	layar.delete(0,END)

def hapus():
	global temp1
	global temp2
	global opr
	temp1=0
	temp2=0
	opr=""
	layar.delete(0,END)

def hasil():
	global temp2
	temp2=int(float(layar.get()))
	global opr
	global temp1
	if opr==1:
		hasilnya=temp1+temp2
		layar.delete(0,END)
		layar.insert(0,hasilnya)
		temp1=int(float(layar.get()))
		temp2=0
		opr=""
	if opr==2:
		hasilnya=temp1-temp2
		layar.delete(0,END)
		layar.insert(0,hasilnya)
		temp1=int(float(layar.get()))
		temp2=0
		opr=""
	if opr==3:
		hasilnya=temp1*temp2
		layar.delete(0,END)
		layar.insert(0,hasilnya)
		temp1=int(float(layar.get()))
		temp2=0
		opr=""
	if opr==4:
		hasilnya=temp1/temp2
		layar.delete(0,END)
		layar.insert(0,hasilnya)
		temp1=int(float(layar.get()))
		temp2=0
		opr=""
	if opr=="":
		pass


# membuat widget tombol
frame_layar=LabelFrame(window,text="layar")
frame_layar.pack(padx=5,pady=5)
frame_tombol=LabelFrame(window,text="tombol")
frame_tombol.pack(padx=5,pady=5)

layar=Entry(frame_layar,width=24, bg="white",fg="black",font=("arial",14),borderwidth=2,justify=RIGHT)
layar.pack(padx=5,pady=5,fill="x")

angka_1=Button(frame_tombol,text=1,padx=15,pady=12,font=("arial",12),fg="white",command=lambda: angka(1))
angka_1.grid(column=0,row=0,padx=2,pady=2)
angka_2=Button(frame_tombol,text=2,padx=15,pady=12,font=("arial",12),fg="white",command=lambda: angka(2))
angka_2.grid(column=1,row=0,padx=2,pady=2)
angka_3=Button(frame_tombol,text=3,padx=15,pady=12,font=("arial",12),fg="white",command=lambda: angka(3))
angka_3.grid(column=2,row=0,padx=2,pady=2)

angka_4=Button(frame_tombol,text=4,padx=15,pady=12,font=("arial",12),fg="white",command=lambda: angka(4))
angka_4.grid(column=0,row=1,padx=2,pady=2)
angka_5=Button(frame_tombol,text=5,padx=15,pady=12,font=("arial",12),fg="white",command=lambda: angka(5))
angka_5.grid(column=1,row=1,padx=2,pady=2)
angka_6=Button(frame_tombol,text=6,padx=15,pady=12,font=("arial",12),fg="white",command=lambda: angka(6))
angka_6.grid(column=2,row=1,padx=2,pady=2)

angka_7=Button(frame_tombol,text=7,padx=15,pady=12,font=("arial",12),fg="white",command=lambda: angka(7))
angka_7.grid(column=0,row=2,padx=2,pady=2)
angka_8=Button(frame_tombol,text=8,padx=15,pady=12,font=("arial",12),fg="white",command=lambda: angka(8))
angka_8.grid(column=1,row=2,padx=2,pady=2)
angka_9=Button(frame_tombol,text=9,padx=15,pady=12,font=("arial",12),fg="white",command=lambda: angka(9))
angka_9.grid(column=2,row=2,padx=2,pady=2)

angka_0=Button(frame_tombol,text=0,padx=15,pady=12,font=("arial",12),fg="white",command=lambda: angka(0))
angka_0.grid(column=0,row=3,padx=2,pady=2)
sama_dengan=Button(frame_tombol,text="=",padx=15,pady=12,font=("arial",12),fg="white",command=hasil)
sama_dengan.grid(column=1,row=3,padx=2,pady=2)
clear=Button(frame_tombol,text="C",padx=15,pady=12,font=("arial",12),fg="white",command=hapus)
clear.grid(column=2,row=3,padx=2,pady=2)

# membuat tombol operasi matematika
tombol_tambah=Button(frame_tombol,text="+",padx=15,pady=12,font=("arial",12),fg="white",command=tambah)
tombol_tambah.grid(column=3,row=0,padx=2,pady=2)
tombol_kurang=Button(frame_tombol,text="-",padx=15,pady=12,font=("arial",13),fg="white",command=kurang)
tombol_kurang.grid(column=3,row=1,padx=2,pady=2)
tombol_kali=Button(frame_tombol,text="x",padx=15,pady=12,font=("arial",12),fg="white",command=kali)
tombol_kali.grid(column=3,row=2,padx=2,pady=2)
tombol_bagi=Button(frame_tombol,text="/",padx=15,pady=12,font=("arial",13),fg="white",command=bagi)
tombol_bagi.grid(column=3,row=3,padx=2,pady=2)

label_penutup=Label(window,text="created by jefri 2022")
label_penutup.pack()
# jalankan program
window.mainloop()
