import random

userdict = {"rock": 1,"scissors": -1, "paper": 0}
revuserdict = {1: "rock", -1: "scissors", 0: "paper"}

while True:
    user_input = input("Enter your choice (rock, paper, scissors or 'exit' to quit): ").lower()
    if user_input == "exit":
        print("Game over. Thanks for playing!")
        break
    if user_input not in userdict:
        print("Invalid input! Please enter rock, paper, scissors, or 'exit'.")
        continue
    usernum = userdict[user_input]
    computer = random.choice([-1, 0, 1])
    print(f"You chose: {revuserdict[usernum]}")
    print(f"Computer chose: {revuserdict[computer]}")
    if computer == usernum:
        print("It's a draw!\n")
    elif (usernum == 1 and computer == -1) or \
         (usernum == 0 and computer == 1) or \
         (usernum == -1 and computer == 0):
        print("You won!\n")
    else:
        print("You lose!\n")
