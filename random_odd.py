import random

def random_odd(min_range, max_range):
    final_number = random.randint(min_range, max_range)
    while final_number % 2 == 0:
        final_number = random.randint(min_range, max_range)
    else:
        return final_number




def main():
    minimum = 20
    maximum = 73
    random_odd(minimum, maximum)


main()