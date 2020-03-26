from tkinter import *
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os

win =Tk()
win.title("Translator")
win.geometry("200x70")

translation1=StringVar()

def Translation(a):
    global translation1
    word=entry.get()
    translator=Translator(service_urls=['translate.google.com'])
    translation1=translator.translate(word,dest='hi')
    # label1=Label(win,text=f"Translated in hindi : {translation1.text}",bg='yellow')
    # label1.grid(row=2,column=0)

def T_S(a):
    Translation(0)
    text=translation1.text
    speech=gTTS(text=text,lang="hi")
    if os.path.isfile('C:\\Users\\omkar\\OneDrive\\Desktop\speech1.mp3'):
        os.remove('C:\\Users\\omkar\\OneDrive\\Desktop\speech1.mp3')
        speech.save(r'C:\\Users\\omkar\\OneDrive\\Desktop\speech1.mp3')
        playsound(r'C:\\Users\\omkar\\OneDrive\\Desktop\speech1.mp3')

    else:
        speech.save(r'C:\\Users\\omkar\\OneDrive\\Desktop\speech1.mp3')
        playsound(r'C:\\Users\\omkar\\OneDrive\\Desktop\speech1.mp3')   



label=Label(win,text="Enter Here")
label.grid(row=0,column=0,sticky="W")

entry=Entry(win)
entry.grid(row=1,column=0)

button=Button(win,text="Translate",command=lambda: T_S(0))
button.grid(row=1,column=2)

win.mainloop()
