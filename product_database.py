import psycopg2
#make connection
conn=psycopg2.connect(host="localhost",
                     dbname="Product_database",
                     user="postgres",
                     password="1831")
cur=conn.cursor()
op=0

while op!=3:
    print("Welcome to Walmart")
    print("Enter 1 for Entry")
    print("Enter 2 for Print")
    print("Enter 3 for Exit..!!")
    op = int(input("Please enter your option: "))
    if op==1:
        op2="yes"
        while op2.lower()=="yes":
            print("<----------ENTRY---------->")
            bill_no= int(input("Enter Bill No.: "))
            customer_name=int(input("Enter Customer Name: "))
            c_number= int(input("Enter Mobile No.: "))
            c_address=int(input("Enter Address: "))
            product_name=int(input("Enter Product Name: "))
            p_rate=int(input("Enter Rate: "))
            p_qty=int(input("Enter Qty: "))
            cur.exceute("insert into Product_database values(%s, %s, %s, %s, %s, %s, %s)"(bill_no, customer_name, c_number, c_address, product_name, p_rate, p_qty))
            conn.commit()
            op2=input("Do You want to enter another Entry Yes/No?")
    elif op==2:
        cur.exceute("select bill_no, customer_name, c_number, c_address, product_name, p_rate, p_qty, p_qty*p_rate from Product_database")
        for row in cur:
            for value in row:
                print(value, end="\t")
            print(" ")
    elif op==3:
            print("You have been Exited..!!")
    else:
            print("WRONG OPTION SELECTED")
cur.close()
conn.close()