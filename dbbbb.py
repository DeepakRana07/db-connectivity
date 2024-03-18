import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "admin",
    database = "semalt"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE deepak (name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO deepak (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql,val)
mycursor.execute("Select * from deepak")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)