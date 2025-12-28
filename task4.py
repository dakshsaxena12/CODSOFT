import random

def choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def play(us, co):
    user = input("Enter your choice: ").lower()
    comp = choice()

    if ((user=="rock" and comp=="paper") or
        (user=="paper" and comp=="scissors") or
        (user=="scissors" and comp=="rock")):
        
        print("Computer chose:", comp)
        print("You lose!")
        co += 1

    elif ((user=="rock" and comp=="scissors") or
          (user=="paper" and comp=="rock") or
          (user=="scissors" and comp=="paper")):
        
        print("Computer chose:", comp)
        print("You win!")
        us += 1

    elif user == comp:
        print("Computer chose:", comp)
        print("It's a tie!")

    else:
        print("Invalid choice!")
        return play(us, co)

    print("Current Score:")
    print(f"User: {us} | Computer: {co}")

    again = input("Want to play again? (y/n): ").lower()
    if again == "y":
        return play(us, co)
    elif again == "n":
        if us > co:
            print("Congratulations! You lead the series.")
        elif us < co:
            print("Computer leads! Better luck next time.")
        else:
            print("A tie is not bad after all!")
        print("Have a great day! Goodbye.")
    else:
        print("Invalid choice! Game terminated.")

print("Welcome to Rock Paper Scissors Game!")
us = 0
co = 0
play(us, co)

