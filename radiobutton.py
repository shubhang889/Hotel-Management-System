
from tkinter import *

root = Tk()
def language():
    r=v.get()
    if r==1:
        mylabel4 = Label(text='         C++ Programming        ').pack()
    elif r==2:
        mylabel1 = Label(text='       Python Programming       ').pack()
    elif r==3:
        mylabel2 = Label(text='          C Programming         ').pack()
    elif r==4:
        mylabel3 = Label(text='         PHP Programming        ').pack()

root.geometry('500x300+100+100')
root.title('radio buttons')

v = IntVar()
v.set(1)
mylabel = Label(text='Computer Programming Language').pack()
# Radiobutton(text='C++',padx=10,pady=20,variable=v,value=1).pack()
# Radiobutton(text='Python',padx=10,pady=20,variable=v,value=2).pack()
# Radiobutton(text='C',padx=10,pady=20,variable=v,value=3).pack()
# Radiobutton(text='PHP',padx=10,pady=20,variable=v,value=4).pack()
#
# Radiobutton(text='C++',padx=10,pady=20,variable=v,value=1,command=language).grid(row=1,column=0)
# Radiobutton(text='Python',padx=10,pady=20,variable=v,value=2,command=language).grid(row=1,column=1)
# Radiobutton(text='C',padx=10,pady=20,variable=v,value=3,command=language).grid(row=1,column=2)
# Radiobutton(text='PHP',padx=10,pady=20,variable=v,value=4,command=language).grid(row=1,column=3)

radios = [('C++',1),('Python',2),('C',3),('PHP',4)]

for rad,val in radios:
    Radiobutton(text=rad,padx=10,variable=v,value=val,command=language,indicatoron=0).pack(anchor=W)

btn2 = Button(text = 'END' , fg='red',font=12 , command=root.destroy).pack()
root.mainloop()
