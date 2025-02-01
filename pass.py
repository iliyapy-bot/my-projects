import random 
import string

chars = string.ascii_letters + string.punctuation + string.digits

chars = list(chars)

key = chars.copy()

random.shuffle(key)


input1 = input("enter your words : ")
idk = ""

for letter in input1 :
    index = chars.index(letter) 
    idk += key[index]


print(idk)

input2 = input("recive the message : ")

idk2 = ""


for letter2 in input2 :
    index2 = key.index(letter2)
    idk2 += chars[index2]

print(idk2)