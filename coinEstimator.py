# coin weight in grams
pennyWeight = 2.5
nickelWeight = 5.0
dimeWeight = 2.268
quarterWeight = 5.670

print("Welcome to the Coin Estimator!")
print("Please enter the weight in grams of your: ")

pennies = float(input("Pennies: "))
nickels = float(input("Nickels:" ))
dimes = float(input("Dimes: "))
quarters = float(input("Quarters: "))

print(f"\nYour pennies weigths : {pennies*pennyWeight} gm")
print(f"Your nickles weigths : {nickels*nickelWeight} gm")
print(f"Your dimes weigths : {dimes*dimeWeight} gm")
print(f"Your quarter weigths : {quarters*quarterWeight} gm")
print(f"\nYour Total pocket weights : {(quarters*quarterWeight) +(pennies*pennyWeight)+(nickels*nickelWeight)+(dimes*dimeWeight)} Grams")