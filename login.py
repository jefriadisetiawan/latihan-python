# Assalamualaikum, kali ini saya akan mencoba membuat Login GUI dengan tkinter python

from tkinter import *
from tkinter import messagebox


def login_app():
	user=user_entry.get()
	password=pass_entry.get()
	if user=="" and password=="":
		messagebox.showinfo("","username dan password tidak boleh kosong")
	elif user=="admin" and password=="admin":
		messagebox.showinfo("","selamat datang")
	else:
		messagebox.showinfo("","username atau password salah")


root=Tk()
root.title("Login")

judul=Label(root,text="Login GUI",font=("arial",13,"bold"))
judul.grid(row=0,column=0,columnspan=2,padx=2,pady=2)

frame1=LabelFrame(root,text="Masukkan username dan password anda")
frame1.grid(row=1,column=0,columnspan=2,padx=2,pady=2)

user=Label(frame1,text="username")
user.grid(row=0,column=0,padx=2,pady=2)

password=Label(frame1,text="password")
password.grid(row=1,column=0,padx=2,pady=2)

user_entry=Entry(frame1)
user_entry.grid(row=0,column=1,padx=2,pady=2)

pass_entry=Entry(frame1)
pass_entry.grid(row=1,column=1,padx=2,pady=2)

tombol=Button(root,text="Login",command=login_app)
tombol.grid(row=2,column=0,columnspan=2,padx=2,pady=2)




root.mainloop()