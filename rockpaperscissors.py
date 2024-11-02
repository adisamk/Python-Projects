import random

choices = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(choices)

    while player not in choices:
        player = input("Choose: (rock, paper, scissors:): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose")
     
    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")