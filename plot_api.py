'''
Assalamualaikum wr wb. Percobaan membuat aplikasi yang menggunakan tkinter matplotlib dan API
semoga berhasil, Wassalamualaikum wr wb
'''

# import module yang dibutuhkan
from tkinter import *
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as tkg
import requests
import json

# programnya
'''
root=Tk()
root.geometry('700x550')
root.title('aplikasi plot dan API')
'''
url='https://data.jakarta.go.id/read-resource/json/data-realisasi-anggaran-pendapatan-dan-belanja-daerah/09527894-913d-4972-afc4-443212f283e3'
data_covid=requests.get(url)
data_covid_json=json.loads(data_covid.content)
print(data_covid_json)




#root.mainloop()