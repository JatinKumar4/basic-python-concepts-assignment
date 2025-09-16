try:
    a=int(input("Enter the first number"))
    b=int(input("Enter the second number"))
    Addition=a+b
    Subtraction=a-b
    Multiplication=a*b
    
    try:
        Division=a/b
    except ZeroDivisionError:
        Division="Undefined(division by zero)"

    print("Addition",Addition)
    print("Subtraction:",Subtraction)
    print("Multiplication:",Multiplication)
    print("Division:",Division)

except ValueError:
    print("Invalid input! Please enter valid integers.")