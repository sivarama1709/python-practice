import sqlite3
con=sqlite3.connect(r"D:\sql\projects\test.db")
cur=con.cursor()
#create a table 
try:
    cur.execute("CREATE TABLE EXPENSES(ID INTEGER,DATE TEXT,DESC TEXT,AMOUNT REAL)")
    print("TABLE EXPENCES CERATED SUCCESSFULLY !")
except Exception as ex:
    print("Sorry! error:",ex.message)
finally:
    con.close()