# install Mysql on your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root'
)

# prepare a cursor Object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute('CREATE DATABASE dcrm')

print('Database Created!!')
