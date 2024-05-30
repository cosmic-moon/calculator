while True:
    a = int(input("Enter the first number you want to operate with:"))
    b = int(input("Enter the second number you want to operate with:"))
    c = input("Enter the operation you want to perform, (+,-,*,):")
    if c == "+":
        print(f"Your result is {add(a,b)}")
    elif c == "-":
        print(f"Your result is {a-b}")
    elif c == "*":
        print(f"Your result is {a*b}")
    elif c == "/":
        print(f"Your result is {a/b}")
    else :
        print("Please enter as suggested in up")


        def add(x,y):
            return x+y
        





        
        print(add(3,8))
            