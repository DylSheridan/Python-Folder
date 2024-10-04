# Assignment 1: Rock-Paper-Scissors
# PROG10004
# Dylan Ponrajah

#Imports
import random

#User Interface and Rules 
print("================== ROCK PAPER SCISSORS ==================\n")
print("Welcome to Rock Paper Scissors!\n")
print("Rules:\nScissors beat paper, paper beats rock, rock beats scissors.\n")

#While Loop
loop = True
while loop:

    #Asking the user how many rounds must be won in order to win the match
    rounds = int(input("How many rounds must a player win to win the match?"))

    #ScoreCounters
    scoreCounterPlayer = 0
    scoreCounterComputer = 0

    #Start of game
    if rounds >=1:
        print("Sounds great! Let's play...\n")
    
        for counter in range(rounds):#Start of for loop
        
            #Player move
            playerChoice = str(input("Choose Rock (R), Paper (P), or Scissors (S): ")).lower()
       
            #Computer move
            moves = ("Rock", "Paper", "Scissors")
            computerChoice = str(random.choice(moves)).lower()    
            if playerChoice == "r" or playerChoice == "p" or playerChoice == "s" or playerChoice == "rock" or playerChoice == "paper" or playerChoice == "scissors":
                print("Computer: " + computerChoice)

            #Player win outcomes
            if (playerChoice == "r" or playerChoice == "rock")  and computerChoice == "scissors":
                scoreCounterPlayer += 1
                print("You win!" + " Score now: " + str(scoreCounterPlayer) + ":" + str(scoreCounterComputer) + "\n")

            elif (playerChoice == "p" or playerChoice == "paper") and computerChoice == "rock":
                scoreCounterPlayer += 1
                print("You win!" + " Score now: " + str(scoreCounterPlayer) + ":" + str(scoreCounterComputer) + "\n")

            elif (playerChoice == "s" or playerChoice == "scissors") and computerChoice == "paper":
                scoreCounterPlayer += 1
                print("You win!" + " Score now: " + str(scoreCounterPlayer) + ":" + str(scoreCounterComputer) + "\n")

            #Computer win outcomes
            elif computerChoice == "rock" and (playerChoice == "s" or playerChoice == "scissors"):
                scoreCounterComputer += 1
                print("I win!" + " Score now: " + str(scoreCounterPlayer) + ":" + str(scoreCounterComputer) + "\n")

            elif computerChoice == "paper" and (playerChoice == "r" or playerChoice == "rock"):
                scoreCounterComputer += 1
                print("I win!" + " Score now: " + str(scoreCounterPlayer) + ":" + str(scoreCounterComputer) + "\n")

            elif computerChoice == "scissors" and (playerChoice == "p" or playerChoice == "paper"):
                scoreCounterComputer += 1
                print("I win!" + " Score now: " + str(scoreCounterPlayer) + ":" + str(scoreCounterComputer) + "\n")
            
            #Invalid Input
            elif playerChoice != "r" and playerChoice != "p" and playerChoice != "s":
                print("Not sure what you mean. Try again...\n")
            
            #Tie outcome  
            else: 
                print("Tie! Try again...\n")

    #Match scenarios 
    if scoreCounterPlayer > scoreCounterComputer:
        userChoice = input("You win the match! Do you want to play another match?(Y/N) ").lower()

    elif scoreCounterPlayer < scoreCounterComputer:
        userChoice = input("I win the match! Do you want to play another match?(Y/N) ").lower()

    else:
        userChoice = input("It's a tie! Do you want to play another match?(Y/N) ").lower()

    #If the user does wish to continue
    if userChoice == "y":
        loop = True

    #If the user does not wish to continue    
    else: 
        loop = False
        print("\nThanks for playing! Bye for now!")
        

