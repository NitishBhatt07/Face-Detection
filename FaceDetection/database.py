import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

'''
try:
    connection = mysql.connector.connect(
        host = 'localhost',
        database = 'attendance',
        user = 'root',
        password = 'root'
        )

    insert_query = "INSERT INTO attdata(ID,Name) values(1,'nb')"
    cursor = connection.cursor()
    cursor.execute(insert_query)
    connection.commit()
    print("sucessfull")
    cursor.close()

except mysql.connector.Error as error:
    print("failed {}".format(error))

finally:
    if(connection.is_connected()):
        connection.close()
        print("connection closed")
'''

def connect_database(name,img):
    try:
        connection = mysql.connector.connect(
        host = 'localhost',
        database = 'attendance',
        user = 'root',
        password = 'root'
        )

        insert_query = "INSERT INTO attdata(Name,photo) values%s,%s)"
        args = (name,img)
        cursor = connection.cursor()
        cursor.execute(insert_query,args)
        connection.commit()
        print("sucessfull")
        cursor.close()
    except mysql.connector.Error as error:
        print("failed {}".format(error))

    finally:
        if(connection.is_connected()):
            connection.close()
            print("connection closed")

    
    
