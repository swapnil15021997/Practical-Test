import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "companydb"
    )
mycursor= mydb.cursor()

mycursor.execute("Create table employee(emp_id integer not null,name varchar(20) not null,salary integer(10),dept_id varchar(10),primary key(emp_id))")


mycursor.execute("Create table Project(proj_id varchar(10),proj_name varchar(20) not null,primary key(proj_id))")

mycursor.execute("Create table Department(dept_id varchar(10),dept_name varchar(20) not null,primary key(dept_id))")

mycursor.execute("create table junction(proj_fk varchar(10) not null,emp_fk integer not null,foreign key(proj_fk) References Project(proj_id),foreign key(emp_fk) References employee(emp_id))")


mycursor.execute("create table junctions(proj_fk varchar(10) not null,emp_fk integer not null,foreign key(proj_fk) References Project(proj_id),foreign key(emp_fk) References employee(emp_id))")
