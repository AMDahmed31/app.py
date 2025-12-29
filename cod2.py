import random
from rich import print

TrueNumber = random.randint(1,100)
Attempts = 10
while Attempts >=0 :
    if Attempts == 0 :

        print("The Game Over! ")
        print(f"The Attempts finshed!\nThe Attempts = {Attempts}")
        print("you want to replay The game?")
        FinshAttempts = input("Enter Yes or No :")
        if FinshAttempts == "Yes" or FinshAttempts == "yes":
            Attempts = 10
            TrueNumber= random.randint(1,100)
        elif FinshAttempts == "No" or FinshAttempts == "no":
            break
        else:
            print("Error")
            break
    print("[bold #161E54 on #F16D34]__Guess the correct number__[/]")
    print("Guess number (1 - 100)")
    Guess = input("Enter correct number : ")
    if Guess != str:
        print("[bold red]Error[/]\n[bold #161E54]write number [/]")
        while Guess != int:
            Guess = input("Enter correct number : ")
            if Guess == int:
                break
    Guess = int(Guess)
    if Guess > TrueNumber :
        Attempts -=1
        print("[bold red]No.[/] Choose a smaller number! '(-)'")
        print(f"The number of attempts is {Attempts}")
        print("-"*50)
        print("\n")
    elif Guess < TrueNumber :
        Attempts -=1
        print("No. Choose a larger number! '(+)'")
        print(f"The number of attempts is {Attempts}")
        print("-"*50)
        print("\n")
    elif Guess == TrueNumber :
        print("you win! \nYour guess is correct.")
        print(f"The number of attempts is {Attempts}")
        print("Do you want to replay the game?")
        print("-"*50)
        print("\n")
        Return = input("Choose Yes or No :")
        if Return == "Yes" or Return == "yes":
            Attempts = 10
            pass
        elif Return == "No" or Return == "no":
            break
        else:
            print("Error")
    else:
        print("Error")
