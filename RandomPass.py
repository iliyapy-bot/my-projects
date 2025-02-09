import random
import string

Chars = string.ascii_lowercase + string.digits

Chars2 = string.ascii_uppercase

Pass = ""

Pass +=(random.choice(Chars2))

User = int(input("enter your chars number: "))

for p in range(1 , User):
    Pass += random.choice(Chars)


print(Pass)
