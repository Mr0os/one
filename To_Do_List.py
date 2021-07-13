from tkinter import *
from tkinter.ttk import *

form = Tk()
form.title("To Do List")
form.geometry("500x500")




Lable_1 = Label(form , text = "Enter name")
Lable_1.pack()


Entry_1 = Entry(form)
Entry_1.pack()





value1 = []
combobox1 = Combobox(form, values = value1 , state = "readonly")

combobox1.pack()

def todo():
    Get = Entry.get(Entry_1)
    value1.append(Get)
    status = combobox1.configure(value = value1)
    # Button_open.pack()
### open information
Lable_open = Label(form , text = "Enter ")
Lable_open.pack_forget()

Entry_open = Entry(form)
Entry_open.pack_forget()

Lable_open2 = Label(form , text = "Enter ")
Lable_open2.pack_forget()

Entry_open2 = Entry(form)
Entry_open2.pack_forget()

Lable_massage = Label(form , text = " ")
Lable_massage.pack_forget()
Lable_massage2 = Label(form , text = " ")
Lable_massage2.pack_forget()
Lable_massage3 = Label(form , text = " ")
Lable_massage3.pack_forget()

''' functions '''
def Open():
    Lable_open.pack()
    Entry_open.pack()
    Lable_open2.pack()
    Entry_open2.pack()
    Button_show.pack()
    Lable_massage.pack()
    Lable_massage2.pack()
    Lable_massage3.pack()
    # Button_save.pack()
    

def BMI():
    
    a = float(Entry_open.get())
    b = float(Entry_open2.get())
    result = b/a**2
    if result<18.5:
        Lable_massage.configure(text = "you are underweight")
    elif result < 25:
        Lable_massage.configure(text = "Normal")
    elif result < 30:
        Lable_massage.configure(text = "you are overweight")
    else:
        Lable_massage.configure(text = "obese")

    Lable_massage2.configure(text = result)   

    # global result

    get_s = combobox1.get()
    if get_s == '':
        Lable_massage3.configure(text = "Pleas chois your name")
    else:
        name = open(f'{get_s}.txt','w') 
        name.write(str(result))







'''  Buttoens  '''
Button_1 = Button(form, text = "Click",command = todo)
Button_1.pack()


Button_2 = Button(form, text = "open",command = Open)
Button_2.pack()

Button_show = Button(form, text = 'print' , command = BMI)
Button_show.pack_forget()






mainloop()

