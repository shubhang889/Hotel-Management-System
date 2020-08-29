from tkinter import *
import time
from tkinter import ttk


# -------------------------------------CALCULATOR FUNCTIONS------------------------------------

def btn(numbers):
    global operator
    operator = operator+str(numbers)
    txt_input.set(operator)

def clear():
    global operator
    operator =''
    txt_input.set('')
    Display.delete(0,END)
    Display.insert(0,'Start Calculating...')

def Equal():
    global operator
    sumup = float(eval(operator))
    txt_input.set(sumup)
    operator = ''

# -----------------------------------------TOTAL FUNCTIONS--------------------------

def TotalResult():
    # ----------------------Cost of Meal------------------
    varme1 = mealdicator.get()
    varme2 = meal1.get()
    if varme1=='Fried Rice':
        varme3 = (varme2*1.8)
        Cost.set(varme3)
    elif varme1=='Fried Rice and Chicken' :
        varme3 = (varme2*2.6)
        Cost.set(varme3)
    elif varme1=='Shawarma':
        varme3 = (varme2*2.0)
        Cost.set(varme3)
    elif varme1=='Cheese':
        varme3 = (varme2*1.0)
        Cost.set(varme3)
    elif varme1=='Burger':
        varme3 = (varme2*1.4)
        Cost.set(varme3)
    else:
        varme3=(varme2*0.0)
        Cost.set(varme3)
    # ----------------------Cost of Meal------------------
    varde1 = drinkitator.get()
    varde2 = drink1.get()
    if varde1=='Coke':
        varde3 = (varde2*1.0)
        Drink.set(varde3)
    elif varde1=='Pepsi' :
        varde3 = (varde2*1.0)
        Drink.set(varde3)
    elif varde1=='Beer':
        varde3 = (varde2*2.0)
        Drink.set(varde3)
    elif varde1=='Lemonade':
        varde3 = (varde2*1.2)
        Drink.set(varde3)
    else:
        varde3=(varde2*0.0)
        Drink.set(varde3)

    # -----------------------Delivery-----------------------------------
    num1=float(Cost.get())
    num2 = float(Drink.get())
    Delivery = (num1+num2)*0.5

    # ---------------------COST OF ROOM-----------------------------------

    room = v.get()
    null=0.0

    rvip=10
    rvip1=float(Delivery/(10*0.5))

    rnormal = 5
    rnormal1 = float(Delivery/(5*2.5))

    if room==1:
        if chkb1.get()==1:
            Service.set(rvip1)
            Room.set(rvip)
            delivery.set(Delivery)
        else:
            Service.set(null)
            Room.set(rvip)
            delivery.set(null)
    elif room==2:
        if chkb1.get()==1:
            Service.set(rnormal1)
            Room.set(rnormal)
            delivery.set(Delivery)
        else:
            Service.set(null)
            Room.set(rnormal)
            delivery.set(null)

    elif room==3:
        Service.set(null)
        Room.set(null)
        delivery.set(null)

    # ----------------------------TOTAL COST---------------------------------

    num1 = float(Cost.get())
    num2 = float(Room.get())
    num3 = float(delivery.get())
    num4 = float(Drink.get())
    num5 = float(Service.get())

    totalval = float(num1+num2+num3+num4+num5)
    Total.set(totalval)

    myTotal = 'Total Cost($)',totalval
    Display.delete(0,END)
    Display.insert(0,totalval)

    if totalval<=0:
        Display.delete(0,END)
        Display.insert(0,'Please, make an order!')

# def Exit():'
#     ask = ttk
def Clear():
    Display.delete(0,END)
    Display.insert(0,'Please make an order')

def hotel():
    Display.delete(0,END)
    Display.insert(0,'Hotel Management Sys.')

def rst():
    Display.delete(0,END)
    Display.insert(0,'Powered by Python')

def rest():
    Clear()
    Display.delete(0,END)
    Display.insert(0,'Hello! Welcome')
    mealdicator.set(value='Delicios Meal')
    drinkitator.set(value='Drink')
    indicator.set(value='Choose a Country')
    txtqtydrink.delete(0,END)
    txtqtydrink.insert(0,0.0)
    txtqtymeal.delete(0,END)
    txtqtymeal.insert(0,0.0)
    v.set(3)
    Total.set(0)
    Service.set(0)
    Drink.set(0)
    Cost.set(0)
    chkb1.set(0)
    delivery.set(0)

def reset():
    Display.delete(0,END)
    Display.insert(0,'System Resetting...')
    Display.after(2000,hotel)
    Display.after(4000,rst)
    Display.after(6000,rest)

def stop():
    root.destroy()

