"""
💡 Task 1: Create a Calculator Using Functions
Separate functions for add, subtract, multiply, divide

Call them based on user input

💡 Task 2: Number Checker
Function is_even(num) → returns True or False

Use it in a loop from 1 to 10

💡 Task 3: Multiplication Table Generator
Function print_table(n) → prints table of n up to 10
"""

def add(no1, no2):
    print(no1 + no2)
def sub(no1, no2):
    print(no1 - no2)
def mul(no1, no2):
    print(no1 * no2)
def div(no1, no2):
    try:
        print(no1 / no2)
    except ZeroDivisionError:
        print("cant divide zero")

def calculator():
    no1 = int(input("Enter no1 : "))
    no2 = int(input("Enter no2 : "))
    operator = input("Enter operator : ")  
    if(operator == '+'):
        add(no1,no2)
    elif(operator == '-'):
        sub(no1,no2)
    elif(operator == '*'):
        mul(no1,no2)
    elif(operator == '/'):
        div(no1,no2)
    else:
        return "Invalid operator"
        
calculator()




def is_even(i):
    return i % 2 == 0  # Returns True or False

for i in range(1, 11):
    print(f"{i} is even: {is_even(i)}")

    print(is_even(i))


def multiplication(i,n):
    result = i*n
    return f"{i} * {n} = {result}"

n = int(input("Enter n : "))
for i in range(1,11):
    print(multiplication(i, n))