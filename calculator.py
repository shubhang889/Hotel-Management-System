from tkinter import *

def btn(numbers):
    global operator
    operator = operator+str(numbers)
    txt_input.set(operator)

def clear():
    global operator
    operator =''
    txt_input.set('')
    # Display.insert(0,'Start Calculating...')

def Equal():
    global operator
    sumup = float(eval(operator))
    txt_input.set(sumup)
    operator = ''

root = Tk()
root.title('Calculator')

operator = ''
txt_input = StringVar(value = 'Start Calculating...')

# ---------------------------------------------------------SCREEN-------------------------------------------------------
Display = Entry(root,font = ('arial',20,'bold') , bg = 'green' , fg = 'white' , justify = 'right' , bd = 40,
                textvariable = txt_input)
Display.grid(columnspan = 4)

# ---------------------------------------------------------row1---------------------------------------------------------

btn7 = Button(text = '7' , font=('arial',20,'bold') , padx=20,pady=10,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(7)).grid(row=1,column=0)
btn8 = Button(text = '8' , font=('arial',20,'bold') , padx=20,pady=10,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(8)).grid(row=1,column=1)
btn9 = Button(text = '9' , font=('arial',20,'bold') , padx=20,pady=10,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(9)).grid(row=1,column=2)
btnC = Button(text = 'C' , font=('arial',20,'bold') , padx=18,pady=10,fg= 'black' , bg='purple' , bd = 8
              , command = clear).grid(row=1,column=3)

# -------------------------------------------------------row2-----------------------------------------------------------

btn4 = Button(text = '4' , font=('arial',20,'bold') , padx=20,pady=10,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(4)).grid(row=2,column=0)
btn5 = Button(text = '5' , font=('arial',20,'bold') , padx=20,pady=10,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(5)).grid(row=2,column=1)
btn6 = Button(text = '6' , font=('arial',20,'bold') , padx=20,pady=10,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(6)).grid(row=2,column=2)
btnplus = Button(text = '+' , font=('arial',20,'bold') , padx=20,pady=10,fg='black' , bg='orange' , bd = 8
              , command = lambda: btn('+')).grid(row=2,column=3)


# ------------------------------------------------------row3------------------------------------------------------------

btn1 = Button(text = '1' , font=('arial',20,'bold') , padx=20,pady=10,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(1)).grid(row=3,column=0)
btn2 = Button(text = '2' , font=('arial',20,'bold') , padx=20,pady=10,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(2)).grid(row=3,column=1)
btn3 = Button(text = '3' , font=('arial',20,'bold') , padx=20,pady=10,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(3)).grid(row=3,column=2)
btnminus = Button(text = '-' , font=('arial',20,'bold') , padx=25,pady=10,fg='black' , bg='orange' , bd = 8
              , command = lambda: btn('-')).grid(row=3,column=3)

# ------------------------------------------------------row4------------------------------------------------------------

btn0 = Button(text = '0' , font=('arial',20,'bold') , padx=20,pady=10,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(0)).grid(row=4,column=0)
btndot = Button(text = '.' , font=('arial',20,'bold') , padx=24,pady=10,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(7)).grid(row=4,column=1)
btndiv = Button(text = '/' , font=('arial',20,'bold') , padx=25,pady=10,fg='black' , bg='orange' , bd = 8
              , command = lambda: btn('/')).grid(row=4,column=2)
btnmul = Button(text = 'X' , font=('arial',20,'bold') , padx=20,pady=10,fg='black' , bg='orange' , bd = 8
              , command = lambda: btn('*')).grid(row=4,column=3)

# -----------------------------------------------------row5-------------------------------------------------------------

btneqals = Button(text = '=' , font=('arial',20,'bold') , padx=66,pady=10,fg='black' , bg='red' , bd = 8
              ,command = Equal).grid(row=5,column=0,columnspan=2)
btnOB = Button(text = '(' , font=('arial',20,'bold') , padx=25,pady=10,fg='black' , bg='orange' , bd = 8
             , command = lambda: btn('(') ).grid(row=5,column=2)
btnCB = Button(text = ')' , font=('arial',20,'bold') , padx=25,pady=10,fg='black' , bg='orange' , bd = 8
              , command = lambda: btn(')')).grid(row=5,column=3)
# btn7 = Button(text = '7' , font=('arial',30,'bold') , padx=30,pady=15,fg='black' , bg='orange' , bd = 8
#               ).grid(row=1,column=0)

# -----------------------------------------------------END--------------------------------------------------------------

root.mainloop()
