from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import sys
pro = Tk()
pro.geometry("800x450")
pro.title("ERP")
pro.iconbitmap("2K main.ico")
title = Label(pro, text="2K", font=("Cairo", 30, "bold"), fg="#f5f6fa", bg="#e1b12c")
title.pack(fill=X)

def  about():
    messagebox.showinfo("About", "KOS OMAK")
def login():
    user = En1.get()
    passw = En2.get()
    if user == 'admin' and passw == '1234':
        messagebox.showinfo("Login", "Welcome")
    else:
        messagebox.showinfo("Login", "3amly feeha hacker ya ksmk")
F1 = Frame(pro, bg="#2f3640", width=220, height=420)
F1.pack(fill=Y, side=LEFT)
#F1.place(x=0, y=80)
Title1 = Label(F1, text="Main Menu", font=("Cairo", 20), fg="#f5f6fa", bg="#2f3640")
Title1.place(x=10, y=10)
Title2 = Label(F1, text="2K", font=("Cairo", 20), fg="#f5f6fa", bg="#2f3640")
Title2.place(x=10, y=60)

B1 = Button(F1, text="Home", font=("Cairo", 15), fg="#f5f6fa", bg="#e1b12c", width=15, height=1)
B1.place(x=6, y=110)
B2 = Button(F1, text="About", font=("Cairo", 15), fg="#f5f6fa", bg="#e1b12c", width=15, height=1, command=about)
B2.place(x=6, y=190)
B3 = Button(F1, text="Exit", font=("Cairo", 15), fg="#f5f6fa", bg="#e1b12c", width=15, height=1, command=pro.destroy)
B3.place(x=6, y=270)

photo = PhotoImage(file="2K main.png")
imo = Label(pro, image=photo)

F2 = Frame(pro, bg="#2c3e50", width=2920, height=1080)
F2.place(x=220, y=81)
L1 = Label(F2, text="User Name", font=("Cairo", 16), fg="#f5f6fa", bg="#2c3e50")
L1.place(x=10, y=25)
L2 = Label(F2, text="Password", font=("Cairo", 16), fg="#f5f6fa", bg="#2c3e50")
L2.place(x=10, y=100)
En1 = Entry(F2, font=("Cairo", 14), fg="#2c3e50", bg="#f5f6fa", width=30)
En1.place(x=150, y=30)
En2 = Entry(F2, font=("Cairo", 14), fg="#2c3e50", bg="#f5f6fa", width=30, show="*")
En2.place(x=150, y=105)
B4 = Button(F2, text="Login", font=("Cairo", 15), fg="#f5f6fa", bg="#e1b12c", width=15, height=1, command=login)
B4.place(x=10, y=180)
pro.mainloop()
