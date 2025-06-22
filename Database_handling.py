import mysql.connector as mysqlConnector

connection = mysqlConnector.connect(
    host="localhost",
    user="root",
    password="password24*",
    database="som"
)

if connection.is_connected():
    print("Successfully connected")
else:
    print("Failed connection")

cursor = connection.cursor(dictionary=True)
cursor.execute("CREATE TABLE IF NOT EXISTS product (name VARCHAR(100), price INT)")
# cursor.execute("INSERT INTO product (name, price) VALUES ('LAPTOP', 1200)")
# cursor.execute("INSERT INTO product (name, price) VALUES ('mobile', 2000)")
connection.commit()

cursor.execute("SELECT * FROM product")
records = cursor.fetchall()
print(records)

cursor.close()
