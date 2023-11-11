import random

# Define the list of choices outside of the loop
choices = ["stone", "paper", "scissors"]

while True:  # Create a loop to play multiple rounds
    l1 = random.choice(choices)
    ucount = 0
    ccount = 0
    
    print("                                                       Can you play this game?")
    print("                                                            1. Yes / 2. No")
    n1 = int(input("                                                                "))
    
    if n1 == 1:
        for i in range(1, 6):
            print('''1. Stone
2. Paper
3. Scissors''')
            n2 = int(input("Enter your choice (1/2/3): "))
            print('')
            if n2 not in [1, 2, 3]:
                print("Invalid input. Please choose 1, 2, or 3.")
                continue
            
            # Map user's choice to the corresponding string
            user_choice = choices[n2 - 1]
            
            print(f"Your choice: {user_choice}")
            print(f"Computer's choice: {l1}")
            
            if user_choice == l1:
                print("It's a draw!")
                ucount +=1
                ccount +=1
            elif user_choice == "stone" and l1 == "scissors" or \
            user_choice == "paper" and l1 == "stone" or \
            user_choice == "scissors" and l1 == "paper":
                print("You win!")
                ucount +=1
            else:
                print("Computer wins!")
                ccount +=1
        if ucount == ccount :
            print("                                                 this match is draw ......")            
            print(f"                                                your total win number {ucount} ")
            print(f"                                                computer total win number {ccount} ")
            print('')
        elif ucount > ccount :
            print("                                                 fanly you win ......")            
            print(f"                                                your total win number {ucount} ")
            print(f"                                                computer total win number {ccount} ")
            print('')
        else:
            print("                                                  this match is computer win ......")            
            print(f"                                                 your total win number {ucount} ")
            print(f"                                                 computer total win number {ccount} ")
            print('')
    elif n1 == 2:
        break  # Exit the game if the user chooses 'No'
    
    else:
        print("Invalid input. Please choose 1 or 2.")
