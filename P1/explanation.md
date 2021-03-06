## Project 1

The task was to implement a LRU cache.

For this approach i used a hash map to ensure operations occured in constant time

Time Complexity is O(1) for get as occurs in constant time
Time Complexity is O(1) for set as occurs in constant time
Space Complexity is O(n) as is dependent of the capacity of the LRU Cache

## Project 2

The task was to implement a file finder.

For this approach recursion is the way to go, as the search depth is unknown for the given search paramter.

Time Complexity is O(n) where n is the total number of files present in the directory (including all sub directories)
Space Complexity is also O(n), where n is the total number of files present in the directory.

## Project 3

The task was to implement a huffman coder.

For this approach, first i used a hash map to determine the character frequency of input string, then built up a huffman tree using summation of largest nodes.

Time Complexity is O(nlogn) for encode as the as we are running a loop for each n 
Space Complexity is O(n) for encode as its dependent on the number of unique letters in the input string
Time Complexity is O(n) for decode where n is size of encoded string
Space Complexity is O(1) as only one varible is used

## Project 4

The task was to implement a basic active directory clone.

For this approach i chose to implement recursion in the is_user_in_group method as the search depth is unknown

Time Complexity is O(n), where n represents the number of recursive iterations need to search, this is dependent on the number of groups and there sub groups/users.
Space Complexity is O(1), as the method only returns once.

## Project 5

The task was to implement a blockchain.

For this approach i used a linked list

Time Complexity is O(1) as the push operation occurs in constant time.
Space Complexity is O(n) as its dependent on the number of blocks (nodes) in the blockchain.

## Project 6

The task was to implement a union and intersect between two linked lists.

For the union i used a dictionary to build up a hash map of unique numbers in the first linked list, to use to match whether or not a given number in the second linked list existed in first
Time Complexity is O(n) as its dependent on the number of elements in the linked lists
Space Complexity is also O(n) as each elements is added to the dict variable

For the intersection i used a dictionary to build a hash map of numbers found in first linked list to match against second
Time Complexity is O(n^2) as it uses a nested while loop
Space Complexity is O(n) as each element is added to dict variable

 
