# create a function that takes two lists and returns a list containing
# the common elements between the initial two lists. 
    # no duplicates
    # make sure the program works with lists of different sizes

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def common_elements(a, b):
    # convert the input lists into sets
    set_a = set(a)
    set_b = set(b)

    # use if loop to compare sets (a) and (b)
    if (set_a & set_b):
        # cast the comparison between set_a and set_b as a (list)
        # and print the common elements
            # the (&) operator compares the sets and returns a set with the
            # common elements, without duplicates
        print(list(set_a & set_b))
    else:
        print("No common elements")


common_elements(a, b)