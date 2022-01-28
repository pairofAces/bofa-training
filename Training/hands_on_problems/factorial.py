import math
import time

# complete the decorator function to print logging messages

def logging(func):
    return True


def factorial(num):
    time.sleep(2)
    print(math.factorial(num))

factorial(int( input() ))