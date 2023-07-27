import random

a=input('masukkan banyak persilangan : ')
banyak=int(a)

sifat1=['BB','Bb','bB','bb']
sifat2=['KK','Kk','kK','kk']

bulat_kuning=0
bulat_hijau=0
kisut_kuning=0
kisut_hijau=0

for i in range(banyak):
	gen1=random.choice(sifat1)
	gen2=random.choice(sifat2)
	if gen1=='bb':
		fen1='kisut'
	else:
		fen1='bulat'
	if gen2=='kk':
		fen2='hijau'
	else:
		fen2='kuning'
	fenotipe=fen1+'_'+fen2
	if fenotipe=='bulat_kuning':
		bulat_kuning+=1
	elif fenotipe=='bulat_hijau':
		bulat_hijau+=1
	elif fenotipe=='kisut_kuning':
		kisut_kuning+=1
	else:
		kisut_hijau+=1

print(f'Bulat Kuning = {bulat_kuning} => {round((bulat_kuning/banyak)*100)} => {round(((bulat_kuning/banyak)*100)/25)}')
print(f'Bulat Hijau = {bulat_hijau} => {round((bulat_hijau/banyak)*100)} => {round(((bulat_hijau/banyak)*100)/25)}')
print(f'Kisut Kuning = {kisut_kuning} => {round((kisut_kuning/banyak)*100)} => {round(((kisut_kuning/banyak)*100)/25)}')
print(f'Kisut Hijau = {kisut_hijau} => {round((kisut_hijau/banyak)*100)} => {round(((kisut_hijau/banyak)*100)/25)}')

