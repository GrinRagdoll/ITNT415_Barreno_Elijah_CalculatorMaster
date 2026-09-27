# calculator.py - ITNT415 Calculator Project
# Author: Elijah Barreno

BIG_NUMBERS = {
    '0': ["  ___  ", " / _ \\ ", "| | | |", "| |_| |", " \\___/ "],
    '1': [" __ ", "/_ |", " | |", " | |", " |_|"],
    '2': [" ___  ", "|__ \\ ", "  / / ", " / /_ ", "|____|"],
    '3': [" ____ ", "|___ \\", " __) |", "|__ < ", "___/ "],
    '4': [" _  _   ", "| || |  ", "| || |_ ", "|__   _|", "   |_|  "],
    '5': [" ____ ", "| ___|", "|___ \\", " ___) |", "|____/ "],
    '6': ["  __  ", " / /  ", "/ _ \\ ", "| (_) |", " \\___/ "],
    '7': [" ____ ", "|___ \\", "  __) |", " / __/ ", "|_____|"],
    '8': ["  ___ ", " ( _ )", " / _ \\", "| (_) |", " \\___/ "],
    '9': ["  ___ ", " / _ \\", "| (_) |", " \__, |", "   /_/ "],
    '.': ["   ", "   ", "   ", "   ", " _ "],
    '-': ["       ", "       ", " _____ ", "       ", "       "]
}

def print_giant_result(result_string):
    print("\nBOOM! RESULT:")
    lines = ["", "", "", "", ""]
    for char in str(result_string):
        if char in BIG_NUMBERS:
            char_art = BIG_NUMBERS[char]
            for i in range(5):
                lines[i] += char_art[i] + "  "
        else:
            for i in range(5):
                lines[i] += char + "  "
    for line in lines:
        print(line)
    print()

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! That's not a number, try again.")

def calculator():
    print("=========================================")
    print("   🤖 MEGA CALCULATOR 3000 (ASCII EDITION) ")
    print("=========================================")
    
    num1 = get_number("Enter first number: ")
    op = input("Enter operator (+, -, *, /): ")
    num2 = get_number("Enter second number: ")

    result = None

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("🚨 ERROR: Cannot divide by zero! Black hole warning!")
            return
        else:
            result = num1 / num2
    else:
        print("❌ Invalid operator! Use +, -, *, or /.")
        return

    if result.is_integer():
        result = int(result)
        
    print_giant_result(result)

if __name__ == "__main__":
    calculator()