import random
import string_utils #has this awesome library to shuffle strings
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root",passwd="1459142337@Ani",database="password_storer")
mycursor=mydb.cursor()

def existing_password():

     app_data=str(input("what is the name of the website you want to save data for"))
     password=str(input("enter the password"))
     mycursor=mydb.cursor()


     insert_db=("INSERT INTO passwordapp(app,password)"
            "VALUES(%s, %s)"
     )
     dt=(app_data,password)
     try:
      mycursor.execute(insert_db,dt)
      mydb.commit()

     except:
        mydb.rollback()

     print("data inserted")
     mydb.close()

def generate_password():
    
    string_small="abcdefghijklmnopqrstuvwxyz"
    string_upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string_number="1234567890"
    string_character="!@#$%^&*()_"
    app_data=str(input("for which app do you need the password for"))
    password=""

    for len in range(4):
        password=password+random.choice(string_small)

    for len in range(4):
        password=password+random.choice(string_upper)

    for len in range(4):
        password=password+random.choice(string_number)

    for len in range(4):
        password=password+random.choice(string_character)

    password=string_utils.shuffle(password)

    print("your password is "+ password + " for the app " + app_data)

    

    insert_db=("INSERT INTO passwordapp(app,password)"
            "VALUES(%s, %s)"
    )
    dt=(app_data,password)

    try:
        mycursor.execute(insert_db,dt)
        mydb.commit()

    except:
        mydb.rollback()

    print("data inserted")
    mydb.close()

master_password="1459142337"
trial_password=""
while(trial_password!=master_password):
    trial_password=str(input())

print("press s for saving password and press c for creating and saving password")
z=str(input())

if(z=="s"):
   existing_password()

else:
    generate_password()


