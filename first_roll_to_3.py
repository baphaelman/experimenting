import random

def roll_dice():
    x = random.randrange(1, 7)
    return x

def n_tries(n):
    k, without_numbers = n, 0
    working_list = []
    while k > 0:
        thing = False
        while not thing:
            x = roll_dice()
            working_list.append(x)
            if x == 3:
                k -= 1
                if 4 not in working_list and 5 not in working_list and 6 not in working_list:
                    without_numbers += 1
                working_list = []
                thing = True
    print('count:', without_numbers)
    print('total:', n)
    probability = without_numbers / n
    return probability