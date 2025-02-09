import random
import string

Chars = string.ascii_lowercase + string.digits + string.ascii_uppercase
Chars2 = string.ascii_uppercase
Pass = ""

User = int(input("enter your chars number: "))
print("don't begin with a number : Y|N")
Yn1 = input("Y/N?: ").upper()
print("Begin with uppercase Char?")
Yn2 = input("Y/N?: ").upper()
for p in range(1 , User):
    Pass += random.choice(Chars)
           
if Yn1 == "Y":
    while Pass[0].isdigit() :
        Pass = ""
        for d in range(1 , User):
            Pass += random.choice(Chars)
if Yn2 == "Y":
        Pass = ""
        Pass += random.choice(Chars2)
        for c in range(1 , User):
            Pass += random.choice(Chars)


print(Pass)
