from tkinter import *
import mysql.connector
from tkinter import messagebox
def mainloop_alter():
     def alter():
          global con,cur
          con = mysql.connector.connect(host = 'localhost',user = 'root',password = 'Enosh', charset='utf8')
          cur = con.cursor()
          cur.execute("use parkinglot")
          global root
          root = Tk()
          root.title("Alter Rate")
          root.geometry("300x300")
          root.minsize(500, 500)
          root.maxsize(500, 500)
          global vt , rt 
          root.config(bg = "#ffd54f")
          l = Label(root,text = "Alter Rate")
          l.config(font = ("Times New Roman",50,'bold'),bg = "#ffd54f",fg = "Blue")
          l.pack()
          t = Label(root,text = "Vehicle Type : ")
          t.config(font = ("Times New Roman",30,'bold'),bg = "#ffd54f",fg = "Black")
          t.pack()
          t.place(x = 20,y = 120)
          vt = StringVar()
          rt = IntVar()
          d = OptionMenu(root,vt,"CAR","BIKE","SUV")
          d.pack()
          d.place(x = 280,y = 130)
          r = Label(root,text = "New Rate : ")
          r.config(font = ("Times New Roman",30,'bold'),bg = "#ffd54f",fg = "Black")
          r.pack()
          r.place(x = 20,y = 200)
          Rt = Entry(root,textvariable = rt,font = ("Times New Roman",18,'bold'),width = 6)
          Rt.pack()
          Rt.place(x = 230,y = 215)  
          sb = Button(root,text = "Submit",bg = "SkyBlue1",fg = "Black",bd = 0,font = ("Times New Roman",18,'bold'),command = Submit)
          sb.pack()
          sb.place(x = 200,y = 400)
          #previous_page_button = Button(root, text = "Previous Page" , width = 50, activebackground='red', command = prevPage)
          #previous_page_button.config(font=('calibre',10, 'bold'))  
          #previous_page_button.place(x=80, y =300)
          root.mainloop()
     def Submit():
          try:
               Vec_Type = vt.get()
               Rate = rt.get()
               cur.execute("update rate set price = {} where Type = '{}'".format(Rate,Vec_Type))
               root.destroy()
               con.commit()
               cur.close()
               con.close()
               messagebox.showinfo("UPDATED","The New Rates are updated")
          except:
               messagebox.showerror("ERROR","Check the entered rate")
         #def prevPage():
        #root.destroy()
        #import home_page
        #home_page.root1()          
     # previous_page_button = Button(root, text = "Previous Page" , width = 50, activebackground='red', command = prevPage)
     # previous_page_button.config(font=('calibre',10, 'bold'))  
     # previous_page_button.place(x=400, y =680)
     alter()

