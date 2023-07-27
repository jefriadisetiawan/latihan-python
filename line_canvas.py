# Assalamualaikum, kita coba belajar canvas tkinter
# menambahkan color chooser dan eraser

from tkinter import *
from tkinter import colorchooser

x_awal=0
y_awal=0
warna='black'

def ambil_xy(event):
	global x_awal
	global y_awal
	x_awal=event.x 
	y_awal=event.y 

def gambar(event):
	global x_awal
	global y_awal
	global warna
	canvas_gambar.create_line(x_awal,y_awal,event.x,event.y,fill=warna,width=2)
	x_awal=event.x 
	y_awal=event.y 

def pilih_warna():
	global warna
	warna_pilihan=colorchooser.askcolor()
	warna=warna_pilihan[1]
	plh_warna['bg']=warna

def hapus_layarnya():
	canvas_gambar.delete('all')


root=Tk()
root.geometry('700x550')
root.title('simple canvas')

canvas_gambar=Canvas(root, width=600,height=400,bg='white')
canvas_gambar.pack(pady=20)

frame=LabelFrame(root,text='pilih warna dan hapus',font=('arial',13))
frame.pack(pady=20)

plh_warna=Button(frame,bg=warna,width=10,command=pilih_warna)
plh_warna.pack(pady=5,padx=10,side=LEFT)

hapus_layar=Button(frame,text="hapus layar",font=('arial',13),command=hapus_layarnya)
hapus_layar.pack(pady=5,padx=10,side=RIGHT)

canvas_gambar.bind('<Button-1>',ambil_xy)
canvas_gambar.bind('<B1-Motion>',gambar)




root.mainloop()