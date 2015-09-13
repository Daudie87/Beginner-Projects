from random import randint

responses = ["Yes", "No", "Good luck with that!", "I wouldn't recommend that!", "Sounds like a bad idea mate",
             "That is excellent!", "I don't think so!", "Maybe."]

print "Welcome to the Magic 8 ball!"

i = 1
while i == 1:
    question = raw_input("Please enter your question: ")

    print "Thinking ..."

    print responses[randint(0, 5)]

    p = 1
    while p == 1:
        print "Would you like to play again? (Y/N)",
        play = raw_input()
        print ""

        if play == "Y" or play == "y":
            p -= 1

        elif play == "N" or play == "n":
            print "Goodbye!"
            i -= 1
            break

        else:
            print "I didn't quite catch that."
