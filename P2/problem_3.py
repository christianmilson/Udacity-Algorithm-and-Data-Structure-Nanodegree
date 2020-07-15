def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if (input_list is None or len(input_list) < 1):
        return [0]

    length = len(input_list)

    if (length == 1):
        return [input_list[0]]

    sorted = merge_sort(input_list)

    left = ''
    right = ''

    for idx in range(length, 0, -1):
        if ((idx - 1) % 2 == 0):
            left += str(sorted[idx -1])
        else:
            right += str(sorted[idx - 1])

    return [int(left), int(right)]

def merge_sort(input_list):
    size = len(input_list)

    if (size > 1):
        mid = size // 2
        left = input_list[:mid]
        right = input_list[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)

    return input_list

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1

        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[4, 6, 2, 5, 10, 8], [1064, 852]])
test_function([[1], [1]])
test_function([[], []])
