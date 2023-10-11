from curses.ascii import isdigit
from email import message
from re import M
from sqlite3 import Date
from tkinter import *
from tkinter import messagebox
from tokenize import String
from turtle import width
from unicodedata import name
import mysql.connector
import time
import random
import datetime as dt
from time import strftime
import datetime

m =  Tk(screenName=None, baseName=None, className='Parking Lot', useTk=1)
m.config(background="#ffd54f")
m.state('zoomed')

user = StringVar()
pw = StringVar()
def gotomainpage():
    m.destroy()
    import home_page
    home_page.root1()
def submit():
    u1 = user.get()
    p1 = pw.get()
    if u1 == 'admin' and p1 == 'password':
        gotomainpage()
    else:
        messagebox.showerror("Wrong Input", message = "Incorrect ID or Passoword")
Header = Label(m, text='Welcome To Parking Lot Manager !!!',font=('Times New Roman',50, 'bold'),bg = "#ffd54f",fg = "Blue")
Header.place(x=160,y=20)
        
Title = Label(m, text='Login Page',font=('Times New Roman',50, 'bold'),bg = "#ffd54f",fg = "Red")
Title.place(x=530,y=100)

user_name_label = Label(m, text='USERNAME',font=('Times New Roman',30, 'bold'),bg = "#ffd54f")
user_name_entry = Entry(m, textvariable=user,font=('Times New Roman',30,'normal'))

password_label = Label(m, text="PASSWORD", font=('Times New Roman',30, 'bold'),bg = "#ffd54f")
password_entry = Entry(m, textvariable=pw,font=('Times New Roman',30,'normal'),show='*')
user_name_label.place(x=430,y=250)
user_name_entry.place(x=800, y =250)

password_label.place(x=430,y=300)
password_entry.place(x=800,y=300)

submituser = Button(m, text = 'Submit', command = submit)
submituser.config(font=('Times New Roman',30, 'normal'),width=13,bg = "SkyBlue1")
submituser.place(x=650, y = 500)

m.mainloop()
