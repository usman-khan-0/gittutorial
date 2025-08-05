import random

game = ["Rock", "Paper", "Scissors"]
comp = random.choice(game)

user = input("Enter your choice (Rock, Paper, Scissors): ")

print(f"Computer chose: {comp}")
print(f"You chose: {user}")

if user == comp:
    print("Its a Draw")
elif (user == "Rock" and comp == "Scissors"):
    print("You Win! Rock beats Scissors")
elif (user == "Paper" and comp == "Rock"):
    print("You Win! Paper beats Rock")
elif (user == "Scissors" and comp == "Paper"):
    print("You Win! Scissors beats Paper")
else:
    print(f"You Lose! {comp} beats {user}")