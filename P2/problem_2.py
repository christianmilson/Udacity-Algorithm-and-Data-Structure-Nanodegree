def pivot(arr, start, end):
    if (start == end):
        return 0

    mid = end // 2

    if (mid < end and arr[mid] > arr[mid + 1]):
        return mid
    elif (start < mid and arr[mid] < arr[mid - 1]):
        return mid -1
    else:
        return pivot(arr, start + 1, end)

def binarySearch(input_list, start, end, search):
    mid = (start + end) // 2

    if (search == input_list[mid]):
        return mid
    elif (search > input_list[mid]):
        return binarySearch(input_list, mid + 1, end, search)
    else:
        return binarySearch(input_list, start, mid - 1, search)

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    length = len(input_list)

    if (length < 1):
        return -1

    if (length == 1):
        if (input_list[0] == number):
            return 0
        else:
            return -1

    pivotPoint = pivot(input_list, 0, length)

    if (number == input_list[pivotPoint]):
        return pivotPoint
    elif (number > input_list[pivotPoint]):
        return -1

    if (number >= input_list[0] and number <= input_list[pivotPoint]):
        return binarySearch(input_list, 0, pivotPoint - 1, number)

    return binarySearch(input_list, pivotPoint + 1, length - 1, number)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[], -1])
test_function([[1], 0])