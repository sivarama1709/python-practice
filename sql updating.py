import sqlite3
con=sqlite3.connect(r"D:\sql\projects\test.db")
cur=con.cursor()
#update the data in a table row
try:
    #taking data from the users
    ID=input("enter ID             :")
    AMOUNT=input("enter new AMOUNT :")
    values=(AMOUNT,ID)
    cur.execute("UPDATE EXPENSES SET AMOUNT=? WHERE ID=?",values)
    if cur.rowcount==1:
        print("UPDATED SUCCESSFULLY!")
        con.commit()
    else:
        print("ID not found!")
except Exception as ex:
    print("Sorry! ERROR: " , ex.message)
finally:
    con.close()