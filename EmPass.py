
import random
import string

Chars = string.ascii_letters + string.digits
BChars = string.ascii_uppercase
SChars = string.ascii_lowercase
#--Email----------------------------------------
def Email():
    mail = ""
    class email:
        def __init__(self, main, type):
            self.main = main 
            self.type = type
        def Show(self):
            return (f"{self.main}@{self.type}")
            
    class gmail(email) :
        def __init__(self, main, type):
            super().__init__(main, type)
            
    class yahoo(email) :
        def __init__(self, main, type):
            super().__init__(main, type)
            
    class outlook(email) :
        def __init__(self, main, type):
            super().__init__(main, type)
            self.type = type
#--Random------------------------------------------
    UserLEN = int(input("Enter your Lenght: "))
    for l in range(1 , UserLEN+1):
        mail += random.choice(Chars)

        if mail[0].isdigit():
               mail = ""
               for m in range(1 , UserLEN+1):
                    mail += random.choice(Chars)
#--Type-----------------------------------------------
    Gmail = gmail(mail, "gmail.com")
    Yahoo = yahoo(mail, "yahoo.com")
    Outlook = outlook(mail, "outlook.com")
#--User-----------------------------------------------   
    while True :
        UserEM= input("Do you want : (1)= gmail , (2)= yahoo , (3)= outlook:")
        if UserEM == "1" :
            Gmail.Show()
            print("your Email. copy it!!")
            break
        elif UserEM == "2":
            Yahoo.Show()
            print("your Email. copy it!!")
            break
        elif UserEM == "3":
            Outlook.Show()
            print("your Email. copy it!!")
            break
        else :
            print("Wrong!!")
#--PassSelection-----------------------------------------------
    UserD = input("Do you want Password?(Y|N)").upper()

    if UserD == "Y":
        Pass()
    elif UserD == "N":
        pass
#--------------------------------------------------
def Pass():
    print("Password Generator")
    Password = ""
    UserPen = int(input("Enter your Pass lenght: "))
    UserUp = input("Password start with Uppercase Characters?(Y|N): ").upper()
    
    for z in range(1 , UserPen+1):
        Password += random.choice(Chars)
    if UserUp == "Y":
        Password = ""
        Password += random.choice(BChars)
        for i in range(1 , UserPen):
            Password += random.choice(Chars)
    elif UserUp == "N":
        Password = ""
        Password += random.choice(SChars)
        for i in range(1 , UserPen):
            Password += random.choice(Chars)

    print("your Password. copy it!!")
    print(Password) 


def main():
    print(Chars)
    print("Welcome")
    print("-----------")
    print("if you want random Email : (1)")
    print("if you want random Password : (2)")
    
    while True:
        User = input("1 or 2: ")
        if not User.isdigit() :
            print("Please Type a Number")
        elif not User == "2" and not User == "1" :
            print("Please Choose From 1 or 2")
        elif User == "1" :
            Email()
            break
        elif User == "2" :
            Pass()
            break

            
if __name__ == '__main__' :
    main()