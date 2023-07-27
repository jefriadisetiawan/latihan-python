import requests as rs 
import json

input_respon=input('apakah ingin memproses (y/n)')
if input_respon=="y":
    url='https://kodepos-2d475.firebaseio.com/kota_kab/k69.json?print=pretty'
    reg=rs.get(url)
    jsn=json.loads(reg.content)
    for item in jsn:
        print(jsn)
else:
        print('akhir dari program')