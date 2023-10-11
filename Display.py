from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
def mainloop_display():
     BIKES = []
     CARS  = []
     SUV  = []
     TEXT = []
     con = mysql.connector.connect(host = 'localhost',user = 'root',password = 'Enosh', charset='utf8')
     cur = con.cursor()
     root = Tk()
     canvas1 = Canvas(root, width=1360, height=750,bd = 0,highlightthickness = 0)
     canvas1.pack()
     cur.execute("use parkinglot")
     cur.execute("select * from slot")
     data = cur.fetchall()

     def display():   
          # global root ,BIKES,CARS,con,cur,SUV,TEXT,canvas1, data
          # BIKES = []
          # CARS  = []
          # SUV  = []
          # TEXT = []
          # con = mysql.connector.connect(host = 'localhost',user = 'root',password = 'root', charset='utf8')
          # cur = con.cursor()
          # root = Tk()
          # canvas1 = Canvas(root, width=1360, height=750,bd = 0,highlightthickness = 0)
          # canvas1.pack()
          # cur.execute("use parkinglot")
          # cur.execute("select * from slot")
          # data = cur.fetchall()
          root.title("Parking Lot View")
          root.geometry("300x300")
          root.minsize(1350, 700)
          root.maxsize(1350, 700)
          bg = ImageTk.PhotoImage(Image.open("Retro.jpg"))
          global car,bike,suv,rc,rs,rb
          car = ImageTk.PhotoImage(Image.open("Car.jpg"))
          rc = ImageTk.PhotoImage(Image.open("Road C.jpg"))
          rb = ImageTk.PhotoImage(Image.open("Road B.jpg"))
          rs = ImageTk.PhotoImage(Image.open("Road S.jpg"))
          bike = ImageTk.PhotoImage(Image.open("Bike.jpg"))
          suv = ImageTk.PhotoImage(Image.open("Truck.jpg"))     
          background = canvas1.create_image(0, 0, anchor=NW, image=bg)
          canvas1.create_text(650, 30, text="Parking Lot View", fill="yellow", font=('Times New Roman',30,'bold'))  
          B = Button(root,text = "B",font = ("Times New Roman",14),width = 4,fg = "Yellow",bg = 'Red',bd = 0,command = Bike)
          W_B = canvas1.create_window(1100,15,anchor = NW,window = B)
          C = Button(root,text = "C",font = ("Times New Roman",14),width = 4,fg = "Purple",bg = 'Orange',bd = 0,command = Car)
          W_C = canvas1.create_window(1170,15,anchor = NW,window = C)
          S = Button(root,text = "S",font = ("Times New Roman",14),width = 4,fg = "Blue",bg = 'White',bd = 0,command = Suv)
          W_S = canvas1.create_window(1240,15,anchor = NW,window = S)
          Bike()
          root.update()
          root.mainloop()
     def Bike():
          DELETE()
          TEXT.append(canvas1.create_text(150, 30, text="Ground Floor : Bikes", fill="yellow", font=('Times New Roman',24,'bold')))
          b1 = 0
          b2 = 120     
          for x in data:
               if(x[0][0] == "B"):
                    if x[1] == 1:
                         BIKES.append(canvas1.create_image(4+68*b1, b2, anchor=NW, image=bike))
                         root.update_idletasks()
                         root.update()
                    else:
                         BIKES.append(canvas1.create_image(4+68*b1, b2, anchor=NW, image=rb))
                         root.update_idletasks()
                         root.update()
                    b1 += 1
                    if(b1 % 20 == 0):
                         b2 += 110
                         b1 = 0

     def Car():
          DELETE()
          TEXT.append(canvas1.create_text(150, 30, text="First Floor : Cars", fill="yellow", font=('Times New Roman',24,'bold')))
          c1 = 0
          c2 = 60     
          for x in data:
               if (x[0][0] == "C"):
                    if x[1] == 1:
                         CARS.append(canvas1.create_image(25+80*c1, c2, anchor=NW, image=car))
                         root.update_idletasks()
                         root.update()
                    else:
                         CARS.append(canvas1.create_image(25+80*c1, c2, anchor=NW, image=rc))
                         root.update_idletasks()
                         root.update()
                    c1 += 1
                    if(c1 % 16 == 0):
                         c2 += 160
                         c1 = 0
     def Suv():
          DELETE()
          TEXT.append(canvas1.create_text(150, 30, text="Second Floor : SUV", fill="yellow", font=('Times New Roman',24,'bold')))
          s1 = 0
          s2 = 60     
          for x in data:
               if(x[0][0] == "S"):
                    if x[1] == 1:
                         SUV.append(canvas1.create_image(30+80*s1, s2, anchor=NW, image=suv))
                         root.update_idletasks()
                         root.update()
                    else:
                         SUV.append(canvas1.create_image(30+80*s1, s2, anchor=NW, image=rs))
                         root.update_idletasks()
                         root.update()
                    s1 += 1
                    if(s1 % 16 == 0):
                         s2 += 165
                         s1 = 0
     def DELETE():
          for x in CARS:
               canvas1.delete(x)
          for x in BIKES:
               canvas1.delete(x)
          for x in SUV:
               canvas1.delete(x)
          for x in TEXT:
               canvas1.delete(x)
     #def prevPage():
        #root.destroy()
        #import home_page
        #home_page.root1()          
     #previous_page_button = Button(root, text = "Previous Page" , width = 50, activebackground='red', command = prevPage)
     #previous_page_button.config(font=('calibre',10, 'bold'))  
     #previous_page_button.place(x=400, y =680)
     display()

