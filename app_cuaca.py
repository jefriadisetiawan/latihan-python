# Assalamualaikum, saya akan mencoba membuat aplikasi perkiraan cuaca
# dengan memanfaatkan API dari openweathermaps.org
# API yang digunakan Current Weather Data dan Geolocation

from tkinter import *
import requests
import json

root=Tk()
root.title('weather app')
root.geometry('300x300')

def cari():
	# mencari kota
	API_key='8f06001c7a867a70336295d4c1c525cd'
	kota=entry_kota.get()
	url_kota=f'http://api.openweathermap.org/geo/1.0/direct?q={kota}&limit=5&appid={API_key}'
	hasil_kota=requests.get(url_kota)
	hasil_kota=json.loads(hasil_kota.content)
	nama_kota=hasil_kota[0]['name']
	lat=hasil_kota[0]['lat']
	lon=hasil_kota[0]['lon']

	# mencari cuaca
	url_cuaca=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
	hasil_cuaca=requests.get(url_cuaca)
	hasil_cuaca=json.loads(hasil_cuaca.content)
	cuacanya=hasil_cuaca['weather'][0]['main']
	temperatur=hasil_cuaca['main']['temp']
	tekanan_udara=hasil_cuaca['main']['pressure']
	kelembaban=hasil_cuaca['main']['humidity']
	state=hasil_kota[0]['country']

	hasil_pencarian=f'	hasil pencarian :\nkota : {nama_kota}\nnegara : {state}\ncuaca : {cuacanya}\ntemperatur : {temperatur}\ntekanan udara : {tekanan_udara}\nkelembaban : {kelembaban}'
	label_hasil.config(text=hasil_pencarian)

	entry_kota.delete(0,END)

label_judul=Label(root,text='masukkan nama kota yang dicari', font=('arial',12,'bold'))
label_judul.pack(padx=5,pady=5)

entry_kota=Entry(root,width=25,font=('arial',12),bg='white')
entry_kota.pack(padx=5,pady=5)

tombol_cari=Button(root,text='cari',font=('arial',12,'bold'),command=cari)
tombol_cari.pack(padx=5,pady=5)

label_hasil=Label(root,font=('arial',12),justify='left')
label_hasil.pack(padx=5,pady=5)


root.mainloop()