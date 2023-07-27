# Assalamulaikum wr wb, saya akan mencoba membuat aplikasi jam digital dengan tkinter

from tkinter import *
import time

root=Tk()
root.title('jam digital')

def update_jam():
	jam=time.strftime('%I')
	menit=time.strftime('%M')
	detik=time.strftime('%S')
	pm_atau_am=time.strftime('%p')
	jam_nya=f'{jam} : {menit} : {detik} {pm_atau_am}'
	label_jam.config(text=jam_nya)
	root.after(1000,update_jam)

label_jam=Label(root,text='00:00:00',font=('helvetica',70,'bold'))
label_jam.pack()

update_jam()

root.mainloop()


