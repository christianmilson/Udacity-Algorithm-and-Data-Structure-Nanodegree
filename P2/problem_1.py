def sqrt(number):
    if (number is None or number < 0):
        return None

    if (number <= 1):
        return number

    start = 1
    end = number

    res = None
    while start <= end:
        middle = (start + end) // 2
        mid_sqrd = middle * middle

        if mid_sqrd == number:
            res = middle
            break

        elif mid_sqrd < number:
            start = middle + 1
            res = middle
        else:
            end = middle - 1

    return res

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (None == sqrt(None)) else "Fail")
print ("Pass" if  (70 == sqrt(5000)) else "Fail")
print ("Pass" if  (None == sqrt(-1)) else "Fail")