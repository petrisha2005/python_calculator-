def get_number(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("❌ Please enter a valid number")


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print("🧮 Safe Python Calculator")

while True:
    print("\n1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit")
    choice = input("Choose (1-5): ")

    if choice == "5":
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice")
        continue

    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        print("Result:", divide(a, b))
