#inserts data into Project table

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "companydb"
    )
mycursor= mydb.cursor()

sql="""insert into project(proj_id,proj_name)values ("P1","Nationa;"),("P2","Regional")"""
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"Was inserted")
