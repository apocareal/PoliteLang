import re
import random
import time
import math

variables = {}
functions = {}

def polite_interpreter(line):
    if not line.strip().lower().endswith("thanks."):
        print("Rude! You forgot to say 'thanks.'")
        return

    line = line.strip()[:-7].lower()  # Remove ' thanks.'

    # Variable creation (number)
    if "create a number called" in line or "make a number called" in line:
        match = re.match(r".*number called (\w+) .*?(\d+)", line)
        if match:
            name, value = match.groups()
            variables[name] = int(value)
            print(f"Politely created number {name} with value {value}")

    # Variable creation (string)
    elif "create a string called" in line:
        match = re.match(r".*string called (\w+) and set it to (.+)", line)
        if match:
            name, value = match.groups()
            variables[name] = value.strip()
            print(f"Politely created string {name}")
        else:
            # Try alternative format
            match = re.match(r".*string called (\w+) .*?to (.+)", line)
            if match:
                name, value = match.groups()
                variables[name] = value.strip()
                print(f"Politely created string {name}")

    # Variable creation (boolean)
    elif "create a boolean called" in line:
        match = re.match(r".*boolean called (\w+) .*?(true|false)", line)
        if match:
            name, value = match.groups()
            variables[name] = value == "true"
            print(f"Politely created boolean {name} = {value}")

    # List creation
    elif "create a list called" in line:
        match = re.match(r".*list called (\w+)", line)
        if match:
            name = match.group(1)
            variables[name] = []
            print(f"Politely created empty list {name}")

    # Addition
    elif "add" in line and "store the result in" in line:
        match = re.match(r"add (\w+) and (\w+) and store the result in (\w+)", line)
        if match:
            a, b, result = match.groups()
            variables[result] = float(variables.get(a, 0)) + float(variables.get(b, 0))
            print(f"Politely calculated {a} + {b} = {variables[result]}")

    # Subtraction
    elif "subtract" in line and "from" in line and "store the result in" in line:
        match = re.match(r"subtract (\w+) from (\w+) and store the result in (\w+)", line)
        if match:
            a, b, result = match.groups()
            variables[result] = float(variables.get(b, 0)) - float(variables.get(a, 0))
            print(f"Politely calculated {b} - {a} = {variables[result]}")

    # Multiplication
    elif "multiply" in line and "by" in line and "store the result in" in line:
        match = re.match(r"multiply (\w+) by (\w+) and store the result in (\w+)", line)
        if match:
            a, b, result = match.groups()
            variables[result] = float(variables.get(a, 0)) * float(variables.get(b, 0))
            print(f"Politely calculated {a} × {b} = {variables[result]}")

    # Division
    elif "divide" in line and "by" in line and "store the result in" in line:
        match = re.match(r"divide (\w+) by (\w+) and store the result in (\w+)", line)
        if match:
            a, b, result = match.groups()
            divisor = float(variables.get(b, 1))
            if divisor == 0:
                print("😅 Sorry, but I can't divide by zero politely!")
                return
            variables[result] = float(variables.get(a, 0)) / divisor
            print(f"🧮 Politely calculated {a} ÷ {b} = {variables[result]}")

    # Power/Exponentiation
    elif "raise" in line and "to the power of" in line and "store the result in" in line:
        match = re.match(r"raise (\w+) to the power of (\w+) and store the result in (\w+)", line)
        if match:
            base, exp, result = match.groups()
            variables[result] = float(variables.get(base, 0)) ** float(variables.get(exp, 0))
            print(f"🧮 Politely calculated {base}^{exp} = {variables[result]}")

    # Square root
    elif "find the square root of" in line and "store it in" in line:
        match = re.match(r"find the square root of (\w+) and store it in (\w+)", line)
        if match:
            a, result = match.groups()
            val = float(variables.get(a, 0))
            if val < 0:
                print("Sorry, but I can't find the square root of a negative number politely!")
                return
            variables[result] = math.sqrt(val)
            print(f"Politely calculated √{a} = {variables[result]}")

    # String concatenation
    elif "combine" in line and "and" in line and "store it in" in line:
        match = re.match(r"combine (\w+) and (\w+) and store it in (\w+)", line)
        if match:
            a, b, result = match.groups()
            variables[result] = str(variables.get(a, "")) + str(variables.get(b, ""))
            print(f"Politely combined strings into {result}")

    # String length
    elif "find the length of" in line and "store it in" in line:
        match = re.match(r"find the length of (\w+) and store it in (\w+)", line)
        if match:
            a, result = match.groups()
            variables[result] = len(str(variables.get(a, "")))
            print(f"Politely measured length of {a} = {variables[result]}")

    # String uppercase
    elif "make" in line and "uppercase and store it in" in line:
        match = re.match(r"make (\w+) uppercase and store it in (\w+)", line)
        if match:
            a, result = match.groups()
            variables[result] = str(variables.get(a, "")).upper()
            print(f"Politely made {a} uppercase")

    # String lowercase
    elif "make" in line and "lowercase and store it in" in line:
        match = re.match(r"make (\w+) lowercase and store it in (\w+)", line)
        if match:
            a, result = match.groups()
            variables[result] = str(variables.get(a, "")).lower()
            print(f"Politely made {a} lowercase")

    # List append
    elif "add" in line and "to the list" in line:
        match = re.match(r"add (\w+) to the list (\w+)", line)
        if match:
            item, list_name = match.groups()
            if list_name not in variables:
                variables[list_name] = []
            variables[list_name].append(variables.get(item, item))
            print(f"Politely added {item} to list {list_name}")

    # List length
    elif "count the items in" in line and "store it in" in line:
        match = re.match(r"count the items in (\w+) and store it in (\w+)", line)
        if match:
            list_name, result = match.groups()
            if isinstance(variables.get(list_name), list):
                variables[result] = len(variables[list_name])
                print(f"Politely counted {variables[result]} items in {list_name}")
            else:
                print(f"Sorry, {list_name} is not a list!")

    # Random number generation
    elif "generate a random number between" in line and "store it in" in line:
        match = re.match(r"generate a random number between (\d+) and (\d+) and store it in (\w+)", line)
        if match:
            min_val, max_val, result = match.groups()
            variables[result] = random.randint(int(min_val), int(max_val))
            print(f"Politely generated random number {variables[result]}")

    # Print
    elif "print" in line:
        match = re.match(r".*print (\w+)", line)
        if match:
            name = match.group(1)
            value = variables.get(name, '[undefined]')
            if isinstance(value, list):
                print(f"{name} = {value}")
            else:
                print(f"{name} = {value}")

    # Print with message
    elif "say" in line and "followed by" in line:
        match = re.match(r'say "([^"]+)" followed by (\w+)', line)
        if match:
            message, var = match.groups()
            value = variables.get(var, '[undefined]')
            print(f"💬 {message} {value}")

    # User input
    elif "ask the user for their" in line and "store it in" in line:
        match = re.match(r"please ask the user for their (.+?) and store it in (\w+)", line)
        if match:
            prompt_text, var = match.groups()
            user_input = input(f"Please enter your {prompt_text.strip()}: ")
            if user_input.replace('.', '').replace('-', '').isnumeric():
                variables[var] = float(user_input)
            else:
                variables[var] = user_input
            print(f"Politely stored your input in {var}")

    # Wait/Sleep
    elif "wait for" in line and "seconds" in line:
        match = re.match(r"wait for (\d+) seconds", line)
        if match:
            seconds = int(match.group(1))
            print(f"Politely waiting for {seconds} seconds...")
            time.sleep(seconds)
            print("Done waiting!")

    # Conditionals - Greater than
    elif "if" in line and "is greater than" in line and "then print" in line:
        match = re.match(r"if (\w+) is greater than (\w+) then print (\w+)", line)
        if match:
            a, b, target = match.groups()
            if float(variables.get(a, 0)) > float(variables.get(b, 0)):
                print(f"{target} = {variables.get(target, '[undefined]')}")

    # Conditionals - Less than
    elif "if" in line and "is less than" in line and "then print" in line:
        match = re.match(r"if (\w+) is less than (\w+) then print (\w+)", line)
        if match:
            a, b, target = match.groups()
            if float(variables.get(a, 0)) < float(variables.get(b, 0)):
                print(f"{target} = {variables.get(target, '[undefined]')}")

    # Conditionals - Equal to
    elif "if" in line and "equals" in line and "then print" in line:
        match = re.match(r"if (\w+) equals (\w+) then print (\w+)", line)
        if match:
            a, b, target = match.groups()
            if variables.get(a) == variables.get(b):
                print(f"{target} = {variables.get(target, '[undefined]')}")

    # Conditionals - Execute multiple commands
    elif "if" in line and "is greater than" in line and "then" in line and "and" in line:
        match = re.match(r"if (\w+) is greater than (\w+) then (.+?) and (.+)", line)
        if match:
            a, b, cmd1, cmd2 = match.groups()
            if float(variables.get(a, 0)) > float(variables.get(b, 0)):
                polite_interpreter(cmd1 + " thanks.")
                polite_interpreter(cmd2 + " thanks.")

    # Loop - Fixed count
    elif "repeat this line" in line and "times" in line and ":" in line:
        match = re.match(r"repeat this line (\d+) times: (.+)", line)
        if match:
            count, inner = match.groups()
            print(f"Politely repeating {count} times...")
            for i in range(int(count)):
                print(f"  Loop {i+1}:")
                polite_interpreter(inner + " thanks.")

    # Loop - While condition
    elif "while" in line and "is less than" in line and "do" in line:
        match = re.match(r"while (\w+) is less than (\w+) do (.+)", line)
        if match:
            var, limit, command = match.groups()
            print(f"🔄 Politely looping while {var} < {limit}...")
            iterations = 0
            while float(variables.get(var, 0)) < float(variables.get(limit, 0)) and iterations < 100: 
                polite_interpreter(command + " thanks.")
                iterations += 1
            if iterations >= 100:
                print("Loop stopped politely to prevent infinite loops!")

    # Function definition
    elif "define a function called" in line and "that does" in line:
        match = re.match(r"define a function called (\w+) that does (.+)", line)
        if match:
            func_name, func_body = match.groups()
            functions[func_name] = func_body.strip()
            print(f"Politely defined function {func_name}")
            print(f"Function body: {func_body.strip()}") 

    # Function call
    elif "call the function" in line:
        match = re.match(r"call the function (\w+)", line)
        if match:
            func_name = match.group(1)
            if func_name in functions:
                print(f"Politely calling function {func_name}")
                func_body = functions[func_name]
                # Make sure the function body ends with 'thanks.' if it doesn't already
                if not func_body.strip().lower().endswith("thanks."):
                    func_body += " thanks."
                polite_interpreter(func_body)
            else:
                print(f"Sorry, function {func_name} doesn't exist!")
                print(f"Available functions: {list(functions.keys())}") 

    # Clear screen
    elif "clear the screen" in line:
        print("\n" * 50) 
        print("✨ Screen politely cleared!")

    # Show all variables
    elif "show all variables" in line:
        print("📊 All variables (politely displayed):")
        for name, value in variables.items():
            print(f"  {name} = {value}")

    # Delete variable
    elif "delete the variable" in line:
        match = re.match(r"delete the variable (\w+)", line)
        if match:
            var_name = match.group(1)
            if var_name in variables:
                del variables[var_name]
                print(f"Politely deleted variable {var_name}")
            else:
                print(f"Variable {var_name} doesn't exist!")

    # Complex math - factorial
    elif "find the factorial of" in line and "store it in" in line:
        match = re.match(r"find the factorial of (\w+) and store it in (\w+)", line)
        if match:
            a, result = match.groups()
            val = int(variables.get(a, 0))
            if val < 0:
                print("Sorry, factorial of negative numbers isn't polite!")
                return
            variables[result] = math.factorial(val)
            print(f"Politely calculated {a}! = {variables[result]}")

    # Polite compliments
    elif "compliment the user" in line:
        compliments = [
            "You're doing great! ",
            "Your politeness is inspiring!",
            "You have excellent manners!",
            "Thank you for being so courteous! ",
            "Your kindness brightens my day! "
        ]
        print(f"{random.choice(compliments)}")

    else:
        responses = [
            "I didn't understand that sentence, but it was polite at least.",
            "Hmm, I'm not sure what you meant, but thank you for being polite!",
            "That's a new one for me, but I appreciate the courtesy!"
        ]
        print(random.choice(responses))

