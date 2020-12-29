from tkinter import*
from math import*
font=("Arial",22)
m=Tk()
m.title("Calculator")
m.geometry("450x650")
heading=Entry(m,width=60,font=font)
heading.pack(side=TOP,pady=20,fill=X)


def all_clear():
    heading.delete(0,END)

def squart():
    x=int(heading.get())
    z=sqrt(x)
    heading.delete(0,END)
    heading.insert(0,END)
def pow2():
    x=int(heading.get())
    z=x**2
    heading.delete(0, END)
    heading.insert(0, z)
def pow3():
    x=int(heading.get())
    z=x**3
    heading.delete(0, END)
    heading.insert(0, z)
def Sin():
    x=int(heading.get())
    z=sin(x)
    heading.delete(0, END)
    heading.insert(0, z)
def Cos():
    x=int(heading.get())
    z=cos(x)
    heading.delete(0, END)
    heading.insert(0, z)
def Tan():
    x=int(heading.get())
    z=tan(x)
    heading.delete(0, END)
    heading.insert(0, z)
def fact():
    n=heading.get()
    num=int(n)
    if num==0 or num==1:
        z=0
    elif num>1:
        for i in range(1,num):
            num=num*i
            z=int(num)
        heading.delete(0,z)
        heading.insert(0,z)
def click_btn_function(event):
    bt=event.widget
    text=bt['text']
    if text=="=":
        ex=heading.get()
        answer=eval(ex)
        heading.delete(0,END)
        heading.insert(0,answer)
        return
    heading.insert(END,text)

buttonframe=Frame(m)
buttonframe.pack(side=TOP)

temp=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(buttonframe,text=int(temp),font=font,bg='pink',fg='black')
        btn.grid(row=i,column=j,padx=3,pady=5)
        temp=temp+1
        btn.bind('<Button-1>',click_btn_function)
zerobtn=Button(buttonframe,text="0",font=font,bg='pink',fg='black')
zerobtn.grid(row=3,column=0,padx=3,pady=5)
dotbtn=Button(buttonframe,text=".",width=2,font=font,bg='pink',fg='black')
dotbtn.grid(row=3,column=1,padx=3,pady=5)
equalbtn=Button(buttonframe,text="=",width=2,font=font,bg='orange',fg='black')
equalbtn.grid(row=3,column=2,padx=3,pady=5)
A=Button(buttonframe,text="+",width=2,font=font,bg='light blue',fg='black')
A.grid(row=0,column=3,padx=3,pady=5)
S=Button(buttonframe,text="-",width=2,font=font,bg='light blue',fg='black')
S.grid(row=1,column=3,padx=3,pady=5)
M=Button(buttonframe,text="x",width=2,font=font,bg='light blue',fg='black')
M.grid(row=2,column=3,padx=3,pady=5)
D=Button(buttonframe,text="/",width=2,font=font,bg='light blue',fg='black')
D.grid(row=3,column=3,padx=3,pady=5)
clear=Button(buttonframe,text="AC",width=7,font=font,command=all_clear,bg='brown',fg='black')
clear.grid(row=4,column=3,columnspan=2,padx=3,pady=5)
A.bind('<Button-1>',click_btn_function)
S.bind('<Button-1>',click_btn_function)
M.bind('<Button-1>',click_btn_function)
D.bind('<Button-1>',click_btn_function)
zerobtn.bind('<Button-1>',click_btn_function)
dotbtn.bind('<Button-1>',click_btn_function)
equalbtn.bind('<Button-1>',click_btn_function)

s3=Button(buttonframe,text="^2",bg='yellow',font=font,fg='black',command=pow2)
s3.grid(row=4,column=1,padx=3,pady=5)
s4=Button(buttonframe,text="√",bg='yellow',font=font,fg='black',command=squart)
s4.grid(row=4,column=0,padx=3,pady=5)
s5=Button(buttonframe,text="n!",width=3,bg='yellow',font=font,fg='black',command=fact)
s5.grid(row=3,column=4,padx=3,pady=5)
s2=Button(buttonframe,text="Sin",width=4,bg='light green',font=("Arial",19),fg='black',command=Sin)
s2.grid(row=0,column=4,padx=3,pady=5)
s1=Button(buttonframe,text="Cos",width=4,bg='light green',font=("Arial",19),fg='black',command=Cos)
s1.grid(row=1,column=4,padx=3,pady=5)
s6=Button(buttonframe,text="Tan",width=4,bg='light green',font=("Arial",19),fg='black',command=Tan)
s6.grid(row=2,column=4,padx=3,pady=5)
s7=Button(buttonframe,text="^3",bg='yellow',font=font,fg='black',command=pow3)
s7.grid(row=4,column=2,padx=3,pady=5)

m.mainloop()