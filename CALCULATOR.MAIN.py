# this is a calculator programme
print('This is a calculator and the following operations can be done with just 2 numbers\nADDITION\nSUBTRACTION'
      '\nDIVISION\nMULTIPLICATION')
try:
    operation = int(input('Which operation would you like to carry out from the above'
                          ',\n Enter 1 for addition 2 for subtraction and so on: '))
    print('enter the two numbers and separate by a space')
    Num1, Num2 = input('Enter the first and second number: ').split()


    def add(x, y):
        """function to help add the two numbers given"""
        return x + y
    R1 = add((int(Num1)), (int(Num2)))


    def subtract(x, y):
        """function to help subtract the two numbers given"""
        return x - y
    R2 = subtract((int(Num1)), (int(Num2)))


    def multiply(x, y):
        """function to help Multiply the two numbers given"""
        return  x * y
    R3 = multiply((int(Num1)), (int(Num2)))


    def divide(x , y):
        """function to help divide the two numbers given"""
        return x / y
    R4 = divide((int(Num1)), (int(Num2)))


    if operation == 1:
        print(R1)
    elif operation == 2:
        print(R2)
    elif operation == 3:
        print(R3)
    elif operation == 4:
        print(R4)
except Exception:
    print("invalid information entered")