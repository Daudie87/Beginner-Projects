from random import randint

responses = ["Yes", "No", "Probably", "Maybe", "I don't think so", "Perhaps",
             "It's possible", "Yes, I think so"]

print "Welcome to the Magic 8 ball!"

while True:
    question = raw_input("Ask me a question: ")
    print responses[randint(0, 7)]

    while True:
        play = raw_input("Would you like to play again? (Y/N) ")
        print ""

        if play == "Y" or play == "y":
            continue

        elif play == "N" or play == "n":
            print "Goodbye!"
            break

        else:
            print "I didn't quite catch that."

    break
