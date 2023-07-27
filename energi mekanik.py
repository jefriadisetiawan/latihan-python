# Assalamualaikum, kali ini saya ingin mencoba membuat program sederhana di pyhton, menghitung energi potensial dan kinetik saat benda jatuh bebas

# percepatan = 10 m/s2 dan kecepatan awal = 0

# ===================================================

massa=int(input("massa benda = "))
tinggi=int(input("ketinggian benda = "))

waktu=0
h=tinggi

while h>0:
    h=tinggi    
    vt=0+(10*waktu)
    EK=0.5*massa*(vt*vt)
    s=0.5*10*(waktu*waktu)
    h=tinggi-s
    EP=massa*10*h
    if EP<0:
        break
    print(f"pada detik ke {waktu} EP = {EP} dan EK = {EK} sehingga EM = {EP+EK}")
    waktu+=1
 
