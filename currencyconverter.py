from tkinter import *
from tkinter import ttk

root = Tk()
# root.geometry('500x300+400+200')

def convert():
    var2 = indicator.get()
    var3 = var1.get()
    if var2=='US':
        e3.delete(0,END)
        var4 = ((var3*0.013362),'USD')
        e3.insert(0,var4)
    elif var2=='Australia':
        e3.delete(0,END)
        var4 = ((var3*0.018485),'Australian Dollar')
        e3.insert(0,var4)
    elif var2=='Canada':
        e3.delete(0,END)
        var4 = ((var3*0.017601),'Canadian Dollar')
        e3.insert(0,var4)
    elif var2=='Europe':
        e3.delete(0,END)
        var4 = ((var3*0.011231),'Euro')
        e3.insert(0,var4)
    elif var2=='Pakistan':
        e3.delete(0,END)
        var4 = ((var3*2.248897),'Pakistani Rupee')
        e3.insert(0,var4)
    elif var2=='Singapore':
        e3.delete(0,END)
        var4 = ((var3*0.018259),'Singapore Dollar')
        e3.insert(0,var4)
    elif var2=='Switzerland':
        e3.delete(0,END)
        var4 = ((var3*0.012167),'Swiss Franc')
        e3.insert(0,var4)
    elif var2=='China':
        e3.delete(0,END)
        var4 = ((var3*0.092476),'Yuan')
        e3.insert(0,var4)
    else:
        e3.delete(0,END)
        var4 = ('INVALID COUNTRY')
        e3.insert(0,var4)

def Clear():
    e1.delete(0,END)
    e3.delete(0,END)


root.title('Currency Converter')

var1 = IntVar()
# var2 = IntVar()
indicator = StringVar(value = 'Choose a Country')
Label(text = 'Currency Converter' , font = ('arial',20 , 'bold')).grid(row=1,column=1)

Label(text = 'Amount(Rs.)' , font = ('arial',20,'bold')).grid(row=2,sticky=W)
e1 = Entry(width=30,font = ('arial',20,'bold'),textvariable=var1)
e1.grid(row=2,column=1)

Label(text = 'Country' , font = ('arial',20,'bold')).grid(row=3,sticky=W)
e2 = ttk.Combobox(width=30,font = ('arial',20,'bold'),textvariable=indicator)
# ttk.Label(text='Select a Country',font=('arial',20,'bold')).grid(row=3,column=1)
e2['values'] = ('US','Australia','Canada','Europe','Pakistan','Singapore','Switzerland','China')
e2.grid(row=3,column=1)

Label(text = 'Amount After Conversion' , font = ('arial',20,'bold')).grid(row=4,sticky=W)
e3 = Entry(width=30,font = ('arial',20,'bold'))
e3.grid(row=4,column=1)

btn1 = Button(text = 'Convert' , font = ('arial',15,'bold'),width=20,command=convert).grid(row=5,column=1,sticky=W)

btn2 = Button(text = 'Clear' , font = ('arial',15,'bold'),width=20,command = Clear).grid(row=5,column=1,sticky=E)

btn3 = Button(text='CLOSE', font = ('arial',15,'bold') , command = root.destroy).grid(row=6,column=1)

root.mainloop()
