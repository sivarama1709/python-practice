import sqlite3
con=sqlite3.connect(r"D:\sql\projects\test.db")
cur=con.cursor()
# insertion of data into database
try:
    #take data from user
    ID=input("Enter id            :")
    DATE=input("Enter date        :")
    DESC=input("Enter description :")
    AMOUNT=input("Enter amount    :")
    
    row=(ID,DATE,DESC,AMOUNT)
    cur.execute("INSERT INTO EXPENSES VALUES(?,?,?,?)",row)
    con.commit()
    print("ADDED SUCESSFULLY !")
except Exception as ex:
    print("Sorry! error:",ex.message)
finally:
    con.close()