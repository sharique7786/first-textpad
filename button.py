import tkinter
from tkinter import *
from tkinter import ttk


converter=Tk()
converter.title('Currency Converter')
converter.geometry('600x400')
converter.wm_iconbitmap('cut.png')

OPTIONS={
    'Austrilian Dollar ':49.10,
    'Brazilian Riyal':17.30,
    'British Pound':90.92,
    'Bulgarian Lev':39.8,
    'Chinees Yuan':10.29,
    'Euro':77.30,
    'Hong Kong Dollar':8.8,
    'Indonesia Rupiya':0.004543,
    'Japanes Yen':0.654,
'pakistani Rupees':0.49,
'Srilankan Rupees':0.39,
'Swis Franc':69.7,
'Us Dollar':69.32
}
def ok():
    price=rupees1.get()
    answer=variable.get()
    D=OPTIONS.get(answer,None)
    converted = float(D)*float(price)
    result.delete(1.0,END)
    result.insert(INSERT,'Price In',INSERT,answer,INSERT,'=',INSERT,converted)



appname=Label(converter,text="Currency ",font=('Arial',12,'bold','underline'),fg='darkred')
appname.grid(row=0,column=0,padx=50)
photo=PhotoImage(file='cut.png')
logo=Label(converter,image=photo)
logo.grid(row=0,column=1)

appname=Label(converter,text=" Converter ",font=('Arial',12,'bold','underline'),fg='dark green')
appname.grid(row=0,column=2,ipadx=50)

result=Text(converter,height=6,width=50,font=('Arial',10,'bold'),bd=7)
result.grid(row=1,columnspan=10,padx=3)

indian=Label(converter,text='Indian Rupees : ',font=('Arial',10,'bold'),fg='blue')
indian.grid(row=2,column=0)

rupees=Entry(converter,font=('calibri',20))
rupees.grid(row=2,column=1)

choice=Label(converter,text='Select Country : ',font=('Arial',10,'bold'),fg='blue')
choice.grid(row=3,column=0)

rupees1=Entry(converter,font=('calibri',20))
rupees1.grid(row=3,column=1)

variable=StringVar(converter)
variable.set(None)
option=OptionMenu(converter,variable,*OPTIONS)
option.grid(row=3,column=1,sticky="ew")
button=Button(converter,text='Convert',fg='green',font=('calibri',20),bg='powder blue',command=ok)
button.grid(row=3,column=2)
button=Button(converter,text='Convert',fg='green',font=('calibri',20),bg='powder blue',command=ok)
button.grid(row=3,column=2)


converter.mainloop()