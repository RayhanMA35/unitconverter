from tkinter import *

window=Tk()
window.title('Unit Converter')
window.minsize(width=300,height=100)
window.config(padx=100,pady=50)
satuan = ['KM' , 'HM', 'DAM', 'M', 'DM', 'CM', 'MM']
ukur = [10**i for i in range(7)]

# eksekusi tombol
def restart():
    result.config(text='')
    reset.grid_forget()
    entry.delete(0, END)


# menentukan apakah pecahan atau tidak
def calculation(hasil):

    hasil2=str("{:.2f}".format(hasil))
    if '.00' in hasil2:
        result.config(text=f'{int(hasil)}')
    else:
        result.config(text=hasil2)



def enter():
    one=clicked.get()
    two=clicked2.get()
    input_=float(entry.get())

    index1=satuan.index(one)
    index2=satuan.index(two)
    cal=index1-index2
    if cal<0:
        cal*=-1
        hasil = input_ * float(ukur[cal])
        calculation(hasil)
    elif cal>0:
        hasil= input_/float(ukur[cal])
        calculation(hasil)
    else:
        hasil = input_ * 1.0
        calculation(hasil)
    # memunculkan tombol reset
    reset.grid(column=1,row=3)


# User Interface

# Dropdown
clicked=StringVar()
clicked.set(satuan[0])
drop=OptionMenu(window,clicked,*satuan)
drop.config(width=2)
drop.grid(column=0,row=0)

clicked2=StringVar()
clicked2.set(satuan[0])
drop2=OptionMenu(window,clicked2,*satuan)
drop2.config(width=2)
drop2.grid(column=2,row=0)

# input penguna
entry=Entry(width=5)
entry.grid(column=0,row=1)

# teks
equal=Label(text='Equla to')
equal.grid(column=1,row=0)

result=Label(text='')
result.grid(column=2,row=1)

# tombol-tombol
process=Button(text='=',command=enter,bg='orange',fg='white')
process.grid(column=1,row=1)

reset=Button(text='Reset',command=restart)








window.mainloop()