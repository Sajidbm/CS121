def myStrategy(myscore, theirscore, last):

    diff = myscore-theirscore
    theirdist = 100 - theirscore
    mydist = 100 - myscore


    if theirscore == 0:
        return 33


    elif theirdist < mydist:
        return (theirscore-myscore)//2.5 + 1


    else:
        return (mydist)//4
