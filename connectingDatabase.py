import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='Hanood',
  password='honey12345@@',
  database='mydatabase'
)

mycursor = mydb.cursor()

# check if table exist
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM customers")
records = mycursor.fetchall()
for record in records:
    print(record)

# fecth Selected Columns
mycursor.execute("SELECT name, id FROM customers")
rec = mycursor.fetchall()
for recs in rec:
    print(recs)


mydb.commit()

# Close the cursor and connection
mycursor.close()
mydb.close()

# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("CREATE TABLE customers (name VARCHAR(225), Address VARCHAR (225), Phone VARCHAR(12) )")
# mycursor.execute(" ALTER TABLE customers ADD id INT AUTO_INCREMENT PRIMARY KEY")
"""query = "INSERT INTO customers (name, Address, Phone) VALUES (%s, %s, %s)"
val =  [
  ('Hannah', 'Mountain 21', '8436374'),
  ('Michael', 'Valley 345', '78456327'),
  ('Sandy', 'Ocean blvd 2', '3867452'),
  ('Betty', 'Green Grass 1', '3826437574'),
  ('Richard', 'Sky st 331', '29748365'),
  ('Susan', 'One way 98', '7675423'),
  ('Vicky', 'Yellow Garden 2', '092387478'),
  ('Ben', 'Park Lane 38', '9374483'),
  ('William', 'Central st 954', '82736725'),
  ('Chuck', 'Main Road 989', '28947558'),
  ('Viola', 'Sideway 1633', '97286477')
]
for record in val:
  mycursor.execute(query, record)"""