# Assalamualaikum, dalam kesempatan ini saya akan mencoba membuat image galery sederhana
# karena ukuran gambar terlalu besar, akhirnya gambar saya resize

from tkinter import *


# membuat list foto
foto=['1.png','2.png','3.png','4.png']

global fotonya
global counter
global hitung
hitung=1
counter=0



def prev_foto():
	global counter
	global fotonya
	global hitung
	hitung-=1
	if hitung==1:
		tombol_prev['state']=DISABLED
		counter=0
		hitung=1
	else:
		tombol_prev['state']=NORMAL
		tombol_next['state']=NORMAL
		counter-=1
	judul_foto['text']=f"foto ke {hitung}"
	fotonya=PhotoImage(file=foto[counter])
	label_foto['image']=fotonya

def next_foto():
	global counter
	global fotonya
	global hitung
	hitung+=1
	if hitung==len(foto):
		tombol_next['state']=DISABLED
		counter=len(foto)-1
		hitung=len(foto)
	else:
		tombol_next['state']=NORMAL
		tombol_prev['state']=NORMAL
		counter+=1
	judul_foto['text']=f"foto ke {hitung}"
	fotonya=PhotoImage(file=foto[counter])
	label_foto['image']=fotonya






root=Tk()
root.title("galeri foto")
root.geometry('350x500')



judul=Label(root,text="geleri foto",font=("arial",12))
judul.pack(padx=5,pady=5)

frame1=Frame(root)
frame1.pack(padx=5,pady=5)

fotonya=PhotoImage(file=foto[counter])
label_foto=Label(frame1,image=fotonya)
label_foto.pack(padx=5,pady=5)

tombol_prev=Button(root,text="previous",state=DISABLED,command=prev_foto)
tombol_prev.pack(padx=5,pady=5)

tombol_next=Button(root,text="next",command=next_foto)
tombol_next.pack(padx=5,pady=5)

judul_foto=Label(root,text=f"foto ke {counter+1}")
judul_foto.pack(padx=5,pady=5)

root.mainloop()