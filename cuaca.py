# Assalamualaikum wr wb
# pada video ini saya akan mencoba membuat aplikasi perkiraan cuaca
# dengan tkinter dan API 

from tkinter import *
import requests
import json
'''
root=Tk()



root.mainloop()
'''
# ambil kota
ambil_kota=input('masukkan nama kota :')
url_kota='https://geocoding-api.open-meteo.com/v1/search?name=' + ambil_kota
kota=requests.get(url_kota)
kota1=json.loads(kota.content)
nama_kota=kota1['results'][0]['name']
lat=kota1['results'][0]['latitude']
lon=kota1['results'][0]['longitude']
print(f'{nama_kota} {lat} {lon}')

API_key='8f06001c7a867a70336295d4c1c525cd'
url_cuaca=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
cuaca=requests.get(url_cuaca)
cuaca1=json.loads(cuaca.content)
for i in cuaca1:
	print(f'{i} = {cuaca1[i]}')