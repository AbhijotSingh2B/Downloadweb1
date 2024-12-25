#Import adds tools

#Import time adds tools to control time
print("hello world\n")

import time
import sys
import random

last_edit_date = "24/12/24 DD/MM/YY"

#tests if modules are working and Corrects Text
print("imported module(s) time, sys, random    Variables Loaded   \033[1;32;40m Text Corrected  \033[0;37;40m Starting testing below: \n")

def test_sys():
    return sys.version, sys.version_info

def test_time():
    print("sleeping for 0.2 second")
    time.sleep(0.2)
    return "Import Working"

def test_random():
    random_num_test = random.randint(1, 10)
    return (f"random number (1 to 10): {random_num_test}")

#prints test results
print(test_time())
print(test_random())
print("\033[0;37;40mimported module(s) time and testing has been completed    \033[1;40;37m Starting code below: \n\n")

#Calls all tests
def testing_prog():
    print(test_time())
    print(test_random())
    print(test_sys())
    return "Testing Complete"

#exit / break code (used to stop code)
def exit_prog():
    print("Exit attempt detected, are you sure you want to do this? \n")
    exit_code = input("Type \"0\" here if you want to exit the program: ")
    if int(exit_code) == 0:
        print("\n\n ▄▄▄▄▄▄▄▄▄▄  ▄         ▄ ▄▄▄▄▄▄▄▄▄▄▄ ")
        print("▐░░░░░░░░░░▌▐░▌       ▐░▐░░░░░░░░░░░▌")
        print("▐░█▀▀▀▀▀▀▀█░▐░▌       ▐░▐░█▀▀▀▀▀▀▀▀▀ ")
        print("▐░▌       ▐░▐░▌       ▐░▐░▌          ")
        print("▐░█▄▄▄▄▄▄▄█░▐░█▄▄▄▄▄▄▄█░▐░█▄▄▄▄▄▄▄▄▄ ")
        print("▐░░░░░░░░░░▌▐░░░░░░░░░░░▐░░░░░░░░░░░▌")
        print("▐░█▀▀▀▀▀▀▀█░▌▀▀▀▀█░█▀▀▀▀▐░█▀▀▀▀▀▀▀▀▀ ")
        print("▐░▌       ▐░▌    ▐░▌    ▐░▌          ")
        print("▐░█▄▄▄▄▄▄▄█░▌    ▐░▌    ▐░█▄▄▄▄▄▄▄▄▄ ")
        print("▐░░░░░░░░░░▌     ▐░▌    ▐░░░░░░░░░░░▌")
        print(" ▀▀▀▀▀▀▀▀▀▀       ▀      ▀▀▀▀▀▀▀▀▀▀▀ ")
        print("\033[0;37;40m Exiting in 1 Second\n")
        print("\033[0;37;40m Exiting in 1 Second\n")
        print("\033[0;37;40m Exiting in 1 Second\n")
        sys.exit("System Exit executed\n")
        print("\033[0;37;40m Normal text\n")
        print("\033[1;31;40m Red")
        print("\033[1;40;37m inverted normal")
        print("\033[1;32;40m Bright Green") 
    else:
        print("System Execution Terminated")
        print("\033[0;37;40m Continuing Program\n")

