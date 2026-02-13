def checkifsamenumber(number1, number2):
    if((number1 ^ number2)!=0):
        print("The numbers are not equal")
    else:
        print("the numbers are not equal")
number1=int(input("enter the first number"))
number2=int(input("enter the second number"))
checkifsamenumber(number1, number2)