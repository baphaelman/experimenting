# Code written to brute force problem 29 from Math 191 Fall 2024
# Problem: A log is divided by 6 blue marks into 7 equal parts, by 12 red marks into 13 equal parts,and then cut into 20 equal pieces.
# Show that with the exception of two end pieces, each of the remaining 18 contains a red mark or a blue mark.
# the answer is found in running finalFunc(6, 12, 20)

def finalFunc(red, blue, pieces):
    """Given the number of blue and red marks and pieces cut, returns whether each non-end piece contains a red or blue mark"""
    redPieces = red + 1
    bluePieces = blue + 1

    subFactor = lcm(redPieces, bluePieces)
    sumRed = lcm(pieces, bluePieces) # what to add succesively when testing for reds
    sumBlue = lcm(pieces, redPieces) # what to add succesively when testing for blues

    tracker = sumRed
    countTracker = 1
    redCounts = []
    for _ in range(red): # testing for reds
        while (tracker > subFactor):
            tracker -= subFactor
            countTracker += 1
        redCounts.append(countTracker)
        tracker += sumRed
    
    tracker = sumBlue
    countTracker = 1
    blueCounts = []
    for _ in range(blue): # testing for blues (i know, repeating code, ew)
        while (tracker > subFactor):
            tracker -= subFactor
            countTracker += 1
        blueCounts.append(countTracker)
        tracker += sumBlue
    
    # return whether redCount and blueCount have common elements
    for i in redCounts:
        if i in blueCounts:
            return False
    return True

def lcm(a, b):
    """Returns the least common multiple of two numbers"""
    return a * b // gcd(a, b)

def gcd(a, b):
    """Returns the greatest common divisor of two numbers"""
    while b:
        a, b = b, a % b
    return a