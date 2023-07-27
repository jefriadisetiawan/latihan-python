# Assalamualaikum, percobaan membuat game sederhana perkalian

import random


game=True
skor=0

while game==True:
	bilangan1=random.randrange(1,20)
	bilangan2=random.randrange(1,20)
	print(f'\nberapakah hasil perkalian berikut ini')
	jawab=input(str(bilangan1) + " x " + str(bilangan2) + " = ")
	jawaban_benar=bilangan1*bilangan2
	if jawab==str(jawaban_benar):
		skor+=10
		print(f'jawaban anda benar, skor anda = {skor}')
	else:
		print(f'jawaban anda salah, jawaban seharusnya adalah {jawaban_benar}\nskor anda = {skor}')
	konfirmasi=input('\napakah ingin melanjutkan game (y/t)?')
	if konfirmasi=='t':
		break 

print('akhir permainan\n')