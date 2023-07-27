# Assalamualaikum, kali ini saya akan coba belajar Tkinter dan SQLite3, mungkin untuk video ini fokus ke SQLite dulu

import sqlite3

try:
	koneksi=sqlite3.connect('belajar.db')
	print('database telah dibuat')
	kursor=koneksi.cursor()
except:
	print('program error')
	pass
	

# membuat tabel dalam database
kursor.execute('CREATE TABLE IF NOT EXISTS data_siswa (id INTEGER AUTOINCREAMENT,nama TEXT, kelas TEXT)')

# Memasukkan data dalam tabel
for i in range(10):
	kursor.execute('INSERT INTO data_siswa VALUES ('nama_'+str(i),'kelas_'+str(i)')
	print(f'data ke {i} berhasil dimasukkan')