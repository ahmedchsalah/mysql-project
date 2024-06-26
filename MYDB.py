import mysql.connector


dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456"
)

cursor = dataBase.cursor()
cursor.execute("CREATE  DATABASE baseProject")

print('done')