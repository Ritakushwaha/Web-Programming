def check_num():
    number = int(input("Enter a Number : "))
    if number>0:
        print("Number is positive")
    elif number<0:
        print("Number is negative")
    else:
        print("Number is Zero")

while(True):
    check_num()
