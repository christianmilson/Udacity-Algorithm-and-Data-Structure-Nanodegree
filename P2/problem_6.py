def get_min_max(ints):
    if (ints is None or len(ints) < 1):
        return None

    min = ints[0]
    max = ints[0]

    for val in ints:
        if (val > max):
            max = val
        elif (val < min):
            min = val

    return min, max
## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


l = [i for i in range(14, 20)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((14, 19) == get_min_max(l)) else "Fail")

l = [i for i in range(0, 5)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 4) == get_min_max(l)) else "Fail")

print ("Pass" if ((5, 5) == get_min_max([5])) else "Fail")

print ("Pass" if (None == get_min_max([])) else "Fail")