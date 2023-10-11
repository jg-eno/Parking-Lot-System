import tkinter as tk
m =  tk.Tk(screenName=None, baseName=None, className='Tk', useTk=1)
# m.geometry("600x400")
car_number = tk.IntVar()
car_owner = tk.StringVar()
def entry():
    number = car_number.get()
    owner = car_owner.get()

    print("The number is: ",number)
    print("The owner is: ",owner)
    car_number.set("")
    car_owner.set("")

number_label = tk.Label(m, text = 'Car Number', font=('calibre',10, 'bold'))
number_entry = tk.Entry(m,textvariable = car_number, font=('calibre',10,'normal'))

owner_label = tk.Label(m, text = 'Owner Name', font=('calibre',10, 'bold'))
owner_entry = tk.Entry(m, textvariable =car_owner, font=('calibre',10,'normal'))

sub_button = tk.Button(m, text = 'Submit', command = entry)

number_label.grid(row=0,column=0)
number_entry.grid(row=0,column=1)
owner_label.grid(row=1,column=0)
owner_entry.grid(row=1,column=1)
sub_button.grid(row=2,column=1)

# w = tk.button(master, option=value)
button = tk.Button(m,text='Stop',width=25,command=m.destroy)
# button1 = tk.Button(m, text = 'Check', width = 100, activebackground='red', command=
# button1.pack()
# w = tk.Canvas(m, width=50, height=50)
# button.pack()
m.mainloop()
