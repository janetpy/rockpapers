import random

i = ["rock", "paper", "siccors"]


ans = "y"

while ans == "y":
    comp = random.choice(i)
    player = input("Choose between rock, paper and siccors")
    if player == comp:
        print("Tie!!")
    elif player == "siccors":
        if comp == "paper":
            print("player wins")
        else:
            print("Computer wins")
    elif player == "rock":
        if comp == "siccors":
            print("player wins")
        else:
            print("Computer wins")
    elif player == "paper":
        if comp == "rock":
            print("player wins")
        else:
            print("Computer wins")

    ans = input("Do you wish to go again. Input 'y' for yes")

print("game over")
