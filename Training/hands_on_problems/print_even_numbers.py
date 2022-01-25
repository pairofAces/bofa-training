# create a method that prints all even numbers from 0 to input (n)

def even_numbers(n):
    # for each number up to input (n)
    for x in range(n):
        # create logic to check if the number (x) is even
        if (x % 2 == 0):
            # print each even number up to the initial input (n) as strings
            # using the <string>.format() method to concatenate the even
            # number into the curly brackets within the string 
            print("{}".format(x))

n = 101
even_numbers(n)