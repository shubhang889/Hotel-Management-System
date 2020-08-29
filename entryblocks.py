from tkinter import *

root = Tk()
# root.geometry('500x300+200+100')
def dele():
    en1.delete(0,END)
    en2.delete(0,END)
    en3.delete(0,END)
    en4.delete(0,END)
root.title('data entry blocks')
Label(text='First Name').grid(row=0,column=0)
Label(text='Last Name').grid(row=1,column=0)
Label(text='Occupation').grid(row=2,column=0)
Label(text='Email address').grid(row=3,column=0)


en1 = Entry()
en1.grid(row=0,column=1)
en2 = Entry()
en2.grid(row=1,column=1)
en3 = Entry()
en3.grid(row=2,column=1)
en4 = Entry()
en4.grid(row=3,column=1)

btn1 = Button(text='Delete' , command = dele).grid(row=4,column=1)
btn = Button(text='Close Program' , command=root.destroy).grid(row=5,column=1)

root.mainloop()
