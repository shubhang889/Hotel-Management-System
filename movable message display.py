from tkinter import*
import time
msg = 'PROGRAMMING IS GOOD FOR ALL'
text1=''
n=0

def display1():
    global msg,text1,n
    for t in range(len(msg)):
        for k in range(t):
            text1+=' '
        for l in range(len(msg)-t):
            text1+=msg[l]
        text1=text1.strip()
        mygui.update()
        mygui.after(100)
        text1=text1.strip()
        scroll_text.set('')
        scroll_text.set(text1)
        text1=''
    scroll_text.set('')

def display2():
    global msg,text1,n
    for t in range(len(msg)):
        text1=''
        # msg=scroll_text.get()
        for k in range(50-t):
            text1+=' '
        for l in range(t+1):
            text1+=msg[l]
        # text1=text1.strip()
        mygui.update()
        mygui.after(100)
        # text1=text1.strip()
        scroll_text.set('')
        scroll_text.set(text1)
        text1=''
    msg=scroll_text.get().strip()
    for t in range(len(msg)):
        j=t
        for k in range(t+1):
            text1+=' '
        for l in range(len(msg)-t):
            text1+=msg[j]
            j+=1
        text1=text1.strip()
        mygui.update()
        mygui.after(100)
        # text1=text1.strip()
        scroll_text.set('')
        scroll_text.set(text1)
        text1=''
    scroll_text.set('')

def display3():
    global msg,text1,n
    for t in range(len(msg)):
        for k in range(t):
            text1+=' '
        for l in range(len(msg)-t):
            text1+=msg[l]
        # text1=text1.strip()
        mygui.update()
        mygui.after(100)
        # text1=text1.strip()
        scroll_text.set('')
        scroll_text.set(text1)
        text1=''
    scroll_text.set('')

def display4():
    global msg,text1,n
    for t in range(len(msg)):
        j=t
        for k in range(t):
            text1+=' '
        for l in range(len(msg)-t):
            text1+=msg[j]
            j+=1
        # text1=text1.strip()
        mygui.update()
        mygui.after(100)
        # text1=text1.strip()
        scroll_text.set('')
        scroll_text.set(text1)
        text1=''
    scroll_text.set('')

def display5():
    global msg,text1,n
    for t in range(len(msg)):
        j=t
        for k in range(t):
            text1+=' '
        for l in range(len(msg)-t):
            text1+=msg[j]
            j+=1
        text1=text1.strip()
        mygui.update()
        mygui.after(100)
        # text1=text1.strip()
        scroll_text.set('')
        scroll_text.set(text1)
        text1=''
    scroll_text.set('')

def display6():
    global msg,text1,n
    for t in range(len(msg)):
        for k in range(len(msg)-t):
            text1+=' '
        for l in range(t+1):
            text1+=msg[l]
        # text1=text1.strip()
        mygui.update()
        mygui.after(100)
        # text1=text1.strip()
        scroll_text.set('')
        scroll_text.set(text1)
        text1=''
    msg=scroll_text.get()
    for t in range(len(msg)):
        j=t
        for k in range(t+1):
            text1+=' '
        for l in range(len(msg)-t):
            text1+=msg[j]
            j+=1
        text1=text1.strip()
        mygui.update()
        mygui.after(100)
        # text1=text1.strip()
        scroll_text.set('')
        scroll_text.set(text1)
        text1=''
    scroll_text.set('')


mygui = Tk()
scroll_text = StringVar()
mygui.title('Scroll Text')
mygui.geometry('400x360+400+200')
mygui.configure(bg='red')
text2 = Entry(mygui,textvariable = scroll_text,width = 50, bg='white',font=('arial',20,'bold')).grid(row=0,column=0)
Label(text='Click to Scroll Message',padx=10,bg='red',fg='black',font=10).grid(row=1,column=0,sticky=W)
button1 = Button(mygui, text='Scroll1',fg='black',font=('arial',10,'bold'), command=display1, height=3,width=13).place(x=80,y=80)
button2 = Button(mygui, text='Scroll2',fg='black',font=('arial',10,'bold'), command=display2,height=3,width=13).place(x=220,y=80)
button3 = Button(mygui, text='Scroll3',fg='black',font=('arial',10,'bold'),height=3,width=13, command=display3).place(x=80,y=160)
button4 = Button(mygui, text='Scroll4',fg='black',font=('arial',10,'bold'),height=3,width=13, command=display4).place(x=220,y=160)
button5 = Button(mygui, text='Scroll5',fg='black',font=('arial',10,'bold'),height=3,width=13, command=display5).place(x=80,y=240)
button6 = Button(mygui, text='Scroll6',fg='black',font=('arial',10,'bold'),height=3,width=13, command=display6).place(x=220,y=240)



mygui.mainloop()
