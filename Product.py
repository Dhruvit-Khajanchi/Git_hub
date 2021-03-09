class product:
    name = ""
    rate = 0
    quantity = 0
class customer:
    bill_no = 0
    customer = ""
    mobile_no = 0
    product_list = []
customer_list = []
head = ["Bill No.", "Name", "Contact No.", "Description", "Quantity", "Rate", "Total"]
p = "yes"
while p=="yes":
    c1 = customer()
    c1.bill_no = int(input("Enter Bill No.: "))
    c1.customer = input("Enter Name: ")
    c1.mobile_no = int(input("Enter Contact no.: "))
    customer_list.append(c1)
    p2="yes"
    while p2=="yes":
        p1 = product()
        p1.name = input("Enter Product Name: ")
        p1.quantity = int(input("Enter Quantity: "))
        p1.rate = int(input("Enter rate: "))
        c1.product_list.append(p1)
        p2= input("do you want to enter another item (yes/no): ")

    print("Bill No.: ", c1.bill_no)
    print("Name: ", c1.customer)
    print("Contact No.: ", c1.mobile_no)
    total = 0
    for p1 in c1.product_list:
        print("Description: ", p1.name)
        print("Quantity: ", p1.quantity)
        print("Rate: ", p1.rate)
        price = p1.rate*p1.quantity
        print("Price: ", price)
        total = total+price
    print("Total = ", total)
    p = input("Do you want to make another bill (Yes/No): ")