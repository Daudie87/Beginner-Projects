count = 99

while count > 1:
    print "%s bottles of beer on the wall, %s bottles of beer." % (count, count)
    count -= 1
    if count > 1:
        print "Take one down and pass it around, %s bottles of beer on the wall!" % count
        print ""
    elif count == 1:
        print "Take one down and pass it around, %s bottle of beer on the wall!" % count
        print ""

while count == 1:
    print "%s bottle of beer on the wall, %s bottle of beer." % (count, count)
    count -= 1
    print "Take one down and pass it around, no more bottles of beer on the wall!"
    print ""

while count == 0:
    print "No more bottles of beer on the wall, no more bottles of beer."
    print "Go to the store and buy some more, 99 bottles of beer on the wall!"
    break
