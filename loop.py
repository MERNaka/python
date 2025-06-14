no = int(input("enter no : "))
if no%2 == 0:
    print(f"{no} is even")
else:
    print(f"{no} is odd")
    
limit = int(input("enter no : "))
for n in range(1,limit + 1):
    print(n)

attempt = 0
correct_password = "python123"
while attempt < 3:
    password = input("Enter the password : ")
    if password == correct_password:
        break
    else:
        attempt+=1
else:
    print("more attempts")
    exit()
    
        

