import math

def showMenu():
    print("\n1.Add")
    print("2.Substract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Trignometric Operations")
    print("6.Exit")
    return int(input("Your Choice -->"))

def line():
    print("------------------------------>")

    

def add():
    line()
    print("\nADDITION\nEnter two numbers :",end='')
    a = int(input())
    b = int(input())
    print(a,"+",b,"=",a+b)
    line()

def subs():
    line()
    print("\nSUBSTRACTION\nEnter two numbers :",end='')
    a = int(input())
    b = int(input())
    print(a,"-",b,"=",a-b)
    line()

def multiply():
    line()
    print("\nMULTIPLY\nEnter two numbers :",end='')
    a = int(input())
    b = int(input())
    print(a,"*",b,"=",a*b)
    line()

def divide():
    line()
    print("\nDIVISION\nEnter two numbers :",end='')
    a = int(input())
    b = int(input())
    print(a,"/",b,"=",a/b)
    line()

def trigno():
    line()
    print("\nTRIGNOMETRIC")
    print("1.sin")
    print("2.cos")
    print("3.cesec")
    print("4.sec")
    print("5.tan")
    print("6.cot")
    ch = int(input("Your Choice -->"))
    if ch == 1:
        angle = float(input("Enter angle(in degrees) : "))
        angleRad = math.radians(angle) 
        print("sin(",angle,") = ",math.sin(angleRad),sep='')
        line()
    if ch == 2:
        angle = float(input("Enter angle(in degrees) : "))
        angleRad = math.radians(angle) 
        print("cos(",angle,") = ",math.cos(angleRad),sep='')
        line()
    if ch == 3:
        angle = float(input("Enter angle(in degrees) : "))
        angleRad = math.radians(angle) 
        print("cosec(",angle,") = ",1/math.sin(angleRad),sep='')
        line()
    if ch == 4:
        angle = float(input("Enter angle(in degrees) : "))
        angleRad = math.radians(angle) 
        print("sec(",angle,") = ",1/math.cos(angleRad),sep='')
        line()
    if ch == 5:
        angle = float(input("Enter angle(in degrees) : "))
        angleRad = math.radians(angle) 
        print("tan(",angle,") = ",math.tan(angleRad),sep='')
        line()
    if ch == 6:
        angle = float(input("Enter angle(in degrees) : "))
        angleRad = math.radians(angle) 
        print("cot(",angle,") = ",1/math.tan(angleRad),sep='')
        line()

print("\n__________________________START___________________________")
ch = showMenu()
while(ch != 6):
    if ch == 1: 
        add()
        ch = showMenu()
    elif ch == 2: 
        subs()
        ch = showMenu()
    elif ch == 3:
        multiply()
        ch = showMenu()
    elif ch == 4:
        divide()
        ch = showMenu()
    elif ch == 5:
        trigno()
        ch = showMenu()
print("\n_____________x_____________END_____________x____________")