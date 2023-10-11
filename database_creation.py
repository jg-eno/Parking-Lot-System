import mysql.connector
def DC():
     con = mysql.connector.connect(host = 'localhost',user = 'root',password= 'root', charset='utf8')
     cur = con.cursor()
     cur.execute("create database if not exists parkinglot")
     cur.execute("use parkinglot")

     cur.execute("create table if not exists details (Driver char(30) NOT NULL, Reg_No char(15) NOT NULL, Phone numeric(10), Park_Time char(100), Type char(4) NOT NULL, Slot char(3) PRIMARY KEY )")
     cur.execute("create table if not exists rate (Type char(4), price numeric(4))")
     cur.execute("create table if not exists slot (slot char(4), t_f numeric(1))")
     cur.execute("delete from slot")
     c = 1
     for x in range(20):
          cur.execute("insert ignore into slot values('{}',{})".format("B"+str(c),0))
          c += 1
     for x in range(20):
          cur.execute("insert ignore into slot values('{}',{})".format("B"+str(c),0))
          c += 1
     for x in range(20):
          cur.execute("insert ignore into slot values('{}',{})".format("B"+str(c),0))
          c += 1
     for x in range(20):
          cur.execute("insert ignore into slot values('{}',{})".format("B"+str(c),0))
          c += 1
     for x in range(20):
          cur.execute("insert ignore into slot values('{}',{})".format("B"+str(c),0))
          c += 1
     c = 1
     for x in range(16):
          cur.execute("insert ignore into slot values('{}',{})".format("C"+str(c),0))
          c += 1
     for x in range(16):
          cur.execute("insert ignore into slot values('{}',{})".format("C"+str(c),0))
          c += 1
     for x in range(16):
          cur.execute("insert ignore into slot values('{}',{})".format("C"+str(c),0))
          c += 1
     for x in range(16):
          cur.execute("insert ignore into slot values('{}',{})".format("C"+str(c),0))
          c += 1
     c = 1
     for x in range(16):
          cur.execute("insert ignore into slot values('{}',{})".format("S"+str(c),0))
          c += 1
     for x in range(16):
          cur.execute("insert ignore into slot values('{}',{})".format("S"+str(c),0))
          c += 1
     for x in range(16):
          cur.execute("insert ignore into slot values('{}',{})".format("S"+str(c),0))
          c += 1
     for x in range(16):
          cur.execute("insert ignore into slot values('{}',{})".format("S"+str(c),0))
          c += 1

     con.commit()
     cur.close()
     con.close()

DC()
