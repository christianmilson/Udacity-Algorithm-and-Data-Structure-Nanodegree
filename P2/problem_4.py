def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    zero_pointer = 0
    two_pointer  = len(input_list) - 1
    i = 0

    while (i <= two_pointer):
        if (input_list[i] == 0):
            val = input_list[i]
            input_list[i] = input_list[zero_pointer]
            input_list[zero_pointer] = val
            i += 1
            zero_pointer += 1
        elif (input_list[i] == 1):
            i += 1
        else:
            val = input_list[i]
            input_list[i] = input_list[two_pointer]
            input_list[two_pointer] = val
            two_pointer -= 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])
test_function([2])