def Exit():
    Display.delete(0,END)
    Display.insert(0,'Thanks for visiting..')
    Display.after(3000,stop)

root = Tk()
root.title('HOTEL Management System')
root.geometry('1200x600+100+50')

# ------------------------SCREEN PARTITION---------------------------------

Tops = Frame(root,width=1200,height=50,bg='blue',relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width=600,height=700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width=200,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)

f3 = Frame(root,width=35,height=700,relief=SUNKEN)
f3.pack(side=LEFT)

f4 = Frame(root,width=100,height=700,relief=SUNKEN)
f4.pack(side=LEFT)

# ---------------------------MAIN SCREEN------------------------------------

txt_input=StringVar(value='PYTHON is good for all!')
Display = Entry(Tops,font=('arial',75,'bold'),fg='white',bd=30,bg='blue',justify='right',textvariable=txt_input)
Display.grid(columnspan=4)

# --------------------------DATE AND TIME-----------------------------------

localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(f2,font=('arial',15,'bold'),text=localtime,fg='dark blue',bd=10,anchor=W)
lblInfo.grid(row=0,column=0,columnspan=4)

# ---------------------------CALCULATOR---------------------------------------

# ----------row1------------
operator = ''


btn7 = Button(f2,text = '7' , font=('arial',15,'bold') , padx=10,pady=2,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(7)).grid(row=2,column=0)
btn8 = Button(f2,text = '8' , font=('arial',15,'bold') , padx=10,pady=2,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(8)).grid(row=2,column=1)
btn9 = Button(f2,text = '9' , font=('arial',15,'bold') , padx=10,pady=2,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(9)).grid(row=2,column=2)
btnC = Button(f2,text = 'C' , font=('arial',15,'bold') , padx=10,pady=2,fg= 'black' , bg='purple' , bd = 8
              , command = clear).grid(row=2,column=3)

# ----------row2------------

btn4 = Button(f2,text = '4' , font=('arial',15,'bold') , padx=10,pady=2,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(4)).grid(row=3,column=0)
btn5 = Button(f2,text = '5' , font=('arial',15,'bold') , padx=10,pady=2,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(5)).grid(row=3,column=1)
btn6 = Button(f2,text = '6' , font=('arial',15,'bold') , padx=10,pady=2,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(6)).grid(row=3,column=2)
btnplus = Button(f2,text = '+' , font=('arial',15,'bold'), padx=10,pady=2,fg='black' , bg='orange' , bd = 8
              , command = lambda: btn('+')).grid(row=3,column=3)


# ----------row3----------------

btn1 = Button(f2,text = '1' , font=('arial',15,'bold') , padx=10,pady=2,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(1)).grid(row=4,column=0)
btn2 = Button(f2,text = '2' , font=('arial',15,'bold') , padx=10,pady=2,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(2)).grid(row=4,column=1)
btn3 = Button(f2,text = '3' , font=('arial',15,'bold') , padx=10,pady=2,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(3)).grid(row=4,column=2)
btnminus = Button(f2,text = '-' , font=('arial',15,'bold') , padx=13,pady=2,fg='black' , bg='orange' , bd = 8
              , command = lambda: btn('-')).grid(row=4,column=3)

# ------------row4-----------------------

btn0 = Button(f2,text = '0' , font=('arial',15,'bold') , padx=10,pady=2,fg='black' , bg='white' , bd = 8
              , command = lambda: btn(0)).grid(row=5,column=0)
btndot = Button(f2,text = '.' , font=('arial',15,'bold') , padx=12,pady=2,fg='black' , bg='white' , bd = 8
              , command = lambda: btn('.')).grid(row=5,column=1)
btndiv = Button(f2,text = '/' , font=('arial',15,'bold') , padx=13,pady=2,fg='black' , bg='orange' , bd = 8
              , command = lambda: btn('/')).grid(row=5,column=2)
btnmul = Button(f2,text = 'X' , font=('arial',15,'bold') , padx=10,pady=2,fg='black' , bg='orange' , bd = 8
              , command = lambda: btn('*')).grid(row=5,column=3)

# -------------row5------------

btneqals = Button(f2,text = '=' , font=('arial',15,'bold') , padx=42,pady=2,fg='black' , bg='red' , bd = 8
              ,command = Equal).grid(row=6,column=0,columnspan=2)
btnOB = Button(f2,text = '(' , font=('arial',15,'bold') , padx=12,pady=2,fg='black' , bg='orange' , bd = 8
             , command = lambda: btn('(') ).grid(row=6,column=2)
btnCB = Button(f2,text = ')' , font=('arial',15,'bold') , padx=12,pady=2,fg='black' , bg='orange' , bd = 8
              , command = lambda: btn(')')).grid(row=6,column=3)

