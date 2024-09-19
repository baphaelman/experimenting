import random

def doubles(n):
    total = 0
    prev = 0
    for _ in range(n):
        rounds = 1
        while True:
            x = random.randrange(1, 14)
            if x == prev:
                prev = 0
                total += rounds
                break
            else:
                prev = x
                rounds += 1
    print("Doubles: ", total/n)

def both(n):
    total = 0
    cache = [0, 0]
    for _ in range(n):
        rounds = 1
        while True:
            x = random.randrange(1, 14)
            if x in cache:
                cache = [0, 0]
                total += rounds
                break
            else:
                cache = [cache[1], x]
                rounds += 1
    print("Both: ", total/n)

def with_marriages(n):
    total = 0
    cache = [0, 0]
    for _ in range(n):
        rounds = 1
        while True:
            x = random.randrange(1, 14)
            if x in cache: # doubles or sandwiches
                cache = [0, 0]
                total += rounds
                break
            elif sorted([cache[1], x]) == [12, 13]:
                cache = [0, 0]
                total += rounds
                break
            else: # nothing, continues
                cache = [cache[1], x]
                rounds += 1
    print("With Marriages: ", total/n)