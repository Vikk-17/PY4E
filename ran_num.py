# Printing random number according to user input

import random
import time


def _random_num(num):
    
    if (num == 1):
        total_num = int(input("How many random numbers do u want to print>>> "))
        for i in range(total_num):
            time.sleep(0.1)
            print(random.random())

    elif(num == 2):
        lower_range=int(input("Lower range>>> "))
        upper_range=int(input("Upper range>>> "))
        print(random.randint(lower_range, upper_range))

    else:
        quit()


user_input = int(input("""1. pseudorandom numbers.
2. random number between range.\n"""))
_random_num(user_input)




