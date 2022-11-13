#inserts data into employee table

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "companydb"
    )
mycursor= mydb.cursor()

sql="""insert into employee(emp_id,name,salary,dept_id)values (101,"Swapnil",10000,"D1"),
     (102,"Amit",15000,"D2")"""

mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"Was inserted")
