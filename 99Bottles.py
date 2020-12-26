def firstVerse(step,count, bottleTense):
    firstVerse = "Step : %s, \t%s %s of beer on the wall, %s %s of beer." % (step,count, bottleTense, count, bottleTense)
    print(firstVerse)

def secondVerse(step,count, bottleTense):
    secondVerse = " \t\t\tTake one down and pass it around, %s %s of beer on the wall!\n" % (count, bottleTense)
    print(secondVerse)

def lyrics():
    steps = 1
    count = 99
    bottleTense = "bottles"

    while count > 1:
        firstVerse(steps,count, bottleTense)
        steps+=1
        count -= 1

        if count > 1:
            secondVerse(steps,count, bottleTense)
        elif count == 1:
            bottleTense = "bottle"
            secondVerse(steps,count, bottleTense)

    firstVerse(steps,count, bottleTense)

    count = "no more"
    bottleTense = "bottles"
    secondVerse(steps,count, bottleTense)

    count = "No more"
    firstVerse(steps,count, bottleTense)
    print("\t\t\tGo to the store and buy some more, 99 bottles of beer on the wall!\n")

lyrics()
