year = int(input("Enter Any Year: "))

if year % 4 == 0 is True:
    if year % 100 == 0 is True:
       if year % 400 == 0 is True:
        print("It is a Leap Year..!!")

    else:
        print("It's Not a Leap Year..!!")