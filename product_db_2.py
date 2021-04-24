import psycopg2
#make connection
conn=psycopg2.connect(host="localhost",
                     dbname="Product_database",
                     user="postgres", password="1831")
cur=conn.cursor()
cur.execute("create table Product_database (bill_no integer, customer_name text, c_number integer , c_address text, product_name text, p_rate integer, p_qty integer)")
conn.commit()
print("Table is Created..!!")

cur.close()
conn.close()