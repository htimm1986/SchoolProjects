#############################################################
#############################################################
####Art######################################################
logo = """
 _____________________
|  _________________  |
| | htimm7734    0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
#############################################################
#############################################################
#####Functions###############################################
def add(n1, n2):
    """adds two numbers"""
    return n1 + n2
def subtract(n1, n2):
    """subtracts two numbers"""
    return n1 - n2
def multiply(n1, n2):
    """multiply two numbers"""
    return n1 * n2
def divide(n1, n2):
    """divides two numbers"""
    return n1 / n2
###############################################################
###############################################################
#####Dictionary and Inputs#####################################
operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide,
    }
def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    choosen_operation = input("Which operation to perform?: ")
    num2 = float(input("What is the second number?: "))
    if choosen_operation == "/" and num2 == 0:
        print("Impossible!")
        calculator()
    else:
        answer = operations[choosen_operation](num1, num2)
        print(f"{num1} {choosen_operation} {num2} = {answer}")
    continue_operation = True
    while continue_operation == True:
        keep_going = input("Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if keep_going == "y":
            continue_operation = True
            choosen_operation = input("Which operation to perform?: ")
            next_num = int(input("What is the next number?: "))
            if choosen_operation == "/" and next_num == 0:
                print("Impossible!")
                calculator()
            else:    
                next_answer = operations[choosen_operation](answer, next_num)
                print(f"{answer} {choosen_operation} {next_num} = {next_answer}")
                answer = next_answer
        else:
            continue_operation = False
            calculator()
calculator()