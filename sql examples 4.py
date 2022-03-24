import sqlite3

con = sqlite3.connect(r"D:\sql\projects\libary.db")
cur = con.cursor()
cur.execute("select avg(price) from books")
avgprice = cur.fetchone()[0]
print(f"Average price : {avgprice:6.2f}")
con.close()