# Sorting and Searching Algorithms

This repository contains Python code for sorting and searching algorithms. It includes an abstract base class for searching algorithms, two concrete implementations (`LinearSearch` and `BinarySearch`), and a performance comparison plot.

## Search Algorithms

### Search Base Class (`Search`)

- The `Search` class is an abstract base class (ABC) for searching algorithms.
- It provides a common interface for different search algorithms.
- The `__init__` method initializes the search with a list of items to search within and a target element.
- The `search` method performs the search operation and returns the index of the target element or -1 if not found.
- The `_time` method records the execution time of the search operation.
- Subclasses must implement the `_search` method to define the specific search algorithm.

### Linear Search (`LinSearch`)

- The `LinSearch` class is a concrete implementation of the `Search` class for linear search.
- It performs a linear search through the list of items to find the target element.
- The `_search` method iterates through the list and returns the index of the target element or -1 if not found.

### Binary Search (`BinarySearch`)

- The `BinarySearch` class is a concrete implementation of the `Search` class for binary search.
- It performs a binary search through a sorted list of items to find the target element.
- The `_search` method uses a binary search algorithm to efficiently locate the target element in the sorted list.

## Sorting Algorithms

### Sorting Base Class (`Sort`)

- The `Sort` class is an abstract base class (ABC) for sorting algorithms.
- It provides a common interface for different sorting algorithms.
- The `__init__` method initializes the sorting with a list of items to sort.
- The `_sort` method is an abstract method that should be implemented by subclasses to define the specific sorting algorithm.
- The `_time` method records the execution time of the sorting operation.

### Merge Sort (`MergeSort`)

- The `MergeSort` class is a concrete implementation of the `Sort` class for merge sort.
- It implements the merge sort algorithm to efficiently sort a list of items.

### Bubble Sort (`BubbleSort`)

- The `BubbleSort` class is a concrete implementation of the `Sort` class for bubble sort.
- It implements the bubble sort algorithm to sort a list of items.


## Example Usage

```python
# Example usage of LinearSearch and BinarySearch
linear_search = LinSearch([3, 1, 4, 5, 9], 4)
binary_search = BinarySearch([3, 1, 4, 5, 9], 4)

# Perform the search and get the results
result_linear = linear_search.search()
result_binary = binary_search.search()

# Print the results
print(f"Linear Search Result: {result_linear}")
print(f"Binary Search Result: {result_binary}")

# Example usage of MergeSort and BubbleSort
merge_sort = MergeSort([3, 1, 4, 5, 2])
bubble_sort = BubbleSort([3, 1, 4, 5, 2])

# Perform the sorting and get the sorted lists
sorted_merge = merge_sort._sort()
sorted_bubble = bubble_sort._sort()

# Print the sorted lists
print(f"Merge Sort Result: {sorted_merge}")
print(f"Bubble Sort Result: {sorted_bubble}")
```

## Contributors

### Sorting Algorithms
- MergeSort - Saral Agrawal
- BubbleSort - Sayan Karmakar

### Searching Algorithms
- LinearSearch - Amal Nair
- BinarySearch - Rajat Jacob

### Executable File and Plots
- Rajat Jacob
- Saral Agrawal

### Sanity Check | Debug
- Amal Nair
- Sayan Karmakar

