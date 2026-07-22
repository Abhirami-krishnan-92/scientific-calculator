import math

history=[]

print("=" * 40)
print(" PYTHON MINICALCULATION")
print("*" * 40)

while True:
    print("\nChoose an operators")
    print("1. Addition(+)")
    print("2.SUbtraction (-)")
    print("3. Multiplication (*)")
    print("4.Division (/)")
    print("5. Modulus (%)")
    print("6.Power (^)")
    print("7. Square Root")
    print("8. View history")
    print("9.Exit")


    choice = input("\nEnter your choice (1-9): ")

    if choice == "9":
        print("Thank you for using Calculator!")
        break

    elif choice == "8":
        print("\n----- Calculation History -----")
        if len(history) == 0:
            print("No history available.")
        else:
            for item in history:
                print(item)
        continue

    elif choice == "7":
        num = float(input("Enter a number: "))
        if num < 0:
            print("Cannot find square root of negative number.")
        else:
            result = math.sqrt(num)
            print("Result =", round(result, 2))
            history.append(f"√{num} = {round(result,2)}")
        continue

    elif choice in ["1", "2", "3", "4", "5", "6"]:

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = num1 + num2
                operation = "+"

            elif choice == "2":
                result = num1 - num2
                operation = "-"

            elif choice == "3":
                result = num1 * num2
                operation = "*"

            elif choice == "4":
                if num2 == 0:
                    print("Division by zero is not allowed.")
                    continue
                result = num1 / num2
                operation = "/"

            elif choice == "5":
                result = num1 % num2
                operation = "%"

            elif choice == "6":
                result = num1 ** num2
                operation = "^"

            print("Result =", round(result, 2))
            history.append(f"{num1} {operation} {num2} = {round(result,2)}")

        except ValueError:
            print("Please enter valid numbers.")

    else:
        print("Invalid choice.")