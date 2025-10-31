"""
menu - 
1. add record
2. update record
3. delete record
4. display record
5. exiting

db name - school
table - students
name,marks,stream,roll,section,class
ritu,400,science,345,b,11
"""

import mysql.connector as sqlcon

hostName='localhost'
portNo=3406
userName='root'
pwd=""

myconn=sqlcon.connect(host=hostName,port=portNo,user=userName,password=pwd)
mycursor=myconn.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS school")
myconn.close()

dbName="school"

myconn=sqlcon.connect(host=hostName,port=portNo,user=userName,password=pwd,database=dbName)
mycursor=myconn.cursor()

mycursor.execute(''' 
    CREATE TABLE IF NOT EXISTS students( 
        name VARCHAR(30) NOT NULL, 
        roll INT PRIMARY KEY, 
        class VARCHAR(5), 
        section VARCHAR(3), 
        stream VARCHAR(15), 
        marks VARCHAR(5) 
    )
''')

# mycursor.execute("DROP TABLE IF EXISTS students")

while True:
    print("Add Record / Update Record / Delete Record / Display Records / Exit -- 1 / 2 / 3 / 4 / 5")
    ch=int(input("Enter choice: "))
    match ch:
        case 1:
            # Insert
            name=input("Enter Name: ")
            roll=int(input("Enter Roll No.: "))
            cls=input("Enter Class: ")
            sec=input("Enter Section: ")
            stream=input("Enter Stream: ")
            marks=input("Enter Marks: ")
            query="INSERT INTO students VALUES (%s,%s,%s,%s,%s,%s)"
            val=(name,roll,cls,sec,stream,marks)
            mycursor.execute(query,val)
            myconn.commit()
            print(mycursor.rowcount,"record(s) inserted")
        case 2:
            # Update
            roll=int(input("Enter roll for which record want to be updated: "))
            mycursor.execute("SELECT * FROM students WHERE roll=%s",(roll,))
            row=mycursor.fetchone()
            name=input(f"Want to change name (or press Enter to keep current)? (current name: {row[0]}) - ") or row[0]
            cls=input(f"Want to change class (or press Enter to keep current)? (current class: {row[2]}) - ") or row[2]
            sec=input(f"Want to change section (or press Enter to keep current)? (current section: {row[3]}) - ") or row[3]
            stream=input(f"Want to change stream (or press Enter to keep current)? (current stream: {row[4]}) - ") or row[4]
            marks=input(f"Want to change marks (or press Enter to keep current)? (current marks: {row[5]}) - ") or row[5]
            query="UPDATE students SET name=%s, class=%s, section=%s, stream=%s, marks=%s WHERE roll=%s"
            val=(name,cls,sec,stream,marks,roll)
            mycursor.execute(query,val)
            myconn.commit()
            print(mycursor.rowcount,"record(s) updated")
        case 3:
            # Delete
            roll=int(input("Enter roll for which record want to be deleted: "))
            query="DELETE FROM students WHERE roll=%s"
            mycursor.execute(query,(roll,))
            myconn.commit()
            print(mycursor.rowcount,"record(s) deleted")
        case 4:
            # Display
            query="SELECT * FROM students"
            mycursor.execute(query)
            rows=mycursor.fetchall()
            print("(name, roll, class, section, stream, marks)")
            for row in rows:
                print(row)
            print(len(rows),"row(s) returned")
        case 5:
            # Exit
            myconn.close()
            exit()
        case _:
            print("Wrong Choice!!")