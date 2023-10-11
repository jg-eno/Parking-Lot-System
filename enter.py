import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', password='root',charset="utf8")
cur = con.cursor(buffered=True)
cur.execute("use parkinglot")
for i in range(16,65):
    a = 'c{}'.format(i)
    cur.execute("insert into slot values('{}',{})".format(a,0))
    con.commit()
for j in range(11,65):
    b = 's{}'.format(j)
    cur.execute("insert into slot values('{}',{})".format(b,0))
    con.commit()
for k in range(21,101):
    c = 'b{}'.format(k)
    cur.execute("insert into slot values('{}',{})".format(c,0))
    con.commit()
    