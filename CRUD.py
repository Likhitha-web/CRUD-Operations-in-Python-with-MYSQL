# CRUD-Operations
#Create, Read, Update, Delete a table in MYSQL using Python

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="user_information")
mycursor = mydb.cursor()
sql= "INSERT INTO users (`Username`, `First Name`, `Last Name`, `Address`, `Password`) VALUES (%s, %s, %s, %s, %s)"
users= [('Tina123', 'Tina', 'Roy', '123 Austin Ave', 'ilovewhite'),
        ('Rama', 'Rama', 'Devi', '80 liberty ave', 'Vanillaicecream'),
        ('Sita', 'Sita', 'Kumar', '12-13-757/A/1', 'ilovepepsi'),
        ('Gita', 'Gita', 'Narayan', '7-17/56 Gita Nagar', 'CrazyJamuns'),
        ('Rita', 'Rita', 'Kashyap', '589 lincoln drive', 'Lobster'),
        ('Tina123', 'Tina', 'Roy', '123 Austin Ave', 'ilovewhite')]
mycursor.executemany(sql, users)
mydb.commit()


mycursor.execute("select * from users")
myresult = mycursor.fetchall()
for i in myresult:
    print(i)

  
sql = "UPDATE users SET Lastname = '%s' WHERE Username = %s"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")



sql = "DELETE FROM users WHERE Usename = "Rama"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")
