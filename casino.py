import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="hardik",
    database="casino"
)
cursor=mydb.cursor()
loginidct=0

import tkinter as tk
from tkinter import messagebox
from PIL import Image
import random
mwindow=tk.Tk()
#gamepage
def gamepagef():
    game=tk.Tk()
    game.geometry("1000x1000")
    file="casinogif.gif"
    info=Image.open(file)
    frames=info.n_frames
    im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]
    win=None
    anim=None
    flag=0
    def windata():
        global win,flag
        flag=1
        swin=tk.IntVar()
        swin=submitentry.get()
        win=swin
        win=win.strip()
        win=int(win)
        tempo=tk.Label(master=game,
                       text=win)
        tempo.pack()
        return win
    head=tk.Label(master=game,
                  text="Wheel Of Luck\nEnter Your No  "  )
    head.pack()
    
    submitentry=tk.Entry(master=game,
                         width=2)
    submitentry.pack()

    def playi(count,ctt,ct):
        global flag
        flag=1
        kk=0
        if count>15:
            kk=kk+1
        else:
            kk=kk+2
        global win
        if win!=None:
            def animation(count,ctt,ct):
                global anim,flag
                im2 = im[ctt]
                gif_label.configure(image=im2)
                ct += 1
                ctt+= 1
                if ctt == frames:
                    ctt=0
                if ct == count+74+kk:
                    flag=0
                    game.after_cancel(anim)
                    if win==count:
                        messagebox.showinfo("Won","You Won")
                        flag=0
                    else:
                        messagebox.showinfo("Lose","You Lose\nBetter Luck Next Time")
                        flag=0
                if ct<count+74+kk:
                    anim = game.after(150,lambda :animation(count,ctt,ct))
            animation(count,ctt,ct)
        else:
            messagebox.showinfo("no value","Enter your lucky number Please")
    def fin():
        if flag==0:
            windata()
            playi(random.randint(0,37),0,0)
        else:
            messagebox.showinfo("error","Don't Press Button\nWhile Wheel Is Spinning")
            return     
    submitwin=tk.Button(master=game,
                        text="Submit Your Lucky Number",
                        command=fin)
    submitwin.pack()
    gif_label = tk.Label(game,image="")
    gif_label.pack()
    game.mainloop()
#login
def loginf():
    logwindow=tk.Tk()
    def pr_login():
        uid=tk.IntVar()
        upassword=tk.StringVar()
        uid=logenterid.get()
        upassword=logenterpassword.get()
        temp=tk.Label(logwindow,text=uid+"\n"+upassword)
        temp.pack()
        cursor.execute("select * from casinod where login_id="+str(uid))
        tuid=0
        tpassword=""
        for x in cursor:
            tuid=x[0]
            tpassword=x[3]
        uid=uid.strip()
        uid=str(uid)
        tuid=str(tuid)
        tpassword=tpassword.strip()
        tpassword=str(tpassword)
        upassword=upassword.strip()
        upassword=str(upassword)
        if tuid==uid and tpassword==upassword:
            messagebox.showinfo("log","All Credential are correct")
            mwindow.destroy()
            logwindow.destroy()
            gamepagef()
        else:
            messagebox.showinfo("error","Login id or password \n is \n incorrect!!!")
    logframe=tk.Frame(master=logwindow)
    logidname=tk.Frame(master=logwindow)
    logid=tk.Frame(master=logwindow)
    logpassword=tk.Frame(master=logwindow)
    logidpassword=tk.Frame(master=logwindow)
    logsubmit=tk.Frame(master=logwindow)
    loghead=tk.Label(master=logframe,
                     text="LOG IN",
                     font=("chiller",25),
                     bg="green",
                     fg="white",
                     height=8,
                     width=50)
    loghead.pack(fill=tk.X,expand=True)
    logframe.pack()
    loglabelid=tk.Label(master=logidname,
                          text="LOGIN ID",
                          font=("chiller",15),
                          bg="Yellow",
                          height=3,
                          width=30)
    loglabelid.pack()
    logidname.pack()
    logenterid=tk.Entry(master=logid,
                          fg="black",
                          bg="white",
                          width=35)
    logenterid.pack()
    logid.pack()
    loglabelpassword=tk.Label(master=logpassword,
                          text="PASSWORD",
                          font=("chiller",15),
                          bg="Yellow",
                          height=3,
                          width=30)
    loglabelpassword.pack()
    logpassword.pack()
    logenterpassword=tk.Entry(master=logidpassword,
                          fg="black",
                          bg="white",
                          width=35)
    logenterpassword.pack()
    logidpassword.pack()
    logbutton=tk.Button(master=logsubmit,
                        text="SUBMIT",
                        fg="white",
                        bg="Blue",
                        height=3,
                        width=10,
                        command=pr_login)
    logbutton.pack()
    logsubmit.pack()
    logwindow.mainloop()

