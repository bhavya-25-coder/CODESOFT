def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def get_operation():
    print("\n Select an operation:")
    print(" + : Addition")
    print(" - : Subtraction")
    print(" * : Multiplication")
    print(" / : Division")
    print(" % : Modulus")
    print(" ^ : Exponentiation")

    valid_operations = ['+', '-', '*', '/', '%', '^']
    while True:
        op = input("Enter operation symbol (+, -, *, /, %, ^): ").strip()
        if op in valid_operations:
            return op
        else:
            print("Invalid operation. Please choose from the list.")

def calculate(num1, num2, op):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero."
        return num1 / num2
    elif op == '%':
        if num2 == 0:
            return "Error: Cannot modulus by zero."
        return num1 % num2
    elif op == '^':
        return num1 ** num2
def calculator():
    print(" Welcome to the Advanced Calculator ")
    while True:
        num1 = get_number("\nEnter the first number: ")
        num2 = get_number("Enter the second number: ")
        op = get_operation()
        result = calculate(num1, num2, op)
        print(f"\n✅ Result: {num1} {op} {num2} = {result}")
        again = input("\n🔁 Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("👋 Thank you for using the calculator. Goodbye!")
            break
if __name__ == "__main__":
    calculator()
