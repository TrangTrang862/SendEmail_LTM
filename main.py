from tkinter import *
from tkinter import messagebox
from pygame import mixer
import speech_recognition

def settings():
    root1=Toplevel
    root1.title('Setting')
    root1.geometry('650x340+350+90')

    root1.mainloop()

def speak():
    mixer.init()
    mixer.music.load('music1.mp3')
    mixer.music.play()
    sr=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as m:
        try:
            sr.adjust_for_ambient_noise(m,duration=0.2)
            audio=sr.listen(m)
            text=sr.recognize_google(audio)
            textarea.insert(END,text+'.')

        except:
            pass

def iexit():
    result=messagebox.askyesno('Notification','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def clear():
    toEntryField.delete(0,END)
    subjectEntryField.delete(0,END)
    textarea.delete(1.0,END)


root=Tk()
root.title('Email sender app')
root.geometry('780x620+100+50')
root.resizable(0,0)
root.config(bg='dodger blue2')

titleFrame=Frame(root,bg='white')
titleFrame.grid(row=0,column=0)
logoImage=PhotoImage(file='Email.png')
titleLabel=Label(titleFrame,text='  Email sender',image=logoImage,compound=LEFT,font=('Goudy old Style',28,'bold'),
                 bg='white',fg='dodger blue2' )
titleLabel.grid(row=0,column=0)
settingImage=PhotoImage(file='setting.png')

Button(titleFrame,image=settingImage,bd=0,bg='white',cursor='hand2',activebackground='white'
       ,command=settings).grid(row=0,column=1,padx=20)

chooseFrame=Frame(root,bg='dodger blue2')
chooseFrame.grid(row=1,column=0,pady=10)
choice=StringVar()

singleRadioButton=Radiobutton(chooseFrame,text='Single',font=('times new roman',25,'bold')
                              ,variable=choice,value='single',bg='dodger blue2',activebackground='dodger blue2')
singleRadioButton.grid(row=0,column=0,padx=20)

multipleRadioButton=Radiobutton(chooseFrame,text='Multiple',font=('times new roman',25,'bold')
                              ,variable=choice,value='multiple',bg='dodger blue2',activebackground='dodger blue2')
multipleRadioButton.grid(row=0,column=1,padx=20)

choice.set('single')

toLabelFrame=LabelFrame(root,text='to (Email Address)',font=('times new roman',16,'bold'),bd=5,fg='white',bg='dodger blue2')
toLabelFrame.grid(row=2,column=0,padx=100)

toEntryField=Entry(toLabelFrame,font=('times new roman',18,'bold'),width=30)
toEntryField.grid(row=0,column=0)

browserImage=PhotoImage(file='browse.png')

Button(toLabelFrame,text=' browse',image=browserImage,compound=LEFT,font=('arial',12,'bold'),
       cursor='hand2',bd=0,bg='dodger blue2',activebackground='dodger blue2',state=DISABLED).grid(row=0,column=1,padx=20)

subjectLabelFrame=LabelFrame(root,text='Subject',font=('times new roman',16,'bold'),bd=5,fg='white',bg='dodger blue2')
subjectLabelFrame.grid(row=3,column=0,pady=10)

subjectEntryField=Entry(subjectLabelFrame,font=('times new roman',18,'bold'),width=30)
subjectEntryField.grid(row=0,column=0)

emailLabelFrame=LabelFrame(root,text='Compose Email',font=('times new roman',16,'bold'),bd=5,fg='white',bg='dodger blue2')
emailLabelFrame.grid(row=4,column=0,padx=20)
micImage=PhotoImage(file='mic.png')

Button(emailLabelFrame,text=' Speak',image=micImage,compound=LEFT,font=('arial',12,'bold'),
       cursor='hand2',bd=0,bg='dodger blue2',activebackground='dodger blue2',command=speak).grid(row=0,column=0)
attachImage=PhotoImage(file='attachment.png')

Button(emailLabelFrame,text=' Attachment',image=attachImage,compound=LEFT,font=('arial',12,'bold'),
       cursor='hand2',bd=0,bg='dodger blue2',activebackground='dodger blue2').grid(row=0,column=1)

textarea=Text(emailLabelFrame,font=('times new roman',14,),height=8)
textarea.grid(row=1,column=0,columnspan=2)
sendImage=PhotoImage(file='send.png')
Button(root,image=sendImage,bd=0,bg='dodger blue2',cursor='hand2',activebackground='dodger blue2').place(x=490,y=540)

clearImage=PhotoImage(file='clear.png')
Button(root,image=clearImage,bd=0,bg='dodger blue2',cursor='hand2',activebackground='dodger blue2'
       ,command=clear).place(x=590,y=550)

exitImage=PhotoImage(file='exit.png')
Button(root,image=exitImage,bd=0,bg='dodger blue2',cursor='hand2',activebackground='dodger blue2'
       ,command=iexit).place(x=690,y=550)

totalLabel=Label(root,font=('times new roman',18,'bold'),bg='dodger blue2',fg='black')
totalLabel.place(x=10,y=560)

sendLabel=Label(root,font=('times new roman',18,'bold'),bg='dodger blue2',fg='black')
sendLabel.place(x=100,y=560)

leftLabel=Label(root,font=('times new roman',18,'bold'),bg='dodger blue2',fg='black')
leftLabel.place(x=190,y=560)

failedLabel=Label(root,font=('times new roman',18,'bold'),bg='dodger blue2',fg='black')
failedLabel.place(x=280,y=560)

root.mainloop()

