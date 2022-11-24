# With this project I am making a game of Rock, Paper, Scissors!

import random 
"""
Importing 'random' library that let's us generate
pseudo-random numbers. This will be useful when generating the
randomized counter for user input
"""

while True: 
    """
    Wrapping the code inside a while loop so the program
    could be ran more than once
    """
    
    # Next I am going to make a list of choices
    game_choice = ["rock", "paper", "scissors"]
    user_input = input("Rock, paper or scissors: ").lower() 

    """
    I am storing
    the users choice into 'user_input'. I am also using the '.lower()'
    function to automatically set the user input into lowercase in the case
    where the user might capitalise any of the letters and break the
    program.
    """

    computer_input = random.choice(game_choice) 

    """
    This is where the
    'random' library comes into play. It will randomly choose one option
    from the list 'game_choice' and stores it into the variable
    'computer_input'
    Next I'm determining the logic behind the game and choosing the
    winner/loser
    """



    if user_input == computer_input:
        print(f"Both users chose {user_input}. It's a tie!")
    elif user_input == "rock":
        if computer_input == "scissors":
            print("Rock breaks scissors. You win!")
        else: 
            print("Paper covers Rock. You lose!")
    elif user_input == "paper":
        if computer_input == "rock":
            print("Paper covers rock. You Win!")
        else:
            print("Scissors cut paper. You lose!")
    elif user_input == "scissors":
        if computer_input == "paper":
            print("Scissors cut paper. You win!")
        else:
            print("Rock smashes scissors. You lose!")
        
        
    play_again = input("Play again? (Yes/No): ").lower() 
    if play_again != "yes":
        break;