#all the tools and help used
def credits_seq():
    time.sleep(0.2)
    print("\033[1;33;40m _______")
    print("/   |   \   Made By:")
    print("|__/|\__|         Abhijot Singh VIII A")
    print("|  \|/  |   Last Edited on:")
    print("|___|___|          " + last_edit_date +"\n")
    time.sleep(0.2)
    print("\033[0;40;40m___  ___          _       ______          ___  _     _     _ _       _     _____ _             _     ")
    print("|  \/  |         | |      | ___ \        / _ \| |   | |   (_(_)     | |   /  ___(_)           | |    ")
    print("| .  . | __ _  __| | ___  | |_/ /_   _  / /_\ | |__ | |__  _ _  ___ | |_  \ `--. _ _ __   __ _| |__  ")
    print("| |\/| |/ _` |/ _` |/ _ \ | ___ | | | | |  _  | '_ \| '_ \| | |/ _ \| __|  `--. | | '_ \ / _` | '_ \ ")
    print("| |  | | (_| | (_| |  __/ | |_/ | |_| | | | | | |_) | | | | | | (_) | |_  /\__/ | | | | | (_| | | | |")
    print("\_|  |_/\__,_|\__,_|\___| \____/ \__, | \_| |_|_.__/|_| |_|_| |\___/ \__| \____/|_|_| |_|\__, |_| |_|")
    print("                                  __/ |                    _/ |                           __/ |      ")
    print("                                 |___/                    |__/                           |___/       \n")
    time.sleep(0.2)
    print("\033[0;36;40m:::'###:::::'######:::'######::'####:'####::::")
    print("::'## ##:::'##... ##:'##... ##:. ##::. ##:::::")
    print(":'##:. ##:: ##:::..:: ##:::..::: ##::: ##:::::")
    print("'##:::. ##:. ######:: ##:::::::: ##::: ##:::::")
    print(" #########::..... ##: ##:::::::: ##::: ##:::::")
    print(" ##.... ##:'##::: ##: ##::: ##:: ##::: ##:::::")
    print(" ##:::: ##:. ######::. ######::'####:'####::::")
    print("..:::::..:::......::::......:::....::....:::::")
    print("╔═╗┬─┐┌┬┐  ╔╗ ┬ ┬  ╔═╗┬┌─┐┬  ┌─┐┌┬┐   ╦┌─┐  ┌┐ ┬ ┬  ┌─┐┌─┐┌┬┐┌─┐┬─┐ ┬┬┌─")
    print("╠═╣├┬┘ │   ╠╩╗└┬┘  ╠╣ ││ ┬│  ├┤  │    ║└─┐  ├┴┐└┬┘  ├─┘├─┤ │ │ │├┬┘ │├┴┐")
    print("╩ ╩┴└─ ┴   ╚═╝ ┴   ╚  ┴└─┘┴─┘└─┘ ┴   ╚╝└─┘  └─┘ ┴   ┴  ┴ ┴ ┴ └─┘┴└─└┘┴ ┴")
    print("| github.com/patorjk/figlet.js (ASCII Art) | kaggle.com/discussions/general/273188 (Text Colour) |  | [Many Resources are not mentioned here]\n\n")
#Starts Credits/Startup Sequence
credits_seq()

#Calculator Function
def calculator():
    #Get Input
    num1 = float(input("\nEnter 1st Number Here: "))
    num2 = float(input("Enter 2nd Number Here: "))
    operatorin = input("Enter The Operator Here (add, +, plus, multiply, x, *, div, /, division, minus, -, subtract, sqr (Square), Cube etc.): ").lower()

    #Simplify the input
    operator_dictionary = {
            "+": "+", "add": "+", "plus": "+",
            "-": "-", "sub": "-", "minus": "-",
            "x": "*", "*": "*", "multiply": "*", "/": "/",
            "/": "/", "div": "/", "sqr": "x2", "\\": "/",
            "division": "/", "addition": "+", "subtraction": "-",
            "multiplication": "*", "addition": "+", "cube": "x3",
            "square": "x2", "divide": "/", "mul": "*", "**": "x2", "***": "x3", 
        }
    operator = operator_dictionary.get(operatorin, "invalid")

    #Calculation and Categorization
    if operator != "invalid":
        if operator == "+":
            calculated_num = num1 + num2
        elif operator == "-":
            calculated_num = num1 - num2
        elif operator == "/":
            calculated_num = num1 / num2
        elif operator == "*":
            calculated_num = num1 * num2
        elif operator == "x2":
            calculated_num = num1 * num1
        elif operator == "x3":
            calculated_num = num1*num1*num1
    else:
        print("Invalid Operator")
    print("\nThe Answer is: " + str(calculated_num) + "\n")

