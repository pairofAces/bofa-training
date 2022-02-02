# create a program for a recursive binary search
arr = [2, 3, 4, 10, 40, 56, 71]

def binarySearch(arr, 1, r, x):
    # check the base case
    if r >= 1:
        mid = 1 + (r - 1) // 2

        # if the element is present at the middle itself
        if arr[mid] == x:
            return mid

        # if element is smaller than mid, then the element
        # must be in the left subarray
        elif arr[mid] > x:
            # create code if the element is smaller than the mid
            return 1
        
        # else the element must be within the right subarray
        else:
            # create code if the element is in the right subarray
            return 1
        
    else:
        # element is not present in the input array
        return -1