#sign up  window
def signf():
    signwindow=tk.Tk()
    def signcommand():
        def pr_signup():
            sname=tk.StringVar()
            spassword=tk.StringVar()
            scontact=tk.IntVar()
            sname=signentername.get()
            spassword=signenterpassword.get()
            scontact=signentercontact.get()
            if len(sname)<=100 and len(spassword)<=120 and len(scontact)==10:
                global loginidct
                cursor.execute("SELECT COUNT(login_id) FROM casinod")
                for x in cursor:
                    loginidct=x[0]+1
                mydb.commit()
                cursor.execute("insert into casinod values("+str(loginidct)+',"'+sname+'",'+'"'+scontact+'","'+spassword+'",500)')
                mydb.commit()
                messagebox.showinfo("loginid","Your Login id is:- "+str(loginidct)+"\nPlease remember it")
                signwindow.destroy()
                mwindow.destroy()
                gamepagef()
            else:
                messagebox.showinfo("Error","Constarints out of range \nsign up again")
        pr_signup()
    signframe=tk.Frame(master=signwindow)
    signname=tk.Frame(master=signwindow)
    signcontact=tk.Frame(master=signwindow)
    signpassword=tk.Frame(master=signwindow)
    signentryname=tk.Frame(master=signwindow)
    signentrycontact=tk.Frame(master=signwindow)
    signentrypassword=tk.Frame(master=signwindow)
    signsubmit=tk.Frame(master=signwindow)
    signhead=tk.Label(master=signframe,
                     text="SIGN UP",
                     font=("Lucida Grande",25),
                     bg="green",
                     fg="white",
                     height=8,
                     width=50)
    signhead.pack(fill=tk.X,expand=True)
    signframe.pack()
    signlabelname=tk.Label(master=signname,
                          text="NAME",
                          font=("chiller",15),
                          bg="Yellow",
                          height=3,
                          width=30)
    signlabelname.pack()
    signname.pack()
    signentername=tk.Entry(master=signentryname,
                          fg="black",
                          bg="white",
                          width=35)
    signentername.pack()
    signentryname.pack()
    signlabelcontact=tk.Label(master=signcontact,
                          text="CONTACT",
                          font=("chiller",15),
                          bg="Yellow",
                          height=3,
                          width=30)
    signlabelcontact.pack()
    signcontact.pack()
    signentercontact=tk.Entry(master=signentrycontact,
                          fg="black",
                          bg="white",
                          width=35)
    signentercontact.pack()
    signentrycontact.pack()
    signlabelpassword=tk.Label(master=signpassword,
                          text="PASSWORD",
                          font=("chiller",15),
                          bg="Yellow",
                          height=3,
                          width=30)
    signlabelpassword.pack()
    signpassword.pack()
    signenterpassword=tk.Entry(master=signentrypassword,
                          fg="black",
                          bg="white",
                          width=35)
    signenterpassword.pack()
    signentrypassword.pack()
    signbutton=tk.Button(master=signsubmit,
                        text="SUBMIT",
                        fg="white",
                        bg="Blue",
                        height=3,
                        width=10,
                        command=signcommand)
    signbutton.pack()
    signsubmit.pack()
    signwindow.mainloop()
#about us page
def aboutf():
    aboutus=tk.Tk()
    aboutframe=tk.Frame(master=aboutus)
    text=tk.Label(master=aboutframe,
        text="DESIGNED BY:\n>HARDIK JAIN \n >RAGHAV GUPTA\n\n SPECIAL THANKS TO:\n >MRS. HEMLATA TANEJA",
                  font=("comic sans",40),
                  fg="white",
                  bg="orange",
                  height=8,
                  width=40)
    text.pack()
    aboutframe2=tk.Frame(master=aboutus)
    EXIT=tk.Button(master=aboutframe2,
                   text="EXIT",
                   height=3,
                   width=10,
                   command=aboutus.destroy)
    aboutframe2.pack()
    aboutframe.pack()
    EXIT.pack()
    aboutus.mainloop()
#mainpage
frame=tk.Frame(master=mwindow)
frame1=tk.Frame(master=mwindow)
frame2=tk.Frame(master=mwindow)
frame3=tk.Frame(master=mwindow)
heading=tk.Label(master=frame,
                 text="WHEEL  OF LUCK",
                 font=("times",30),
                 bg="Red",
                 fg="Black",
                 height=8,
                 width=40)
heading.pack(fill=tk.BOTH,expand=True)

Login=tk.Button(master=frame1,
                text="LOG IN",
                font=("times",20),
                bg="Blue",
                fg="White",
                height=3,
                width=15,
                command=loginf,
                )
Login.pack(fill=tk.BOTH,expand=True)

Signup=tk.Button(master=frame2,
                text="SIGN UP",
                font=("times",20),
                bg="Blue",
                fg="White",
                height=3,
                width=15,command=signf)
Signup.pack(fill=tk.BOTH,expand=True)

Aboutus=tk.Button(master=frame3,
                text="ABOUT US",
                font=("times",20),
                bg="Blue",
                fg="White",
                height=3,
                width=15,command=aboutf)
Aboutus.pack(fill=tk.BOTH,expand=True)

frame.pack(fill=tk.X)
frame1.pack()
frame2.pack()
frame3.pack()
mwindow.mainloop()

