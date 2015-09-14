while True:
    side_1 = raw_input("Enter a side: ")
    side_2 = raw_input("Enter another side: ")
    side_3 = raw_input("Enter another side: ")

    side_1 = int(side_1) ** 2
    side_2 = int(side_2) ** 2
    side_3 = int(side_3) ** 2

    statement = "\nThis is a pythagorean triple.\n"
    not_statement = "This is not a pythagorean triple.\n"

    triangle = [side_1, side_2, side_3]
    hypotenuse = max(triangle)

    triangle.remove(hypotenuse)

    if sum(triangle) == hypotenuse:
        print statement
    else:
        print not_statement

    count = raw_input("Would you like to go again? (y/n) ")
    if count == 'n':
        break

print "Goodbye!"