# -----------------------------------MEAL BOX-------------------------------------------

meal1=IntVar()
mealdicator = StringVar(value='DELICIOUS MEAL')

lblMeal = Label(f1,font=('arial',10,'bold'),text='Choose Meal',bd=10,anchor=W)
lblMeal.grid(row=0,column=0)
txtMeal = ttk.Combobox(f1,font=('arial',8,'bold'),textvariable=mealdicator)
txtMeal['values']=('Fried Rice','Fried Rice and Chicken','Shawarma','Cheese','Burger')
txtMeal.grid(row=0,column=1)

lblqtymeal = Label(f1,font=('arial',10,'bold'),text='Quantity of Meal',bd=10,anchor=W)
lblqtymeal.grid(row=1,column=0)
txtqtymeal = Entry(f1,font=('arial',8,'bold'),textvariable=meal1,insertwidth=5,bd=5,justify='right')
txtqtymeal.grid(row=1,column=1)

# -----------------------------------Drink box---------------------------------------

drink1=IntVar()
drinkitator = StringVar(value='Choose Drink')

lbldrink = Label(f1,font=('arial',10,'bold'),text='Choose Drink',bd=10,anchor=W)
lbldrink.grid(row=2,column=0)
txtdrink = ttk.Combobox(f1,font=('arial',8,'bold'),textvariable=drinkitator)
txtdrink.grid(row=2,column=1)
txtdrink['values']=('Coke','Pepsi','Beer','Lemonade')

lblqtydrink = Label(f1,font=('arial',10,'bold'),text='Quantity of Meal',bd=10,anchor=W)
lblqtydrink.grid(row=3,column=0)
txtqtydrink = Entry(f1,font=('arial',8,'bold'),textvariable=drink1,insertwidth=5,bd=5,justify='right')
txtqtydrink.grid(row=3,column=1)

# -----------------------------------ORDER DELIVERY------------------------------------
chkb1 = IntVar()

lblHomedelivery = Label(f1,text='Home Delivery',font = ('arial',10,'bold'),bd=10,anchor=W)
lblHomedelivery.grid(row=4,column=0)
txtHomedelivery = Checkbutton(f1,text='YES',variable=chkb1,font = ('arial',8,'bold'))
txtHomedelivery.grid(row=4,column=1)

# --------------------------------------BOOK A ROOM-------------------------------------

v = IntVar()
v.set(3)
lblRoom1 = Label(f1,text='Book a Room',font = ('arial',10,'bold'),bd=10,anchor=W)
lblRoom1.grid(row=5,column=0)

Myradios = Radiobutton(f1,text='VIP',font=('arial',5,'bold'),variable=v,value=1)
Myradios.grid(row=5,column=1,sticky=W)

Myradios = Radiobutton(f1,text='Common Room',font=('arial',5,'bold'),variable=v,value=2)
Myradios.grid(row=5,column=1)

Myradios = Radiobutton(f1,text='No',font=('arial',5,'bold'),variable=v,value=3)
Myradios.grid(row=5,column=1,sticky=E)

# -------------------------------------COST DISPLAY SCREEN-------------------------------

Cost = StringVar()
lblMeal1=Label(f1,font=('arial',10,'bold'),text='Cost of Meal($)',bd=10,anchor=W)
lblMeal1.grid(row=0,column=2)
txtMeal1 = Entry(f1,font=('arial',8,'bold'),justify='right',bg='blue',textvariable=Cost,bd=10,insertwidth=4)
txtMeal1.grid(row=0,column=3)

Drink = StringVar()
lbldrink1=Label(f1,font=('arial',10,'bold'),text='Cost of Drink($)',bd=10,anchor=W)
lbldrink1.grid(row=1,column=2)
txtdrink1 = Entry(f1,font=('arial',8,'bold'),justify='right',bg='blue',textvariable=Drink,bd=10,insertwidth=4)
txtdrink1.grid(row=1,column=3)

delivery = StringVar()
lbldelivery=Label(f1,font=('arial',10,'bold'),text='Cost of Home delivery($)',bd=10,anchor=W)
lbldelivery.grid(row=2,column=2)
txtdelivery = Entry(f1,font=('arial',8,'bold'),justify='right',bg='blue',textvariable=delivery,bd=10,insertwidth=4)
txtdelivery.grid(row=2,column=3)

Room = StringVar()
lblroom=Label(f1,font=('arial',10,'bold'),text='Cost of Room($)',bd=10,anchor=W)
lblroom.grid(row=3,column=2)
txtroom = Entry(f1,font=('arial',8,'bold'),justify='right',bg='blue',textvariable=Room,bd=10,insertwidth=4)
txtroom.grid(row=3,column=3)

