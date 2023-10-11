import base64
import tkinter.font as font
from tkinter import *
from turtle import back, bgcolor
import mysql.connector
import datetime as dt
from time import strftime
import Exit
#from database_creation import *
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb  

#root =  Tk(screenName=None, baseName=None, className='Parking Lot', useTk=1)
#root.config(background=rgb_hack((255,204,159)))
#root.state('zoomed')

#DROP DOWN OPTION OF PARK
#CLASHING  OF 2 USERS
def root1():
    #DC()
    root =  Tk(screenName=None, baseName=None, className='Parking Lot', useTk=1)
    root.config(background="#ffd54f")
    root.state('zoomed')

    con = mysql.connector.connect(host='localhost', user='root', password='Enosh',charset="utf8")
    cur = con.cursor(buffered=True)


    title_label = Label(root, text= "Parking Lot Manager",width = 20, font=("Times New Roman", 40,'bold'), background="#ffd54f")
    title_label.place(relx=0,rely=0, relwidth=1, relheight=1)
    

    title_label.pack()

    date=dt.datetime.now()
    format_date=f"{date:%a, %b %d %Y}"
    date_label=Label(root, text=format_date, width = 20,font=("Times New Roman", 30),background=rgb_hack((255,153,102)))
    date_label.pack()
    def my_time():
        time_string = strftime('%H:%M:%S %p') # time format 
        time_label.config(text=time_string)
        time_label.after(1000,my_time) # time delay of 1000 milliseconds 

    time_label=Label(root,width = 20,font=("Times New Roman", 30),background="Red")
    my_time()
    time_label.pack()



    def parkpage():
        root.destroy()
        import park
        park.main()
        root1()
        # park.s()
    # def prevPage():
    #     m.destroy()
    #     import page3
    def CLOSE():
        root.destroy()

    def EXIT():
        root.destroy()
        Exit.Ex()
        root1()
    

    def Alter():
        root.destroy()
        import Alter
        Alter.mainloop_alter()
        root1()
    def Display():
        root.destroy()
        import Display
        Display.mainloop_display()
        root1()

    park_button = Button(root, text = 'Park',font = ("Times New Roman",20,'bold'), width = 30, height=2,background="SkyBlue1", foreground = 'Black',activebackground='blue', command = parkpage, justify=CENTER)
    park_button.pack()

    display_button = Button(root, text='Display',font = ("Times New Roman",20,'bold'),width = 30,height=2,background="SkyBlue1", foreground = 'Black',activebackground='blue', command = Display,justify=CENTER)    
    display_button.pack()

    alter_rate_button = Button(root, text='Alter Rate',font = ("Times New Roman",20,'bold'),width = 30,height=2,background="SkyBlue1", foreground = 'Black', command = Alter,justify=CENTER)
    alter_rate_button.pack()

    exit_button = Button(root, text  = 'Exit',font = ("Times New Roman",20,'bold'),width = 30,height=2,background="SkyBlue1", foreground = 'Black',command = EXIT,justify=CENTER)
    exit_button.pack()
    
    close_button = Button(root, text  = 'Close Application',font = ("Times New Roman",20,'bold'),width = 30,height=2,background="SkyBlue1", foreground = 'Black',command = CLOSE,justify=CENTER)
    close_button.pack()
    


    def shift():
        x1,y1,x2,y2 = canvas.bbox("marquee")
        if(x2<0 or y1<0): #reset the coordinates
            x1 = canvas.winfo_width()
            y1 = canvas.winfo_height()//2
            canvas.coords("marquee",x1,y1)
        else:
            canvas.move("marquee", -2, 0)
        canvas.after(1000//fps,shift)
    canvas=Canvas(root, background=rgb_hack((153,153,255)), height=5)
    canvas.pack(fill=BOTH, expand=1)
    cur.execute('use parkinglot')
    query="SELECT * FROM Rate"
    cur.execute(query)
    suv_rate = cur.fetchone()[1]
    car_rate = cur.fetchone()[1]
    bike_rate = cur.fetchone()[1]
    text_var=("Today's Rate: SUV: {}/hr     CAR: {}/hr      BIKE: {}/hr".format(suv_rate,car_rate,bike_rate))
    text=canvas.create_text(0,-2000,text=text_var,font=('Times New Roman',20,'bold'),fill='black',tags=("marquee",),anchor='w')
    x1,y1,x2,y2 = canvas.bbox("marquee")
    width = x2-x1
    height = y2-y1
    canvas['width']=width
    canvas['height']=5 
    fps=40   #Change the fps to make the animation faster/slower
    shift()
    root.mainloop()

root1()
