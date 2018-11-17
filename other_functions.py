from random import randint

def generate_code():
    range_start = 10**(4-1)
    range_end = (10**4)-1
    return randint(range_start, range_end)