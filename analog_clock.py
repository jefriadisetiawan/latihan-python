# Assalamualaikum wr wb
# saya akan mencoba membuat jam analog dengan tkinter

from tkinter import *
import time
import math

pusat_x=200
pusat_y=200



def update_jam():
	global pusat_x,pusat_y
	global detik, menit, jam
	
	jam=int(time.strftime('%I'))
	menit=int(time.strftime('%M'))
	detik=int(time.strftime('%S'))
	# setiap detik sudut yang terbuat 360/60 = 6 jam
	
	jarum_detik=180
	jarum_jam=130
	jarum_menit=150

	sudut_detik=detik*6
	sin_detik=jarum_detik*math.sin(math.radians(sudut_detik))
	cos_detik=jarum_detik*math.cos(math.radians(sudut_detik))*-1

	sudut_menit=menit*6
	sin_menit=jarum_menit*math.sin(math.radians(sudut_menit))
	cos_menit=jarum_menit*math.cos(math.radians(sudut_menit))*-1
	
	sudut_jam=(jam*30)+(sudut_menit/30)
	sin_jam=jarum_jam*math.sin(math.radians(sudut_jam))
	cos_jam=jarum_jam*math.cos(math.radians(sudut_jam))*-1

	canvas.coords(jarum_penunjuk_detik, pusat_x,pusat_y,pusat_x+sin_detik,pusat_y+cos_detik)
	canvas.coords(jarum_penunjuk_menit, pusat_x,pusat_y,pusat_x+sin_menit,pusat_y+cos_menit)
	canvas.coords(jarum_penunjuk_jam, pusat_x,pusat_y,pusat_x+sin_jam,pusat_y+cos_jam)

	root.after(1000,update_jam)

root=Tk()
root.title('jam analog')
root.geometry('400x400')

gmb_jam=PhotoImage(file='jam.png')
canvas=Canvas(root,width=400,height=400)
canvas.create_image(200,200,image=gmb_jam)

jarum_penunjuk_detik=canvas.create_line(pusat_x,pusat_y,pusat_x+180,pusat_y+180,width=5,fill='red')
jarum_penunjuk_menit=canvas.create_line(pusat_x,pusat_y,pusat_x+130,pusat_y+130,width=5,fill='green')
jarum_penunjuk_jam=canvas.create_line(pusat_x,pusat_y,pusat_x+150,pusat_y+150,width=5,fill='blue')

canvas.pack()

update_jam()


root.mainloop()