unit = input("What unit of weight do you want to convert? (K/L) : ")
weight = float(input("Enter the weight: "))

if unit == "K":
    weight = weight * 2.205
    print(f"{weight} Lb/s")
elif unit == "L":
    weight = weight * 0.4536
    print(f"{weight} Kg/s")
else:
    print(f"{unit} is not available!")