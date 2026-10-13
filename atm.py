bal=5000
while True:
    print("Press 1 for Checking Bank Balance\nPress 2 for Depositing money\nPress 3 for Withdrawing money\nPress 4 to exit")
    a=int(input("Enter required service: "))
    if a not in [1,2,3,4]:
        print("Invalid")
        continue
    match a:
        case 1:
            print(f"Your account balance is {bal}")
        case 2:
            b=int(input("Enter deposit amount: "))
            if b<=0:
                print("Invalid")
                continue
            else:
                bal+=b
                print(f"Your current balance is {bal}")
        case 3:
            c=int(input("Enter withdrawal amount: "))
            if c<=0 or c>b:
                print("Sorry can't withdraw this amount!")
            else:
                bal-=c
                print(f"You have withdrawn: {c}")
        case 4:
            print("Thank you for using our banking services!")
            break