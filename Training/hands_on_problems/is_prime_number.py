# write a function isPrimeNumber(num), take the (num) parameter being passed
# and return the string 'true' if the paramter is a prime number, otherwise
# return the string 'false'
    # the range will be between 1 and 2^16

def isPrimeNumber(num):
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if (num % 2) == 0:
                print("False")
                break
        else:
            print("True")
    else:
        print("False")

x = 12
isPrimeNumber(x)