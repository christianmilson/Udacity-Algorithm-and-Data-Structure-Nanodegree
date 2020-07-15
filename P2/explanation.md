## Problem 1

To satisfy the required time complexity of O(logn) i used binary search to find the floored squared root of a given input.

Time Complexity is O(logn)
Space Complexity is O(1)

## Problem 2

To satisfy the required time complexity of O(logn) i first found the pivot point of the given input array, then spilt
array into two and performed binary search on each, until the index was found.

Time Complexity is O(logn)
Space Complexity is O(logn)

## Problem 3

This was the trickiest of all the problems to solve, I used a divide and conquer sorthing alorithm...merge sort to meet the
O(nlogn) requirement.

I used merge sort to sorted the input array, once sorted I added all values with even indexs to a single array, and odd indexes to another
to find the maximum sum.

Time Complexity is O(nlog(n))
Space Complexity is O(n)

## Problem 4

To meets the requirement of a single traversal, i used pointers to track the position of zero and two, to partition the array.
Time Complexity is O(n)
Space Complexity is O(1)

## Problem 5

To statisy the requirement i used a trie data structure.
Time Complexity is O(n x m) (n = number inputs, m = length of average input)
Space Complexity is O(n)

## Problem 6

For this i managad a single traversal, by storing the min and max values found in variables outside the scope of the 
traversal loop, and then comparing the current val in the traversal with these two value of these two variables.
Time Complexity is O(n)
Space Complexity is O(1)

## Problem 7

For this i first split the url into its given components, before creating a trie data structure.
Time Complexity is O(n x m) (n = number inputs, m = length of average input)
Space Complexity is O(n)
