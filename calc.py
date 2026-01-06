import math

def calculator():
    while True:
        print("""
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Square Root
7. Exit
""")
        choice = input("Choose (1-7): ")

        if choice == "7":
            break

        if choice == "6":
            num = float(input("Enter number: "))
            print("Result:", math.sqrt(num))
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", a + b)
        elif choice == "2":
            print("Result:", a - b)
        elif choice == "3":
            print("Result:", a * b)
        elif choice == "4":
            print("Result:", "Error" if b == 0 else a / b)
        elif choice == "5":
            print("Result:", pow(a, b))
        else:
            print("Invalid choice")

calculator()
