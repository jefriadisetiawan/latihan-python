'''
Assalamualaikum wr wb, dalam video ini saya akan mencoba membuat grafik dinamis / live graph
'''
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import random
from matplotlib import style

style.use('fivethirtyeight')



fig=plt.figure()
grafik=fig.add_subplot(1,1,1)

def nilai_x():
	file1=open('data.txt','r')
	isi=file1.read()
	ukuran=isi.split('\n')
	count=0
	for item in ukuran:
		count=count+1
	return count
	file1.close()

def nilai_y():
	nilai=random.randrange(14000,15000)
	return nilai
	
def update():
	nilaiX=nilai_x()
	nilaiY=nilai_y()
	file2=open('data.txt','a')
	string=f'{nilaiX},{nilaiY}\n'
	file2.write(string)
	file2.close()

def animasi(event):
	update()
	file3=open('data.txt','r')
	nilai=file3.read()
	nilai_raw=nilai.split('\n')
	print(nilai)
	x=[]
	y=[]
	for raw in nilai_raw:
		if raw=='':
			pass
		else:
			xx,yy=raw.split(',')
			x.append(int(xx))
			y.append(int(yy))
	grafik.clear()
	grafik.set_title('kurs rupiah terhadap dolar')
	grafik.set_xlabel('hari')
	grafik.set_ylabel('nilai rupiah')
	#grafik.set_xticks(x)
	grafik.plot(x,y)
	

ani=animation.FuncAnimation(fig,animasi,interval=500)
plt.show()

