fname=input("Enter your first name")
lname=input("Enter your last name")

if fname=="" or lname=="":
    print("please enter both first and last name.")  
else:
    name=fname+" "+lname
    print(f"Hello, {name}! Welcome to the Python program.")