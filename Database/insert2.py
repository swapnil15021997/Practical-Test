#inserts data into department table

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "companydb"
    )
mycursor= mydb.cursor()

sql="""insert into department(dept_id,dept_name)values ("D1","Information Tech"),("D2","Accounts")"""

mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"Was inserted")
