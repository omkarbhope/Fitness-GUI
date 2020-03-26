import tkinter.ttk as ttk
from tkinter import *
import pandas as pd 
import numpy as np
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os


root=Tk()
root.configure(bg="#6028BD")
r1=IntVar()
r2=BooleanVar()
r3=StringVar()
bmi=IntVar()
BMI=IntVar()
def open_window(a):
    global frame1,bmi
    frame1=Toplevel()
    frame1.configure(bg="#6028BD")
    e1=Entry(frame1,width=45,borderwidth=0,bg='#2F0C68',fg='White')
    e1.insert(0,0)
    e1.grid(row=0,column=1,padx=10,pady=40)


    e2=Entry(frame1,width=45,borderwidth=0,bg='#2F0C68',fg='White')
    e2.insert(0,0)
    e2.grid(row=0,column=3,padx=10,pady=40)

    e3=Entry(frame1,width=45,borderwidth=0,bg='#2F0C68',fg='White')
    e3.insert(0,0)
    e3.grid(row=1,column=1,padx=10,pady=40)

    label1=Label(frame1,text="Enter Height (cm)",bg="#6028BD",fg="#B9AAD1",anchor="w",pady=40)
    label1.grid(row=0,column=0)

    label2=Label(frame1,text="Enter Weight (kg)",bg="#6028BD",fg="#B9AAD1",anchor="w",pady=40,padx=40)
    label2.grid(row=0,column=2)

    label3=Label(frame1,text="Enter Age (2-120)",bg="#6028BD",fg="#B9AAD1",anchor="w",pady=40,padx=40)
    label3.grid(row=1,column=0)

    label4=Label(frame1,text="Gender",bg="#6028BD",fg="#B9AAD1",anchor="w",pady=40,padx=40)
    label4.grid(row=2,column=0)

    
    r1.set(1)
    Radio1=Radiobutton(frame1,text="Male",value=1,variable=r1,anchor='w',padx=10,bg='#2F0C68',fg="#B9AAD1")
    Radio2=Radiobutton(frame1,text="Female",value=2,variable=r1,anchor='w',padx=2,bg='#2F0C68',fg="#B9AAD1")

    Radio1.grid(row=2,column=1)
    Radio2.grid(row=2,column=2)

    Button1=Button(frame1,text="CALCULATE",padx=30,pady=30,anchor='center',bg='#2F0C68',fg="#B9AAD1",command=lambda: calculate(0))
    Button1.grid(row=3,column=0,columnspan=3)
    bmi.set(10)
    def calculate(a):
        # Retrieves all necessary information to calculate BMI
        global bmi,BMI
        weight = float(e2.get())
        height = float(e1.get())
        bmi = float((weight)/((height/100)**2))
        BMI=int(bmi)
        # Updates the status label
        if bmi < 18.5:
            label=Label(frame1,text="You are underweight",bg="#6028BD",anchor='center',fg="#B9AAD1",pady=40,padx=40)
            label.grid(row=3,column=0,columnspan=3)
            label1=Label(frame1,text="YOUR BMI IS :-  "+str(BMI),bg="#6028BD",anchor='center',fg="#B9AAD1",pady=40,padx=40)
            label1.grid(row=4,column=0,columnspan=3)
        if 18.5 <= bmi < 25:
            label=Label(frame1,text="You are normal",bg="#6028BD",fg="#B9AAD1",anchor='center',pady=40,padx=40)
            label.grid(row=3,column=0,columnspan=3)
            label1=Label(frame1,text="YOUR BMI IS :-  "+str(BMI),bg="#6028BD",anchor='center',fg="#B9AAD1",pady=40,padx=40)
            label1.grid(row=4,column=0,columnspan=3)
        if 25 <= bmi < 30:
            label=Label(frame1,text="You are overweight",bg="#6028BD",fg="#B9AAD1",anchor='center',pady=40,padx=40)
            label.grid(row=3,column=0,columnspan=3)
            label1=Label(frame1,text="YOUR BMI IS :-  "+str(BMI),bg="#6028BD",anchor='center',fg="#B9AAD1",pady=40,padx=40)
            label1.grid(row=4,column=0,columnspan=3)
        if 30<= bmi > 30:
            label=Label(frame1,text="You are obese",bg="#6028BD",fg="#B9AAD1",anchor='center',pady=40,padx=40)
            label.grid(row=3,column=0,columnspan=3)
            label1=Label(frame1,text="YOUR BMI IS :-  "+str(BMI),bg="#6028BD",anchor='center',fg="#B9AAD1",pady=40,padx=40)
            label1.grid(row=4,column=0,columnspan=3)

    Button1=Button(frame1,text="NEXT",anchor='center',bg='#2F0C68',fg="#B9AAD1",command=lambda: first_window(0))
    Button1.grid(row=4,column=0)

    frame1.mainloop()


