# create a function that will take an input string 
# and return the reverse

def reverse_string(str):
    x = str[::-1]
    return x

ex = "this is an example"
print(ex)
print(reverse_string(ex))