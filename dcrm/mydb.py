import mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'imad2324686'
)

# prepare cursor Object:
cursorObject = dataBase.cursor()

# Create a dataBase
cursorObject.execute("CREATE DATABASE imad")

print('All done !!')