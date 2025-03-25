def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

addition = add
subtraction = subtract
multiplication = multiply
division = divide

operations = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiplication,
    "/" : division,
}

retry = True

n1 = None

while retry:

    if n1 == None:
        n1 = float(input("Enter first number: "))

    operator = None

    operator = input("Enter operator: ")
    
    while operator not in operations:
        operator = input("Enter valid operator: ")
    
    n2 = float(input("Enter second number: "))

    result = (operations[operator](n1, n2))

    result_output = round(result, 2)

    print(f"{n1} {operator} {n2} = {result_output}")

    another = input("Do you want to use result for another operation? Type 'Yes' or 'No': ").lower()

    if another == "yes":
        n1 = result
        retry = True
    else:
        print(result_output)
        retry = False
