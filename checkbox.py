from tkinter import *

root = Tk()
def show():
    r1=chkb1.get()
    r2=chkb2.get()
    r3=chkb3.get()
    r4=chkb4.get()
    if r1==1:
        Label(text='        C++     ').grid(row=6,sticky=W)
    if r2==1:
        Label(text='        Python  ').grid(row=7,sticky=W)
    if r3==1:
        Label(text='        C       ').grid(row=8,sticky=W)
    if r4   ==1:
        Label(text='        Ruby     ').grid(row=9,sticky=W)


root.geometry('500x300+200+100')
root.title('checkbox')

chkb1 = IntVar()
Checkbutton(text = 'C++' , variable=chkb1).grid(row=0,sticky=W)
chkb2=IntVar()
Checkbutton(text='Python',variable=chkb2).grid(row=1,sticky=W)
chkb3=IntVar()
Checkbutton(text='C',variable=chkb3).grid(row=2,sticky=W)
chkb4=IntVar()
Checkbutton(text='Ruby',variable=chkb4).grid(row=3,sticky=W)

btn = Button(text='get values' , bg='yellow' , fg='black',command=show).grid(row=4,sticky=W)
btn2 = Button(text = 'END' , fg='red',font=12 , command=root.destroy).grid(row=5,sticky=W)

root.mainloop()
