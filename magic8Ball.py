from random import randint

responses = ["Yes", "No", "Probably", "Maybe", "I don't think so", "Perhaps",
             "It's possible", "Yes, I think so","Thats a boring Question Ask a new one ","Ummmmm What you asked ?","Oh really ! i have to answer this bull shit"]

print("Welcome to the Magic 8 ball!")


while True:

    question = input("Ask me a question: ")
    print(responses[randint(0, 10)])

    play = input("Would you like to play again? (Y/N) ")
    print ("")

    if play.lower() == "y" or play.lower()=='yes':
        continue

    elif play.lower() == "n" or play.lower() == "no":
        print("Goodbye!")
        break

    else:
        print("I didn't quite catch that.")

