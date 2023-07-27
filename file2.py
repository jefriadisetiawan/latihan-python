import matplotlib.pyplot as plt

a=[]
b=[]

file=open('data.txt','r').read()
isi=file.split('\n')
for i in isi:
	if i=='':
		pass
	else:
		x,y=i.split(',')
		a.append(int(x))
		b.append(int(y))

print(f'a = {a}')
print(f'b = {b}')

plt.plot(a,b)
plt.show()