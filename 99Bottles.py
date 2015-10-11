def firstVerse(count, bottleTense):
    firstVerse = "%s %s of beer on the wall, %s %s of beer." % (count, bottleTense, count, bottleTense)
    print firstVerse

def secondVerse(count, bottleTense):
    secondVerse = "Take one down and pass it around, %s %s of beer on the wall!\n" % (count, bottleTense)
    print secondVerse

def lyrics():
    count = 99
    bottleTense = "bottles"

    while count > 1:
        firstVerse(count, bottleTense)
        count -= 1

        if count > 1:
            secondVerse(count, bottleTense)
        elif count == 1:
            bottleTense = "bottle"
            secondVerse(count, bottleTense)

    firstVerse(count, bottleTense)

    count = "no more"
    bottleTense = "bottles"
    secondVerse(count, bottleTense)

    count = "No more"
    firstVerse(count, bottleTense)
    print "Go to the store and buy some more, 99 bottles of beer on the wall!"

print lyrics()
