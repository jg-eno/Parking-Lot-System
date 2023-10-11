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

def main():
    
    m =  Tk(screenName='Park', baseName=None, className='Park', useTk=1)
    m.state('zoomed')
    m.config(bg = "#ffd54f")
    #def prevPage():
        #m.destroy()
        #import home_page
        #home_page.root1()

    title = Label(text = 'Parking Details', font=('Times New Roman',60, 'bold'),bg = "#ffd54f",fg = "Red")
    title.pack()
    car_number = IntVar()
    car_owner = StringVar()
    phone_number = IntVar()
    d = datetime.datetime.now()
    parking_time = str(d.day)+" "+str(d.hour)
    vehicle=StringVar()


    def entry():
        #try:    
                    # car_reg_number = car_number.get()
                    # owner_name = car_owner.get()
                    # owner_phone_number = phone_number.get()
        fl = 0
        vehicle_menu = OptionMenu(m, vehicle, "CAR","BIKE","SUV")
        vehicle_menu.place(x=800,y=400)
        vehicle_type = vehicle.get()
        con = mysql.connector.connect(host='localhost', user='root', password='Enosh',charset="utf8")
        cur = con.cursor(buffered=True)
        cur.execute("use parkinglot")
        try:
                cur.execute("select Reg_No from Details")
                car_reg_number = car_number.get()
                if(type(car_reg_number) != int or len(str(car_reg_number)) != 4):
                    1/0
                a = cur.fetchall()
                print(a)
                try:
                    for x in a:
                        print(x)
                        if x[0] == str(car_reg_number):
                            1/0
                    try:
                        owner_name = car_owner.get()
                        if(len(owner_name)>30):
                            1/0
                        try:
                            owner_phone_number = phone_number.get()
                            if(str(owner_phone_number).isdigit() == False or len(str(owner_phone_number))!=10):
                                1/0
                            print("The number is: ",car_reg_number)
                            print("The owner is: ",owner_name)
                            print("Phone number is: ",owner_phone_number)
                            print("Vehicle type", vehicle_type)
                            print("Time", parking_time)
                            car_number.set("")
                            car_owner.set("")
                            phone_number.set("")
                            vehicle.set("")
                            # success_msg = Label(m, text="Vehicle added!")
                            # success_msg.grid(row=10,column=10)
                            # cur.execute("select * from slot")
                            
                            cur.execute("select * from slot")
                            slot_available = []
                            for x in cur:

                                if x[1] ==0:
                                    slot_available.append(x[0])
                            
                            car_slot_available = []
                            suv_slot_available=[]
                            bike_slot_available=[]
                            for i in slot_available:
                                if i.startswith('S'):
                                    suv_slot_available.append(i)
                                elif i.startswith('B'):
                                    bike_slot_available.append(i)
                                else:
                                    car_slot_available.append(i)
                            if vehicle_type.upper() == 'CAR':
                                if len(car_slot_available)>0:
                                    slot_index = random.randint(0,len(car_slot_available)-1) 
                                    slot = car_slot_available[slot_index]
                                    floor = "First Floor"
                                else:
                                    # slot_label = Label(m, text='No slot available!')
                                    # slot_label.grid(row=11,column=10)
                                    messagebox.showinfo("No Slot!", message="No slots available")
                                    fl = 1
                            elif vehicle_type.upper() == "SUV":
                                if len(suv_slot_available)>0:
                                    slot_index = random.randint(0,len(suv_slot_available)-1) 
                                    slot = suv_slot_available[slot_index]
                                    floor = "Second Floor"
                                else:
                                    # slot_label = Label(m, text='No slot available!')
                                    # slot_label.grid(row=11,column=10)
                                    messagebox.showinfo("No Slot!", message="No slots available")
                                    fl = 1
                            else:
                                if len(bike_slot_available)>0:
                                    slot_index = random.randint(0,len(bike_slot_available)-1) 
                                    slot = bike_slot_available[slot_index]
                                    floor = "Ground Floor"

                                else:
                                    # slot_label = Label(m, text='No slot available!')
                                    # slot_label.grid(row=11,column=10)
                                    messagebox.showinfo("No Slot!", message="No slots are available")
                                    fl = 1
                            # if len(slot_available)>0:
                            #     slot_index = random.randint(0,len(slot_available)-1)
                            #     slot = slot_available[slot_index]
                            #print(slot_available)
                            #print(car_slot_available)
                            #print(bike_slot_available)
                            #print(suv_slot_available)
                            #cur.execute("update slot set t_f={} where slot = '{}'".format(1,slot))
                            #con.commit()
                            # slot_label = Label(m, text="Slot assigned is {}. Direct to '{}' ".format(slot,floor))
                            # slot_label.grid(row=11,column=10)
                            if(fl == 0):
                                 messagebox.showinfo("Slot Assigned!", message="Slot assigned is {}. Direct to '{}' ".format(slot,floor))
                            # else:
                            #     slot_label = Label(m, text='No slot available!')
                            #     slot_label.grid(row=11,column=10)
                                 m.update()
                            # if len(owner_name)>30:
                            #     messagebox.showinfo("Wrong Input", message="Enter a short name")
                            # if str(car_reg_number).isdigit()!= True or (type(car_reg_number) is not int):
                            #     messagebox.showinfo("Wrong Input", message="Enter correct Registration Number")
                            # if str(owner_phone_number).isdigit()!=True or len(str(owner_phone_number))!=10:
                            #     messagebox.showinfo("Wrong Input", message="Enter correct Mobile Number")
                        
                                 cur.execute("INSERT INTO details VALUES (%s, %s, %s, %s, %s, %s)", (owner_name, car_reg_number, owner_phone_number,parking_time,vehicle_type,slot))
                                 con.commit()
                                 cur.execute("update slot set t_f={} where slot = '{}'".format(1,slot))
                                 con.commit()
                        except:
                            messagebox.showerror("Wrong Input", message="Enter correct Mobile Number")
                    except:
                       messagebox.showerror("Wrong Input", message="Enter a short name")
                except:
                    messagebox.showerror("Wrong Input",message = "Registration_No already exists !!!")
        except:
          messagebox.showerror("Wrong Input", message="Enter correct Car Registration Number")
            
                
        #if(type(car_reg_number) == int and len(str(car_reg_number)) == 4):                                     
            #l.append(car_reg_number)
            #count += 1
        #else:
           # messagebox.showinfo("Wrong Input", message="Enter correct Registration Number")
            
                    
        #if(len(owner_name)<30):                  
            #l.append(owner_name)
            #count += 1
        #else:
            #messagebox.showinfo("Wrong Input", message="Enter a short name")

                    
        #if(str(owner_phone_number).isdigit() and len(str(owner_phone_number))==10):                   
           # l.append(owner_name)
            #count += 1
       # else:
           # messagebox.showinfo("Wrong Input", message="Enter correct Mobile Number")
       # if(count == 3):
        #cur.execute("insert into Details values (%s,%s,%s)",(car_reg_number,owner_name,owner_phone_number))

        '''try:
            owner_name = car_owner.get()
            
            cur.execute("insert into Details (Driver) values ('{}')".format(owner_name))
            
        except:
            messagebox.showinfo("Wrong Input", message="Enter a short name")
        
        try:
            owner_phone_number = phone_number.get()
           
            cur.execute("insert into Details(Phone) values ({})".format(owner_phone_number))
            
                
        except:
            messagebox.showinfo("Wrong Input", message="Enter correct Mobile Number")'''
                
            
            




        
        
        '''print("The number is: ",car_reg_number)
        print("The owner is: ",owner_name)
        print("Phone number is: ",owner_phone_number)
        print("Vehicle type", vehicle_type)
        print("Time", parking_time)
        car_number.set("")
        car_owner.set("")
        phone_number.set("")
        vehicle.set("")
        # success_msg = Label(m, text="Vehicle added!")
        # success_msg.grid(row=10,column=10)
        # cur.execute("select * from slot")
        
        cur.execute("select * from slot")
        slot_available = []
        for x in cur:

            if x[1] ==0:
                slot_available.append(x[0])
        
        car_slot_available = []
        suv_slot_available=[]
        bike_slot_available=[]
        for i in slot_available:
            if i.startswith('S'):
                suv_slot_available.append(i)
            elif i.startswith('B'):
                bike_slot_available.append(i)
            else:
                car_slot_available.append(i)
        if vehicle_type.upper() == 'CAR':
            if len(car_slot_available)>0:
                slot_index = random.randint(0,len(car_slot_available)-1) 
                slot = car_slot_available[slot_index]
                floor = "First Floor"
            else:
                # slot_label = Label(m, text='No slot available!')
                # slot_label.grid(row=11,column=10)
                messagebox.showinfo("No Slot!", message="No slots available")
        elif vehicle_type.upper() == "SUV":
            if len(suv_slot_available)>0:
                slot_index = random.randint(0,len(suv_slot_available)-1) 
                slot = suv_slot_available[slot_index]
                floor = "Second Floor"
            else:
                # slot_label = Label(m, text='No slot available!')
                # slot_label.grid(row=11,column=10)
                messagebox.showinfo("No Slot!", message="No slots available")
        else:
            if len(bike_slot_available)>0:
                slot_index = random.randint(0,len(bike_slot_available)-1) 
                slot = bike_slot_available[slot_index]
                floor = "Ground Floor"

            else:
                # slot_label = Label(m, text='No slot available!')
                # slot_label.grid(row=11,column=10)
                messagebox.showinfo("No Slot!", message="No slots available")
        # if len(slot_available)>0:
        #     slot_index = random.randint(0,len(slot_available)-1)
        #     slot = slot_available[slot_index]
        #print(slot_available)
        #print(car_slot_available)
        #print(bike_slot_available)
        #print(suv_slot_available)
        #cur.execute("update slot set t_f={} where slot = '{}'".format(1,slot))
        #con.commit()
        # slot_label = Label(m, text="Slot assigned is {}. Direct to '{}' ".format(slot,floor))
        # slot_label.grid(row=11,column=10)
        messagebox.showinfo("Slot Assigned!", message="Slot assigned is {}. Direct to '{}' ".format(slot,floor))
        # else:
        #     slot_label = Label(m, text='No slot available!')
        #     slot_label.grid(row=11,column=10)
        m.update()
        # if len(owner_name)>30:
        #     messagebox.showinfo("Wrong Input", message="Enter a short name")
        # if str(car_reg_number).isdigit()!= True or (type(car_reg_number) is not int):
        #     messagebox.showinfo("Wrong Input", message="Enter correct Registration Number")
        # if str(owner_phone_number).isdigit()!=True or len(str(owner_phone_number))!=10:
        #     messagebox.showinfo("Wrong Input", message="Enter correct Mobile Number")

        cur.execute("INSERT INTO details VALUES (%s, %s, %s, %s, %s, %s)", (owner_name, car_reg_number, owner_phone_number,parking_time,vehicle_type,slot))
        con.commit()
        cur.execute("update slot set t_f={} where slot = '{}'".format(1,slot))
        con.commit()'''

        # success_msg.grid(row=10,column=10)
        # time.sleep(5)
        # m.update_idletasks()
        # time.sleep(3)
        
        # prevPage()
    #except TclError:
    #     print("HEllow world")
      #messagebox.showinfo("Wrong Input", message="Check the values given")
            

    number_label = Label(m, text = 'Car Number', font=('Times New Roman',30, 'bold'),bg = "#ffd54f")
    number_entry = Entry(m,textvariable = car_number, font=('Times New Roman',30,'normal'))

    owner_label = Label(m, text = 'Owner Name', font=('Times New Roman',30, 'bold'),bg = "#ffd54f")
    owner_entry = Entry(m, textvariable =car_owner, font=('Times New Roman',30,'normal'))

    phone_number_label = Label(m, text = 'Phone Number', font=('calibre',30, 'bold'),bg = "#ffd54f")
    phone_number_entry = Entry(m, textvariable =phone_number, font=('calibre',30,'normal'))


    vehicle_type_label = Label(m,text = 'Enter Vehcile type', font=('Times New Roman',30, 'bold'),bg = "#ffd54f")
    vehicle_type_entry = Entry(m, textvariable =vehicle, font = ('Times New Roman',30,'normal'))

    vehicle_menu = OptionMenu(m, vehicle, "CAR","BIKE","SUV")
    # number_label.grid(row=10,column=10, sticky="S")
    # number_entry.grid(row=10,column=11, sticky="S")
    # owner_label.grid(row=11,column=10, sticky="NESW")
    # owner_entry.grid(row=11,column=11, sticky="NESW")
    # phone_number_label.grid(row=12,column=10, sticky="NESW")
    # phone_number_entry.grid(row=12,column=11, sticky="NESW")
    # vehicle_type_label.grid(row=13,column=10, sticky="NESW")
    # vehicle_type_entry.grid(row=13,column=11, sticky="NESW")
    number_label.place(x=430,y=250)
    number_entry.place(x=800, y= 250)
    owner_label.place(x= 430, y =300)
    owner_entry.place(x= 800, y =300)
    phone_number_label.place(x=430, y =350)
    phone_number_entry.place(x=800, y =350)
    vehicle_type_label.place(x=430, y =400)
    vehicle_type_entry.place(x=800, y =400)
    menu = m.nametowidget(vehicle_menu.menuname)
    menu.config(font=('calibre',30, 'normal'))
    vehicle_menu.place(x=800,y=400)
    vehicle_menu.config(font=('calibre',30, 'normal'), width=18)
    sub_button = Button(m, text = 'Submit', command = entry)
    sub_button.config(font=('Times New Roman',30, 'normal'),width=13,bg = "SkyBlue1")
    sub_button.place(x=650, y = 500)
    
    


    #previous_page_button = Button(m, text = "Previous Page" , width = 50, activebackground='red', command = prevPage)
    #previous_page_button.config(font=('Times New Roman',20, 'bold'))  
    #previous_page_button.place(x=400, y =600)
    m.mainloop()


# main()


#drop down list
#update slot
