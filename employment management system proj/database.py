from logging import exception

import pymysql
from tkinter import messagebox
def connect_database():
    global mycursor,connection
    try:
       connection=pymysql.connect(host='localhost', port=3306,user='root',password='Kar2004@')
       mycursor=connection.cursor()

    except:
        messagebox.showerror('Error','Something went wrong,Please open mysql app before running again')
        return

    mycursor.execute('create database IF NOT EXISTS management_data')
    mycursor.execute('use management_data')
    mycursor.execute('create table IF NOT EXISTS data (Id VARCHAR(20),Name VARCHAR(50),Phone VARCHAR(15),Role VARCHAR(50),Gender VARCHAR(20),Salary DECIMAL(10,2))')

def insert(id,name,phone,role,gender,salary):
    mycursor.execute('insert into data values (%s,%s,%s,%s,%s,%s)',(id,name,phone,role,gender,salary))
    connection.commit()



def id_exists(id):
    mycursor.execute('select  count(*)  from data where id = %s',id)
    result = mycursor.fetchone()
    return result[0]>0

def fetch_empolyees():
    mycursor.execute('select * from data')
    result = mycursor.fetchall()
    return result

def update(id,new_name,new_phone,new_role,new_gender,new_salary):
    mycursor.execute('update data set name=%s,phone=%s,role=%s,gender=%s,salary=%s where id=%s',(new_name,new_phone,new_role,new_gender,new_salary,id))
    connection.commit()

def delete(id):
    mycursor.execute('delete from data where id=%s',id)
    connection.commit()

def search(option,value):
     mycursor.execute(f'select * from data where {option}=%s',value)
     result = mycursor.fetchall()
     return result

def deleteall_records():
    mycursor.execute('truncate table data ')
    connection.commit()


connect_database()