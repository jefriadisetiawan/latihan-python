'''
IPA kelas 9
BBKK = biji bulat warna kuning (dominan) x bbkk (biji kisut warna hijau, resesif) => BbKk (biji bulat warna kuning)
BbKk x BbKk
'''
import random

print(' \nPERSILANGAN DIHIBRIDA\n')
banyak=input('masukkan banyak persilangan : ')
banyak=int(banyak)

# simulasi mendapatkan gamet
gen1=['BB','Bb','bB','bb']
gen2=['KK','Kk','kK','kk']

hasil=[]

# fenotipe
bltkng=0
blthju=0
kstkng=0
ksthju=0


for i in range(banyak):
	g1=random.choice(gen1)
	g2=random.choice(gen2)
	gen_jadi=g1+g2
	hasil.append(gen_jadi)
	if g1=='bb':
		bentuk='kisut'
	else:
		bentuk='bulat'
	if g2=='kk':
		warna='hijau'
	else:
		warna='kuning'
	# memasukkan fenotipe
	if bentuk=='bulat':
		if warna=='kuning':
			bltkng+=1
		else:
			blthju+=1
	if bentuk=='kisut':
		if warna=='kuning':
			kstkng+=1
		else:
			ksthju+=1
		
# perbandingan fenotipe
a=round(bltkng/ksthju)
b=round(blthju/ksthju)
c=round(kstkng/ksthju)
d=round(ksthju/ksthju)


print('=== hasil fenotipe ===')
print(f'bulat kuning = {bltkng} => {a}')
print(f'bulat hijau = {blthju} => {b}')
print(f'kisut kuning = {kstkng} => {c}')
print(f'kisut hijau = {ksthju} => {d}')
print('\n')