Service = StringVar()
lblservice=Label(f1,font=('arial',10,'bold'),text='Service Fee($)',bd=10,anchor=W)
lblservice.grid(row=4,column=2)
txtservice = Entry(f1,font=('arial',8,'bold'),justify='right',bg='blue',textvariable=Service,bd=10,insertwidth=4)
txtservice.grid(row=4,column=3)

Total = StringVar()
lbltotal = Label(f1,font=('arial',10,'bold'),text='Total Cost($)',bd=10,anchor=W)
lbltotal.grid(row=5,column=2)
txttotal = Entry(f1,font=('arial',8,'bold'),justify='right',bg='blue',textvariable=Total,bd=10,insertwidth=4)
txttotal.grid(row=5,column=3)

# -------------------------------------CURRENCY CONVERTER-------------------------------

def convert():
    var2 = indicator.get()
    var3 = var1.get()
    if var2=='US':
        Display.delete(0,END)
        var4 = ((var3*0.013362),'USD')
        Display.insert(0,var4)
    elif var2=='Australia':
        Display.delete(0,END)
        var4 = ((var3*0.018485),'Australian Dollar')
        Display.insert(0,var4)
    elif var2=='Canada':
        Display.delete(0,END)
        var4 = ((var3*0.017601),'Canadian Dollar')
        Display.insert(0,var4)
    elif var2=='Europe':
        Display.delete(0,END)
        var4 = ((var3*0.011231),'Euro')
        Display.insert(0,var4)
    elif var2=='Pakistan':
        Display.delete(0,END)
        var4 = ((var3*2.248897),'Pakistani Rupee')
        Display.insert(0,var4)
    elif var2=='Singapore':
        Display.delete(0,END)
        var4 = ((var3*0.018259),'Singapore Dollar')
        Display.insert(0,var4)
    elif var2=='Switzerland':
        Display.delete(0,END)
        var4 = ((var3*0.012167),'Swiss Franc')
        Display.insert(0,var4)
    elif var2=='China':
        Display.delete(0,END)
        var4 = ((var3*0.092476),'Yuan')
        Display.insert(0,var4)
    else:
        Display.delete(0,END)
        var4 = ('INVALID COUNTRY')
        Display.insert(0,var4)


var1 = IntVar()
# var2 = IntVar()
indicator = StringVar(value = 'Choose a Country')

lblcurcon = Label(f1,font=('arial',10,'bold'),text='-------------------------------------------Currency Converter-----------------------------------------------------'
                  ,bd=10,anchor=W)
lblcurcon.grid(row=7,columnspan=4)
# Label(f1,text = 'Currency Converter' , font = ('arial',10 , 'bold')).grid(row=8,column=1)

Label(f1,text = 'Amount(Rs.)' , font = ('arial',10,'bold')).grid(row=8,column=2)
e1 = Entry(f1,width=25,font = ('arial',10,'bold'),textvariable=var1)
e1.grid(row=8,column=3,sticky=E)

Label(f1,text = 'Country' , font = ('arial',10,'bold')).grid(row=8,column=0)
e2 = ttk.Combobox(f1,width=30,font = ('arial',10,'bold'),textvariable=indicator)
# ttk.Label(text='Select a Country',font=('arial',20,'bold')).grid(row=3,column=1)
e2['values'] = ('US','Australia','Canada','Europe','Pakistan','Singapore','Switzerland','China')
e2.grid(row=8,column=1)

# ---------------------------------------CONTROL BUTTONS----------------------------------------------------

btnConvert = Button(f1,padx=10,pady=5,bd=10,font = ('arial',10,'bold'),width=10,text='Covert',bg='orange',command=convert)
btnConvert.grid(row=9,column=2)

btnTotal = Button(f4,padx=10,pady=5,bd=10,font = ('arial',10,'bold'),width=10,text='Total',bg='orange',command=TotalResult)
btnTotal.grid(row=0,column=0)

btnScreen = Button(f4,padx=10,pady=5,bd=10,font = ('arial',10,'bold'),width=10,text='Clear',bg='blue',command=Clear)
btnScreen.grid(row=1,column=0)

btnReset = Button(f4,padx=10,pady=5,bd=10,font = ('arial',10,'bold'),width=10,text='Reset',bg='green',command=reset)
btnReset.grid(row=2,column=0)

btnExit = Button(f4,padx=10,pady=5,bd=10,font = ('arial',10,'bold'),width=10,text='Exit',bg='red',command=Exit)
btnExit.grid(row=3,column=0)



root.mainloop()
