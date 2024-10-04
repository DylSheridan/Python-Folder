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
       
            if playerChoice != "r" or playerChoice != "p" or playerChoice != "s":
                print("Not sure what you mean. Try again...\n")

            #Computer move
            moves = ("Rock", "Paper", "Scissors")
            computerChoice = str(random.choice(moves)).lower()
            print("Computer: " + computerChoice)

            #Winner

            #Player win Outcomes
            if playerChoice == "r" and computerChoice == "scissors":
                scoreCounterPlayer += 1
                print("You win!" + " Score now: " + str(scoreCounterPlayer) + ":" + str(scoreCounterComputer) + "\n")

            elif playerChoice == "p" and computerChoice == "rock":
                scoreCounterPlayer += 1
                print("You win!" + " Score now: " + str(scoreCounterPlayer) + ":" + str(scoreCounterComputer) + "\n")

            elif playerChoice == "s" and computerChoice == "paper":
                scoreCounterPlayer += 1
                print("You win!" + " Score now: " + str(scoreCounterPlayer) + ":" + str(scoreCounterComputer) + "\n")

            #Computer win outcomes
            elif computerChoice == "rock" and playerChoice == "s":
                scoreCounterComputer += 1
                print("I win!" + " Score now: " + str(scoreCounterPlayer) + ":" + str(scoreCounterComputer) + "\n")

            elif computerChoice == "paper" and playerChoice == "r":
                scoreCounterComputer += 1
                print("I win!" + " Score now: " + str(scoreCounterPlayer) + ":" + str(scoreCounterComputer) + "\n")

            elif computerChoice == "scissors" and playerChoice == "p":
                scoreCounterComputer += 1
                print("I win!" + " Score now: " + str(scoreCounterPlayer) + ":" + str(scoreCounterComputer) + "\n")
            #Tie outcome  
            else: 
                print("Tie! Try again...\n")

            #Invalid Input 

                #print("Not sure what you mean. Try again...")
        #End of for loop

    #Win scenarios 
    if scoreCounterPlayer > scoreCounterComputer:
        choice = input("You win the match! Do you want to play another match?(Y/N) ").lower()
    elif scoreCounterPlayer < scoreCounterComputer:
        choice = input("I win the match! Do you want to play another match?(Y/N) ").lower()
    else:
        choice = input("It's a tie! Do you want to play another match?(Y/N) ").lower()

    if choice == "y":
        loop = True
    else: 
        print("\nThanks for playing! Bye for now!")
        break

