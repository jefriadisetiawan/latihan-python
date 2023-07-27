import random

print('\n==== SIMULASI PERSILANGAN MONOHIBRIDA DOMINAN-RESESIF ====\n')

banyak=input('masukkan berapa kali disilangkan: ')
print('\n')
banyak=int(banyak)

parental1=['merah','putih']
parental2=['merah','putih']

count=1
hasil=[]
while count<=banyak:
	gen1=random.choice(parental1)
	gen2=random.choice(parental2)
	gen=gen1+' '+gen2
	hasil.append(gen)
	count+=1
merah_merah=0
merah_putih=0
putih_putih=0

merah=0
putih=0

for i in range(0,banyak):
	if hasil[i]=='merah merah':
		merah_merah+=1
		merah+=1
	elif hasil[i]=='putih putih':
		putih_putih+=1
		putih+=1
	else:
		merah_putih+=1
		merah+=1

# persen genotipe
persen_merah_merah=round((merah_merah/banyak)*100)
persen_merah_putih=round((merah_putih/banyak)*100)
persen_putih_putih=round((putih_putih/banyak)*100)


# persen fenotipe
persen_merah=round((merah/banyak)*100)
persen_putih=round((putih/banyak)*100)


print('perbandingan genotipe')
print(f'merah merah = {merah_merah} => {persen_merah_merah} %')
print(f'merah putih = {merah_putih} => {persen_merah_putih} %')
print(f'putih putih = {putih_putih} => {persen_putih_putih} %')
print(f'perbandingan merah merah : merah putih : putih putih = {round(persen_merah_merah/25)} : {round(persen_merah_putih/25)} : {round(persen_putih_putih/25)}')
print('\n')
print('perbandingan fenotipe')
print(f'merah = {merah} => {persen_merah} %')
print(f'putih = {putih} => {persen_putih} %')
print(f'perbandingan merah merah : merah putih : putih putih = {round(persen_merah/25)} : {round(persen_putih/25)}')
print('\n')

