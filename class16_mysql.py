import mysql.connector
database1 = mysql.connector.connect(host="localhost",user="root",passwd="20Tola18",database= "pythonclass16_db")
action = database1.cursor()
# action.execute("CREATE TABLE products(productid INT AUTO_INCREMENT, name VARCHAR(50),description VARCHAR(50),brand VARCHAR(50),model VARCHAR(50),price INT, discount INT, newprice INT)" )

create = "INSERT INTO products (name_,descri,brand,model,price,discount,newprice) VALUES (%s ,%s, %s,%s,%s,%s,%s)"



# print(action)
# action.execute("SHOW TABLES")
# for table in action:
#     print(table)