def first_window(a):
    global frame2,r2
    frame1.destroy()
    frame2=Toplevel()
    frame2.configure(bg="#6028BD")


    label1=Label(frame2,text="DO YOU GO TO GYM ?",bg="#6028BD",fg="#B9AAD1",anchor="center",pady=40,padx=20)
    label1.grid(row=0,column=0)

    r2.set(True)
    Radio1=Radiobutton(frame2,text="Yes !",value=True,variable=r2,anchor='center',padx=10,pady=10,bg='#6028BD',fg="#B9AAD1")
    Radio2=Radiobutton(frame2,text="No !",value=False,variable=r2,anchor='center',padx=10,pady=10,bg='#6028BD',fg="#B9AAD1")
    Radio1.grid(row=1,column=0)
    Radio2.grid(row=2,column=0)

    Button1=Button(frame2,text="CHOOSE!!!",anchor='center',bg='#2F0C68',fg="#B9AAD1")
    Button1.grid(row=3,column=0)

    label1=Label(frame2,text="",bg="#6028BD",fg="#B9AAD1",anchor="center",pady=10,padx=10)
    label1.grid(row=4,column=0)

    Button1=Button(frame2,text="NEXT",anchor='center',bg='#2F0C68',fg="#B9AAD1",command=lambda :second_window(0))
    Button1.grid(row=5,column=0)

    frame2.mainloop()

def second_window(a):
    global frame3,r3
    frame2.destroy()
    frame3=Toplevel()
    frame3.configure(bg="#6028BD")


    label1=Label(frame3,text="WHAT DO YOU WANT ?",bg="#6028BD",fg="#B9AAD1",anchor="center",pady=40,padx=20)
    label1.grid(row=0,column=0)

    r3.set('DIET')
    Radio1=Radiobutton(frame3,text="Diet Plan",value='DIET',variable=r3,anchor='center',padx=10,pady=10,bg='#6028BD',fg="#B9AAD1")
    Radio2=Radiobutton(frame3,text="Exercise",value='EXERCISE',variable=r3,anchor='center',padx=10,pady=10,bg='#6028BD',fg="#B9AAD1")
    Radio3=Radiobutton(frame3,text="Both",value='BOTH',variable=r3,anchor='center',padx=10,pady=10,bg='#6028BD',fg="#B9AAD1")
    Radio1.grid(row=1,column=0)
    Radio2.grid(row=2,column=0)
    Radio3.grid(row=3,column=0)

    Button1=Button(frame3,text="CALCULATE",anchor='center',bg='#2F0C68',fg="#B9AAD1")
    Button1.grid(row=4,column=0)

    label1=Label(frame3,text="",bg="#6028BD",fg="#B9AAD1",anchor="center",pady=10,padx=10)
    label1.grid(row=5,column=0)

    Button1=Button(frame3,text="NEXT",anchor='center',bg='#2F0C68',fg="#B9AAD1",command=lambda: third_window(0))
    Button1.grid(row=6,column=0)

    frame3.mainloop()

def third_window(a):
    global frame4
    frame3.destroy()
    frame4=Toplevel()
    frame4.configure(bg="#6028BD")
    choice=r3.get()

    label1=Label(frame4,text="YOUR PLAN IS:- ",bg="#6028BD",fg="#B9AAD1",anchor="center",pady=40,padx=20)
    label1.grid(row=0,column=0)

    Button1=Button(frame4,text="PRINT",bg='#2F0C68',fg="#B9AAD1",padx=10,pady=10,anchor="center",command=lambda:get_backend(0))
    Button1.grid(row=1,column=0)

    label1=Label(frame4,text="",bg="#6028BD",fg="#6028BD",anchor="center",pady=5,padx=5)
    label1.grid(row=2,column=0)

    Button1=Button(frame4,text="TRANSLATE",bg='#2F0C68',fg="#B9AAD1",anchor="center",padx=10,pady=10,command=lambda:translate(0))
    Button1.grid(row=3,column=0)

    label1=Label(frame4,text="",bg="#6028BD",fg="#6028BD",anchor="center",pady=5,padx=5)
    label1.grid(row=5,column=0)
    
    frame4.mainloop()      

