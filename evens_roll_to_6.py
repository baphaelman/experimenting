import random

def roll():
    x = random.randrange(1, 7)
    return x

def n_rolls_to_6(n):
    so_far, working = [], []
    for _ in range(n):
        while True:
            x = roll()
            working.append(x)
            if x == 6:
                so_far.append(working)
                working = []
                break
    return so_far

def filter_for_evens(s):
    """Filters s for all the lists that contain only even numbers."""
    for x in s:
        for i in x:
            if i % 2 != 0:
                s.remove(x)
                break
    filtered = [x for x in s if all(i % 2 == 0 for i in x)]
    return filtered

def final(n):
    """Computes the probability that the first roll is a 2 given n rolls"""
    count = 0
    even_rolls = filter_for_evens(n_rolls_to_6(n))
    for x in even_rolls:
        if x[0] == 2:
            count += 1
    print('probability: ', count/len(even_rolls))