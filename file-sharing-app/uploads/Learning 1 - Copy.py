# Delay/Wait Module
import time

last_edit_date = "24/10/24"
# Fake Startup Sequence
def startup_sequence():

    print("hello world: Initializing")

    print("Variables Loaded")
    print("Setting Up.")
    time.sleep(0.2)
    print("Setting Up..")
    print("Setting Up...")
    print("Setting Up....")
    print("Setting Up.....")
    print("Setting Up......")
    print("Setting Up.......")
    # time.sleep(Time in seconds) = wait
    time.sleep(0.2)
    time.sleep(0.2)
    print("Setting Up........")
    print("Setting Up........")
    print("Setting Up........")
    print("Setting Up........")
    print("Setting Up........")
    print("Setting Up........")
    print("Setting Up........ \n")

    print("Set Up Complete! \n")

    time.sleep(1)
    # Credits
    print(" _______")
    print("/   |   \   Made By:")
    print("|__/|\__|         Abhijot Singh VIII A")
    print("|  \|/  |   Last Edited on:")
    print("|___|___|          " + last_edit_date +"\n")

    print(" __  __             _         ____               __       _      _      _  _         _   ")
    print("|  \/  |           | |       |  _ \             /  \     | |    | |    (_)(_)       | |  ")
    print("| \  / |  __ _   __| |  ___  | |_) | _   _     /  _ \    | |__  | |__   _  _   ___  | |_ ")
    print("| |\/| | / _` | / _` | / _ \ |  _ < | | | |   /  /_\ \   | '_ \ | '_ \ | || | / _ \ | __|")
    print("| |  | || (_| || (_| ||  __/ | |_) || |_| |  /  ____  \  | |_) || | | || || || (_) || |_ ")
    print("|_|  |_| \__,_| \__,_| \___| |____/  \__, | /__/    \__\ |_.__/ |_| |_||_|| | \___/  \__|")   
    print("                                      __| |                            ___| |  ")
    print("                                     |___/                            |_____/  ")
    print("   ASCII Art \n")
    # Returns if process was successful, needed later
    tr_fa = True
    return tr_fa

st_re = startup_sequence()
# Returns if process was successful, needed later
if st_re:
    print("Completed Startup")
else:
    print("Error")

print("Console ready, Starting Code in 3 seconds")
time.sleep(1)
print("Console ready, Starting Code in 2 seconds")
time.sleep(1)
print("Console ready, Starting Code in 1 seconds")
time.sleep(1)
print("Console ready, Started Code Below: \n\n")

terminate_program_value = float(input("Enter \"1\" if you want to terminate the program:"))
# Program Terminator
if terminate_program_value == 1:
    print("\nTermination val = 1, Terminating program.\n")
    exit()
else:
    print("\nTermination canceled, continuing program.\n")

# Calculator Using Dictionary, input -> .lower() -> Dictionary -> if statements -> operation -> answer

def calculator():
    num1 = float(input("Enter 1st Number:"))
    num2 = float(input("Enter 2nd Number:"))
    # Calculator Dictionary
    operator_dictionary = {
        "x": "*",
        "X": "*",
        "*": "*",
        "div": "/",
        "+": "+",
        "plus": "+",
        "-": "-",
        "minus": "-",
        "sub": "-",
        "add": "+",
        "multiply": "*",
        "Minus": "-",
        "Sub": "-",
        "Add": "+",
        "Multiply": "*",
        "Div": "/",
        "/": "/",
    }

    operator_input = input("Enter operator (+, add, plus)(-, sub, Sub, Minus)(x, X, *, Multiply)(/, div, Div): ")

    operator = operator_dictionary.get(operator_input.lower(), "Invalid Key")

    print("\n")
    if operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "x":
        print(num1*num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "X":
        print(num1*num2)
    elif operator == "/":
        print(num1/num2)
    # Calculator restart
    else:
        restart_val = float(input("Invalid Operator, type 1 to restart or 0 to ignore:"))
        if restart_val == 1:
            print("Restarting")
            calculator()
        else:
            print("\nError Ignored")
# Calculator Function caller
calculator()




print("\n\nEnd of Code\n")