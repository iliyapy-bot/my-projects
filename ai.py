import random

def ai():
    def talk():
        hellolist = ["hi :)", "hello", "hey !!"]
        whatsuplist = ["im good","bad :(","im great"]
        answerlist = ["its good", "great", ";)"]
        _answerlist = ["why!!", "what happened?"]
        __answerlist = ["nothing waiting for you", "nothing"]
        goodbye = ["ok goodbye", "have a good day", "byeee :)"]

        while True:
            user_input = input("Talk with fxbot!! :").lower()

            if user_input == "hi" or user_input == "hello":
                print(random.choice(hellolist))
            elif user_input == "whatsup" or user_input == "how are you":
                print(random.choice(whatsuplist))
            elif user_input == "im good too" or user_input == "im great":
                print(random.choice(answerlist))
            elif user_input == "im not good" or user_input == "im sad":
                print(random.choice(_answerlist))
            elif user_input == "what were you doing":
                print(random.choice(__answerlist))
            elif user_input == "ok goodbye" or user_input == "goodbye" or user_input == "ok bye" or user_input == "bye":
                print(random.choice(goodbye))
            else:
                print("chimigi??")

    import random

    def minigame():
        print("OK, let's play!!!\n")
        print("It's a guessing number game!!!\n")
        print("One of us picks a number between 1 to 10, and the other must guess the number.\n")
        
        user_choice = input("Do you want to guess the number? (yes or no): ")

        if user_choice.lower() == "yes":
            random_number = random.choice(range(1, 11))
            print("I picked a number. Now it's your turn to guess!")

            guess_number = 0
            while True:
                guess = int(input("Your guess: "))
                guess_number += 1

                if guess == random_number:
                    print(f"Well done! You guessed it in {guess_number} attempts.")
                    break
                else:
                    print("Try again!")

        elif user_choice.lower() == "no":
            user_number = int(input("OK, pick a number between 1 to 10: "))
            print("I will try to guess your number!")

            guess_number = 0
            while True:
                computer_guess = random.choice(range(1, 11))
                guess_number += 1

                if computer_guess == user_number:
                    print(f"I guessed it! It took me {guess_number} attempts.")
                    break
                else:
                    print("Oops, wrong guess. I'll try again!")

        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

    def question():
        print("ask me a question and if i know that i answer\n")
        print("i know math\n")
        while True :
            question = (input("what do you want?"))
            if question.lower() == "math" :
                number1 = input("tell me your number :")
                operator = input(" * / + / (/) / -  :")
                number2 = int(input("tell me your number :"))
                if operator == "/" and number2 == "0" :
                    print("invalid !!")
                
            
                _answer = str(number1) + " " + operator + " " + str(number2)
                answer = eval(_answer)
                print(answer)


    print("hi :)\n")
    print("myname is fxbot and i simplest bot you ever see\n")
    print("if you want to talk to me press 1 and if you want to play minigame with me press 2  and if you want ask me a question press 3 and if want to quit press any button Except 1 and 2 and 3 \n")

    pickinput = input (" 1 or 2 or 3 :")

    while True :
        if pickinput == "1" :
            talk()
        elif pickinput == "2" :
            minigame()
        elif pickinput == "3" :
            question()
        else :
            print("exit")
            break
  


        


                
                

                
                    

                

            
            
            
        
            


    
    

ai()




