# Assalamualaikum wr wb, dalam video ini saya akan mencoba membuat GUI message box sederhana di python

from tkinter import *
from tkinter import messagebox


window=Tk()
window.title("simple app")
window.geometry("250x200")

NAMA=StringVar()

def proses():
	isi=f"assalamualaikum saudara {NAMA.get()}"
	messagebox.showinfo(title="informasi",message=isi)

# 1. membuat widget GUI
frame=LabelFrame(window, text="data")
frame.pack(padx=5,pady=5)
nama_label=Label(frame,text="masukkan nama anda")
nama_label.pack(padx=5,pady=5)
nama_entry=Entry(frame,textvariable=NAMA,font=("arial",14))
nama_entry.pack(padx=5,pady=5,fill='x')
tombol_ok=Button(window, text="silahkan",command=proses)
tombol_ok.pack(padx=5,pady=5,fill='x')



window.mainloop()

# wassalamualaikum wr wb, semoga bermanfaat