def calculate(op,num1,num2):
    if op=='+':
        res=num1+num2
    elif op == '-':
        res=num1-num2
    elif op == '*':
        res=num1*num2
    elif op=='/':
        if num2!=0:
            res=num1/num2
        else:
            print("invalid division")
    elif op == '%':
        res=num1%num2
    else:
        print("invalid operator")
    return res

num1=float(input("enter the first operand: "))
num2=float(input("enter the second operand: "))
op=input('enter the operation to be performed: ')
print("result=",end="")
print(calculate(op,num1,num2))