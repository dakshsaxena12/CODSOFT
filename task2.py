def calculate():
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    print("""Choose operation to perform (enter number): 
    1. Addition
    2. Subtraction 
    3. Multiplication 
    4. Division
    5. Floor Division 
    6. Exponential 
    7. Remainder""")
    op=int(input())
    match op:
        case 1:
            print(f"Sum of {num1} and {num2}: {num1+num2}")
        case 2:
            print(f"Difference of {num1} and {num2}: {num1-num2}")
        case 3:
            print(f"Product of {num1} and {num2}: {num1*num2}")
        case 4:
            print(f"Division of {num1} and {num2}: {num1/num2}")
        case 5:
            print(f"Floor Division of {num1} and {num2}: {num1//num2}")
        case 6:
            print(f"Exponential of {num1} and {num2}: {num1**num2}")
        case 7:
            print(f"Remainder of {num1} and {num2}: {num1%num2}")
        case _:
            print("Invalid choice!")
    choice=input("Want to calculate again? Type(y/n): ").lower()
    if(choice=='y'):
        return calculate()
    else:
        return
calculate()
print("Have a goood day!")
