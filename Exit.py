# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settinimporimpo
from tkinter import *
from tkinter import messagebox
import mysql.connector
import datetime as dt
con=mysql.connector.connect(host="localhost",user="root",password='Enosh',database='parkinglot', charset='utf8')
cur=con.cursor()
def check():
    m = q.get()
    print(m)
    cur.execute("Select * from details where reg_no='{}'".format(m))
    x = cur.fetchone()
    print(x)
    if(x != "" and x != None and m.isdigit()):
        root.destroy()
        m = int(m)
        top = Tk()
        top.title("Exit Details")
        top.geometry("300x300")
        top.minsize(500, 500)
        top.maxsize(500, 500)
        top.config(bg ="#ffd54f")
        print(x)
        a, b, c, d, e,f = x
        label = Label(top, text="BILL",bg="#ffd54f",bd = 20,fg = 'red',font = ("Times new roman",35,'bold')).pack()
        labe1 = Label(top, text="Name : "+str(a),bg="#ffd54f",bd = 10,font = ("Times new roman",20,'bold')).pack()
        labe2 = Label(top, text="Reg_no : "+str(b),bg="#ffd54f",bd=10, font=("Times new roman",20,'bold')).pack()
        labe3 = Label(top, text="Phone no : "+str(c),bg="#ffd54f", bd=10, font=("Times new roman",20,'bold')).pack()
        labe4 = Label(top, text="Parking time : "+d,bg="#ffd54f", bd=10, font=("Times new roman",20,'bold')).pack()
        labe5 = Label(top, text="Type : "+str(e), bd=10,bg="#ffd54f", font=("Times new roman",20,'bold')).pack()
        labe6 = Label(top, text="Slot : "+str(f),bd=10,bg="#ffd54f",font=("Times new roman",20,'bold')).pack()
        date = dt.datetime.now()
        l = d.split()
        d1, h1 = int(l[0]),int(l[1])
        d2 = date.day
        h2 = date.hour
        h = (d2 - d1) * 24 + h2 - h1
        cur.execute("Select price from rate where type = '{}'".format(e))
        print(e)
        y = cur.fetchone()
        labe7 = Label(top, text="Amount : " + str(int(y[0])*h), bd=10,bg="#ffd54f", font=("Times new roman", 20,'bold')).pack()
        cur.execute("update slot set t_f = {} where slot='{}'".format(0,f))
        con.commit()
        top.mainloop()
    else:
        messagebox.showerror("Error", "Enter the correct Registration Number")

def Ex():
    try:
        global root
        root = Tk()
        root.title("Exit")
        root.geometry("300x300")
        root.minsize(400, 400)
        root.maxsize(400, 400)
        root.config(bg="#ffd54f")
        global q
        q = StringVar()
        n=Label(root, text="Enter registration no :",bg="#ffd54f",width=15,bd = 10,font = ("Times new roman",25,'bold'))
        n.pack()
        n.place(x=10,y=20)
        e = Entry(root,textvariable=q,width=15,bg="white",font = ('Times New Roman',20))
        e.pack()
        e.place(x=80,y=100)
        myButton = Button(root, text="Submit",fg="black",font = ("Times New Roman",20,'bold'), bg="skyblue1",width = 6,height = 1,command = check)
        myButton.pack()
        myButton.place(x = 150,y = 250)
        root.mainloop()
    except:
        messagebox.showerror("Error", "Enter the correct Registration Number")










