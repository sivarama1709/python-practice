import sqlite3
con = sqlite3.connect(r"D:\sql\projects\office.db")    
cur = con.cursor()                                     
deptid=input("enter department id: ")
cur.execute("delete from departments where deptid = ?",(deptid,))
if cur.rowcount==1:
    print("successfully deleted!")
    con.commit()
else:
    print("failed to delete id not found!")