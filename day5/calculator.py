# calculator
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
num1=int(input("whats the first number "))
num2=int(input("whats the second number "))
for key in operations:
    print(key)
operation_sym=input("what operetion would you like to carry out?")
result=operations[operation_sym](num1,num2)
print(result)
conti=input("would you like to continue with previous calculation? 'y' or 'n'.")
while (conti=='y'):
    another_num=int(input("type another number "))
    operation=input("what operetion would you like to carry out? ")
    result=operations[operation](result,another_num)
    print(result)
    conti=input("would you like to continue with previous calculation? 'y' or 'n'. ")
    