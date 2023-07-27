# Assalamualaikum percobaan membuat grafik sinusoidal tkinter python

from tkinter import *
from math import *



root=Tk()
root.geometry('600x600')

canvas=Canvas(root,width=550,height=400,bg='white')


canvas.create_line(0,0,50,50,fill='red',width=2)


for item in range(1,360):
	x1=item-1
	y1=(200+sin(radians(x1)))
	x2=item
	y2=(200+sin(radians(x2)))
	canvas.create_line(x1,y1,x2,y2,fill='red',width=2)


canvas.pack(pady=10)

print(canvas.winfo_height())
print(canvas.winfo_width())
root.mainloop()