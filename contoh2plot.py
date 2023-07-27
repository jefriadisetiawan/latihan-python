'''
import matplotlib.pyplot as plt
10with open(’data.txt’, ’r’) as f:
l = f.read().strip().split(’\n’)
x = []
y = []
for i in l:
xny = i.split(’,’)
x.append(int(xny[0]))
y.append(int(xny[1]))
# sebelum di plot, mari kita ubah tampilan
fig = plt.figure()
rect = fig.patch
rect.set_facecolor(’#31312e’)
ax1 = fig.add_subplot(1, 1, 1, axisbg=’grey’)
ax1.plot(x, y, ’c’, linewidth=3.3)
# plot dimulai
ax1.set_title(’matplotlib example title’)
ax1.set_xlabel(’matplot x label’)
ax1.set_ylabe
'''
import matplotlib.pyplot as plt

with open('data.csv','r') as f :
	l=f.read().strip().split('\n')
	#print(l)

x=[]
y=[]

for i in l:
	temp=i.split(',')
	x.append(temp[0])
	y.append(temp[1])

#print(x)
#print(y)
fig=plt.figure()
rect = fig.patch
rect.set_facecolor('white')
ax1=fig.add_subplot(1,1,1,axisbg='white')
ax1.plot(x,y,'c',linewidth=3)
ax1.set_title('contoh grafik')
ax1.set_xlabel('tanggal')
ax1.set_ylabel('jumlah')
plt.show()
