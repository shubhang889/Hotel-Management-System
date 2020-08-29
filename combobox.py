from tkinter import *
from tkinter import ttk

root = Tk()

def click():
    Label(text='   your selected fruit is: ' + var.get(),font=20).grid(row=2,column=1)\

root.title('combobox')

var = StringVar(value='Choose a fruit')
combo = ttk.Combobox(width=25,textvariable=var)
combo['values']  = ('Apple','Mango','Banana','papaya','guava')
combo.grid(row=0,column=1)

ttk.Label(text='Select a fruit').grid(row=0,column=0)
btn = Button(text='CLICK' , command=click).grid(row=1,column=1)
btn3 = Button(text='CLOSE',command = root.destroy).grid(row=1,column=0)

root.mainloop()