def run_politelang(code):
    """Execute PoliteLang code by processing each line"""
    print("Welcome to PoliteLang - The Courteous Programming Language!")
    print("Remember: Every command must end with 'thanks.' or it won't work!\n")
    
    lines = code.strip().split('\n')
    for line in lines:
        line = line.strip()
        if line:  
            polite_interpreter(line)
            print() 

def show_help():
    print("""
PoliteLang Commands (all must end with 'thanks.'):

Variables:
- Create a number called X with value 5 thanks.
- Create a string called Y and set it to Hello thanks.
- Create a boolean called Z with value true thanks.
- Create a list called mylist thanks.

Math:
- Add X and Y and store the result in Z thanks.
- Subtract X from Y and store the result in Z thanks.
- Multiply X by Y and store the result in Z thanks.
- Divide X by Y and store the result in Z thanks.
- Raise X to the power of Y and store the result in Z thanks.
- Find the square root of X and store it in Y thanks.
- Find the factorial of X and store it in Y thanks.

Strings:
- Combine X and Y and store it in Z thanks.
- Find the length of X and store it in Y thanks.
- Make X uppercase and store it in Y thanks.
- Make X lowercase and store it in Y thanks.

Lists:
- Add X to the list mylist thanks.
- Count the items in mylist and store it in count thanks.

Random:
- Generate a random number between 1 and 10 and store it in X thanks.

Input/Output:
- Please ask the user for their name and store it in username thanks.
- Print X thanks.
- Say "Hello" followed by username thanks.

Control:
- Wait for 3 seconds thanks.
- If X is greater than Y then print Z thanks.
- If X is less than Y then print Z thanks.
- If X equals Y then print Z thanks.
- Repeat this line 5 times: print X thanks.
- While X is less than Y do add 1 to X thanks.

Functions:
- Define a function called greet that does print greeting thanks.
- Call the function greet thanks.

Utilities:
- Show all variables thanks.
- Delete the variable X thanks.
- Clear the screen thanks.
- Compliment the user thanks.
    """)
if __name__ == "__main__":
    show_help()
    print("\n" + "="*60 + "\n")
    
    code = """
Please ask the user for their name and store it in username thanks.
Create a string called greeting and set it to Hello there,  thanks.
Combine greeting and username and store it in message thanks.
Print message thanks.
Please ask the user for their favorite number and store it in fav thanks.
Multiply fav by fav and store the result in squared thanks.
Say "Your favorite number squared is" followed by squared thanks.
Create a number called ten with value 10 thanks.
If fav is greater than ten then compliment the user thanks.
Create a list called numbers thanks.
Add fav to the list numbers thanks.
Add squared to the list numbers thanks.
Print numbers thanks.
Generate a random number between 1 and 100 and store it in lucky thanks.
Say "Your lucky number today is" followed by lucky thanks.
Define a function called farewell that does say "Thank you for using PoliteLang!" followed by username thanks.
Call the function farewell thanks.
"""
    
    run_politelang(code)
