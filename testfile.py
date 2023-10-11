# import mysql.connector

# con = mysql.connector.connect(host='localhost', user='root', password='root',charset="utf8")
# cur = con.cursor(buffered=True)

# cur.execute("use parkinglot")
# cur.execute("select * from slot")
# slot_available = []
# for x in cur:
#     if x[1] ==1:
#         slot_available.append(x[0])
    
# print(slot_available)
# import datetime
# a = datetime.datetime.now()
# print(type(a))
# b = a.split()
# print(a)
# print(b)
from time import strftime
parking_time = strftime('%H:%M:%S ')
print(parking_time)
print(type(parking_time))
print(parking_time.split())
(Driver,Reg_No,Phone,Park_Time,Type,Slot)