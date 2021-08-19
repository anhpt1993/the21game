# the 21 game
import random

def input_data():
    while True:
        try:
            num = int(input("Enter an integer in range (1,3): "))
            if 1 <= num <= 3:
                return num
                break
            else:
                print("Out of range (1,3), try again please")
                print()
        except ValueError:
            print("Enter an integer, not float or string")
            print()

def play_again():
    answer = input("Do you want to play again?(Y/N): ").upper()
    if answer == "Y" or answer == "YES":
        return True

if __name__ == '__main__':
    while True:
        current_number = 0
        human = []
        computer = []
        if random.randint(0,1) == 0:
            current_player = "human"
            print("Human, first")
            print()
        else:
            current_player = "computer"
            print("Computer, first")
            print()

        while True:
            #print("SUM: {}".format(current_number))
            print()

            if current_player == "human":
                print("HUMAN TURN")
                player_choice = input_data()
                print("You choose {}".format(player_choice))
                human.append(player_choice)
                current_number += player_choice

                if current_number >= 21:
                    print()
                    print("Your choice: ")
                    print(human)
                    print("Computer's choice: ")
                    print(computer)
                    print()
                    print("THE CURENT NUMBER IS {}".format(current_number))
                    print("You lose!!! Better luck next time")
                    print()
                    break
                else:
                    current_player = "computer"
            else:
                print("COMPUTER TURN")
                computer_choice = random.randint(1, 3)
                print("Computer chooses {}".format(computer_choice))
                computer.append(computer_choice)
                current_number += computer_choice

                if current_number >= 21:
                    print()
                    print("Computer's choice: ")
                    print(computer)
                    print("Your choice: ")
                    print(human)
                    print()
                    print("THE CURRENT NUMBER IS {}".format(current_number))
                    print("You won!!! Congratulations")
                    print()
                    break
                else:
                    current_player = "human"

        if play_again() != True:
            print("Bye, see you later!")
            break