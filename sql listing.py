import sqlite3
con=sqlite3.connect(r"D:\sql\projects\test.db")
cur=con.cursor()
#list rows from a table
try:
    cur.execute("SELECT * FROM EXPENSES ORDER BY ID")
    for row in cur.fetchall():
        print(row[1],row[2],row[3])
    else:
        cur.close()
except Exception as ex:
    print("sorry! error :",ex.message)
finally:
    con.close()