from tkinter import *
import math, random, os
from tkinter import messagebox

class Erp:
    def __init__(self, master):
        self.master = master
        self.master.title("ERP")
        self.master.geometry("1920x1080")
        self.master.iconbitmap("2K main.ico")
        self.master.config(bg="#2c3e50")
        self.title = Label(self.master, text="2K", font=("Cairo", 30, "bold"), fg="#f5f6fa", bg="#e1b12c")
        self.title.pack(fill=X)
        #Customer#
        F1 = Frame(self.master, bg="#2f3640", width=220, height=420)
        F1.pack(fill=Y, side=LEFT)
        tit = Label(F1, text="Customer Info", font=("Cairo", 12), fg="#f5f6fa", bg="#2f3640", justify=CENTER)
        tit.place(x=10, y=10)
        his_name = Label(F1, text="Name", font=("Cairo", 12), fg="#f5f6fa", bg="#2f3640")
        his_name.place(x=10, y=60)
        
master = Tk()
obj = Erp(master)
master.mainloop()    
    