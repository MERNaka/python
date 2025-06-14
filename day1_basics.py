# Ask for name and favorite language
# Print: "Hello <name>, you love <language>"
"""
printName = str(input("Enter your Name : "))
printLanguage = str(input("Enter your Language : "))
print(f"Hello {printName}, you love {printLanguage}")
"""

# Ask for 2 numbers and an operator (+, -, *, /)
# Perform and print the result
# """
no1 = int(input("Enter No1 : "))
no2 = int(input("Enter No2 : "))
operator = input("Enter Operator : ")
# print(printNo1 + printOperator + printNo2)
if(operator == '+'):
    print(no1 + no2)
elif(operator == '-'):
    print(no1 - no2)
elif(operator == '*'):
    print(no1 * no2)
elif(operator == '/'):
    print(no1 / no2)
else:
    print("inavlid operator")

# """

# Input: radius
# Output: area = π * r^2 (use 3.14)

"""
radius = int(input("Enter radius : "))
pi = 3.14
print(pi * radius * radius)

"""
