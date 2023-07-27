# Assalamualaikum, saya akan mencoba belajar membuat jam digital dengan tkinter

from tkinter import *
import time


root=Tk()
root.geometry("300x100")

label_judul=Label(root,text="Jam Digital",font=("arial bold",18))
label_judul.pack(padx=2,pady=2)

def mulai():
	while True:
		jam=time.ctime()
		label_jam['text']=jam
		#print(jam)
		root.mainloop()
		time.sleep(1)

	
		

label_jam=Label(root,text="",font=("arial bold",14))
label_jam.pack(padx=2,pady=2)

mulai()

#tombol=Button(root,text="ON",font=("arial bold",14),command=mulai)
#tombol.pack(padx=2,pady=2)












