from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("belajar listbox")

def pesan_makanan():
	messagebox.askokcancel(title='konfirmasi pesanan',message=f'makanan yang anda pesan adalah {list_makanan.get(list_makanan.curselection())}')


makanan=['soto','rawon','pecel','sate','gulai','rendang','bakso','siomay','bubur','urap']

judul_label=Label(window,text='pilih makanan')
judul_label.pack(padx=10,pady=5)

list_makanan=Listbox(window,bg='white',fg='black')
list_makanan.pack(padx=10,pady=5)

for i in range(len(makanan)):
	list_makanan.insert(i,makanan[i])

tombol_pesan=Button(window,text="pesan makanan",command=pesan_makanan)
tombol_pesan.pack(padx=10,pady=5)

window.mainloop()