#Rock Paper Scissors Function
def rock_paper_scissors():
    #Deciding moves
    player_movein = input("What Move do you want to play? (Rock, R, Scissors, S, Paper, P): ").lower()
    robot_movein = random.randint(1,3)

    #Simplification
    rb_move_dictionary = {
        1: "r", 2: "p", 3: "s" 
        }

    pl_move_dictionary = {
        "rock": "r", "paper": "p", "scissors": "s", "scissor": "s",
        "s": "s", "r": "r", "p": "p"
        }

    player_move = pl_move_dictionary.get(player_movein, "invalid")
    robot_move = rb_move_dictionary.get(robot_movein, "invalid")

    #Design improve
    reverse_move_dictionary = {
        "s": "Scissors","r": "Rock","p": "Paper",
    }

    reverse_player_move = reverse_move_dictionary.get(player_move)
    reverse_robot_move = reverse_move_dictionary.get(robot_move)

    #Calculation
    if player_move != "invalid":
        if player_move == robot_move:
            print(f"\n\033[1;32;40mIt is a Tie! | Player: {reverse_player_move} Robot: {reverse_robot_move}")
        elif player_move == "r":
            if robot_move == "p":
                print(f"\nYou Lost.... | Player: {reverse_player_move} Robot: {reverse_robot_move}")
            else:
                print(f"\nYou Won! | Player: {reverse_player_move} Robot: {reverse_robot_move}")
        elif player_move == "p":
            if robot_move == "s":
                print(f"\nYou Lost.... | Player: {reverse_player_move} Robot: {reverse_robot_move}")
            else:
                print(f"\nYou Won! | Player: {reverse_player_move} Robot: {reverse_robot_move}")
        elif player_move == "s":
            if robot_move == "r":
                print(f"\nYou Lost.... | Player: {reverse_player_move} Robot: {reverse_robot_move}")
            else:
                print(f"\nYou Won! | Player: {reverse_player_move} Robot: {reverse_robot_move}")

    else:
        print(f"Your Move is Invalid! | {player_move} | {player_movein}")

#Easter Egg
def easter_egg1():
    print("Time for a Quiz!")
    ans1 = input("Who was in the OYO Hotel With Kartik?: ").lower()

    if ans1 == "kavya":
        print("Correct!")
        time.sleep(0.2)
        print("██╗  ██╗ █████╗ ██████╗ ████████╗██╗██╗  ██╗    ███╗   ██╗    ██╗  ██╗ █████╗ ██╗   ██╗██╗   ██╗ █████╗ ")
        print("██║ ██╔╝██╔══██╗██╔══██╗╚══██╔══╝██║██║ ██╔╝    ████╗  ██║    ██║ ██╔╝██╔══██╗██║   ██║╚██╗ ██╔╝██╔══██╗")
        print("█████╔╝ ███████║██████╔╝   ██║   ██║█████╔╝     ██╔██╗ ██║    █████╔╝ ███████║██║   ██║ ╚████╔╝ ███████║")
        print("██╔═██╗ ██╔══██║██╔══██╗   ██║   ██║██╔═██╗     ██║╚██╗██║    ██╔═██╗ ██╔══██║╚██╗ ██╔╝  ╚██╔╝  ██╔══██║")
        print("██║  ██╗██║  ██║██║  ██║   ██║   ██║██║  ██╗    ██║ ╚████║    ██║  ██╗██║  ██║ ╚████╔╝    ██║   ██║  ██║")
        print("╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝     ╚═╝   ╚═╝  ╚═╝")
        time.sleep(0.2)
        print("were in the \"OYO\"")
        time.sleep(3)
    else:
        print(f"Incorrect! (Time for kartik to get the pookie machine) | {ans1}")

#Calls Functions
def func_selector():
    #Loop Main
    while True:
        time.sleep(0.2)
        input_value = input("\n\033[1;36;40mWhich program do you want to use?(1: Calculator, 2: B, 3: C, 4: D, 5: E, 6: Rock Paper Scissors!, 7: Credits, 8: Testing Program, 9: Exit Program): ")
        if input_value == "1":
            print("Launching Calculator")
            calculator()
        elif input_value == "2":
            print("Not Ready Yet!")
        elif input_value == "3":
            print("Not Ready Yet!")
        elif input_value == "4":
            print("Not Ready Yet!")
        elif input_value == "5":
            print("Not Ready Yet!")
        elif input_value == "6":
            print("Rock Paper Scissors")
            rock_paper_scissors()
        elif input_value == "7":
            print("Launching Credits Sequence")
            credits_seq()
        elif input_value == "8":
            print("Launching Testing Program")
            testing_prog()
        elif input_value == "9":
            print("\033[1;31;40m Starting Program Handler")
            exit_prog()
        elif input_value == "69":
            print("\nYou Found a Easter Egg!")
            easter_egg1()
        else:
            print("Unknown Value")

#Loop Start
if __name__ == "__main__":
    func_selector()