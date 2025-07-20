a=float(input("Enter First Number"))
b=float(input("Enter Second Number"))
operation=int(input("Press Number associated to Operation\n1. Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"))
match operation:
        case 1:
            print("Addition of {} and {} is {}".format(a,b,a+b))
        case 2:
            print("Subtraction of {} and {} is {}".format(a,b,a-b))
        case 3:
            print("Multiplication of {} and {} is {}".format(a,b,a*b))
        case 4:
            print("Division of {} and {} is {}".format(a,b,a/b))
        case _:
            print("Choose Correct Option\n Choose in 1 to 4")

    