def get_backend(x):
    a=bmi
    a=int(a)
    b=r2.get()
    c=r3.get()
    backend(a,b,c)
    fourth_window(0)

def fourth_window(a):
    global frame5
    frame5=Toplevel()
    frame5.configure(bg="#6028BD")

    with open("C:\\Users\\omkar\\OneDrive\\Desktop\\MyProj-1.txt","r+",encoding='utf-8') as myfile:
        data=myfile.read()

    label2=Text(frame5,bg="#6028BD",fg="#B9AAD1",pady=10,padx=10)
    label2.insert(END,data)
    label2.grid(row=1,column=0)    

    frame5.mainloop()

def translate(a):
    
    with open("C:\\Users\\omkar\\OneDrive\\Desktop\\MyProj-1.txt","r+",encoding='utf-8') as myfile:
        data=myfile.read()
    def Translation(a):
        global translation1
        word=data
        translator=Translator(service_urls=['translate.google.com'])
        translation1=translator.translate(word,dest='en')
    

    def T_S(a):
        Translation(0)
        text=translation1.text
        speech=gTTS(text=text,lang="en")
        if os.path.isfile('C:\\Users\\omkar\\OneDrive\\Desktop\speech1.mp3'):
            os.remove('C:\\Users\\omkar\\OneDrive\\Desktop\speech1.mp3')
            speech.save(r'C:\\Users\\omkar\\OneDrive\\Desktop\speech1.mp3')
            playsound(r'C:\\Users\\omkar\\OneDrive\\Desktop\speech1.mp3')

        else:
            speech.save(r'C:\\Users\\omkar\\OneDrive\\Desktop\speech1.mp3')
            playsound(r'C:\\Users\\omkar\\OneDrive\\Desktop\speech1.mp3')   
    T_S(0)

def backend(bmi,choice,Diet_Exe):
    df=pd.read_csv('C:\\Users\\omkar\\OneDrive\\Desktop\\project2.csv',index_col=0)
    b=[]
    e=[]
    df=df[df['BMI']==bmi]
    df=df[df['GYM']==choice]
    if(Diet_Exe!='BOTH'):
        df=df[Diet_Exe]

        for i in range(0,len(df)):
            b.append(str(df.iloc[i]))
    
        filename="C:\\Users\\omkar\\OneDrive\\Desktop\\MyProj-1.txt"
        f=open(filename,"w")

        if(Diet_Exe=='DIET'):
            headers="The Diet Plan is :-\n\n"
        else:
            headers="The Work-Out Plan is :-\n\n"

        f.write(headers)

        for i in range (0,len(df)):
            f.write(b[i]+"\n")
    else:
        d1=df['DIET']
        d2=df['EXERCISE']

        for i in range(0,len(d1)):
            b.append(str(d1.iloc[i]))

        filename="C:\\Users\\omkar\\OneDrive\\Desktop\\MyProj-1.txt"
        f=open(filename,"w") 

        headers="The Diet Plan is :-\n\n" 

        f.write(headers)

        for i in range (0,len(d1)):
            f.write(b[i]+"\n")  

        headers1="\n\nThe Work-Out Plan is :-\n\n" 
        f.write(headers1)   

        for i in range(0,len(d2)):
            e.append(str(d2.iloc[i])) 

        for i in range (0,len(d2)):
            f.write(e[i]+"\n")
      

label1=Label(root,text="LOGIN PAGE !!!!!",bg="#6028BD",fg="#B9AAD1",anchor="center",pady=40,padx=20)
label1.grid(row=0,column=0)
Button1=Button(root,text="NEXT",anchor='center',bg='#2F0C68',fg="#B9AAD1",command=lambda: open_window(0))
Button1.grid(row=1,column=0)
root.mainloop()
