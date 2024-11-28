unit = input("Choose what type of calculation do you want to do!(+ addition, - subtracting, / division, * multiplication, ** power): ")

if unit == "+":
    num1 = float(input("You've choosed addition, type the 1st number you wanna add: "))
    num2 = float(input("And now the 2nd number: "))
    result = num1 + num2
    print(f"The result is: {result}")
elif unit == "-":
    num1 = float(input("You've choosed subtraction, type the 1st number you wanna subtract: "))
    num2 = float(input("And now the 2nd number: "))
    result = num1 - num2
    print(f"The result is: {result}")
elif unit == "/":
    num1 = float(input("You've choosed division, type the 1st number you wanna divide: "))
    num2 = float(input("And now the 2nd number: "))
    result = num1 / num2
    print(f"The result is: {result}")
elif unit == "*":
    num1 = float(input("You've choosed multiplication, type the 1st number you wanna multiplicate: "))
    num2 = float(input("And now the 2nd number: "))
    result = num1 * num2
    print(f"The result is: {result}")
elif unit == "**":
    num1 = float(input("You've choosed power, type the 1st number you want to be powered: "))
    num2 = float(input(f"And now at what power should {num1} be powered?: "))
    result = num1 ** num2
    print(f"The result is: {result}")
else:
    print(f"{unit} is NOT an available type of calculation!")