import sqlite3

con = sqlite3.connect(r"D:\sql\projects\office.db")    
cur = con.cursor()                                     

cur.execute("select * from departments order by deptname")
for row in cur.fetchall():
    print(row[0], row[1], row[2])