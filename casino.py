import random




def spin_row() :
    Symbols = ['⭐' ,'🍪' ,'💥' ,'🍇' ,'🍍' ,'🐧' ]
    return [random.choice(Symbols) for _ in range(3)]
    

def print_row(row) :
    print(" | ".join(row))

def payout(bet , row ) :
    if row[0] == row[1] == row[2] :
        if row[0] == '⭐' :
            return bet ** 5
        elif row[0] == '💥' :
            return bet ** 3 
        elif row[0] == '🍪' :
            return bet ** 2
        elif row[0] == '🍍' :
            return bet ** 4
        elif row[0] == '🐧' :
            return bet ** 3
        elif row[0] == '🍇' :
            return bet ** 2
    return 0




def main():
    Balance = 200
    print("-------------------------------")
    print("            Welcome            \n")
    print(" Symbols : ⭐ , 🍪 , 💥 ")
    print("-------------------------------")
    print(f"your Balance : {Balance}")
    

    while Balance > 0 :
        bet = input("place your bet :")
        if not bet.isdigit() :
            print("pls Type a number ")
            continue
        bet = int(bet)
        if bet > Balance :
            print("low budget ..")
            continue
        if bet <= 0 :
            print("Wrong ..")
            continue    
        
        Balance -= bet 
        print(Balance)
        row = spin_row()
        print("spining..")
        print_row(row)

        pay = payout(bet , row)

        if pay > 0 :
            print(f"You Won : ${pay}")
        else :
            print("lost")

        Balance += pay
        print(f"${Balance}")
        while True :

            play_again = input("play again : (Y/N) :").upper()

            if play_again.isdigit():
                continue
            elif play_again == "Y":
                x = True
                break
            else :
                x = False
                break

        if x == True :
            continue
        else :
            break



if __name__ == '__main__' :
    main()