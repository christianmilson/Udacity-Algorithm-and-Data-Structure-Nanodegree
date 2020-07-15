## Problem 1

Task: Find the floored squared root of an integer.

To satisfy the required time complexity of O(logn) i used binary search to find the floored squared root of a given input.

Time Complexity is O(logn)
Space Complexity is O(1)

## Problem 2

Task: Search in a rotated sorted array.

To satisfy the required time complexity of O(logn) i first found the pivot point of the given input array, then spilt
array into two and performed binary search on each, until the index was found.

Time Complexity is O(logn)
Space Complexity is O(logn)

## Problem 3

Task: Rearrange Array Elements so as to form two number such that their sum is maximum.

This was the trickiest of all the problems to solve, I used a divide and conquer sorthing alorithm...merge sort to meet the
O(nlogn) requirement.

I used merge sort to sorted the input array, once sorted I added all values with even indexs to a single array, and odd indexes to another
to find the maximum sum.

Time Complexity is O(nlog(n))
Space Complexity is O(n)

## Problem 4

Task: Dutch National Flag Problem.

To meets the requirement of a single traversal, i used pointers to track the position of zero and two, to partition the array.
Time Complexity is O(n)
Space Complexity is O(1)

## Problem 5

Task: Make a basic autocomplete.

To statisy the requirement i used a trie data structure.
Time Complexity is O(n x m) (n = number inputs, m = length of average input)
Space Complexity is O(n)

## Problem 6

Task: Max and Min in a Unsorted Array.

For this i managad a single traversal, by storing the min and max values found in variables outside the scope of the 
traversal loop, and then comparing the current val in the traversal with these two value of these two variables.
Time Complexity is O(n)
Space Complexity is O(1)

## Problem 7

Task: Make a basic HTTP router.

For this i first split the url into its given components, before creating a trie data structure.
Time Complexity is O(n x m) (n = number inputs, m = length of average input)
Space Complexity is O(n)
