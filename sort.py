from abc import ABC, abstractmethod

"""Module with the base implementation of a Sort class."""

class Sort(ABC):
    """Abstract base class for sorting."""

    def __init__(self, items):
        self._items = items

    @abstractmethod
    def _sort(self):
        """Returns the sorted version of the elements contained
        in the `_items` property.
        Returns:
            List: The sorted elements.
        """
        pass
#hello testing how to make changes and get them to reflect 
    def get_items(self):
        return self._items

    def _time(self):
        self.time = 0
        return self.time
    
    
    class MergeSort(Sort):
    """Class that represents a MergeSort implementation."""

    def _sort(self):
    # Check if the length of the list is greater than 1 (base case for recursion)
    if len(self._items) > 1:
        # Calculate the midpoint of the list
        mid = len(self._items) // 2

        # Divide the list into two halves: L and R
        L = self._items[:mid]
        R = self._items[mid:]

        # Create instances of MergeSort for left and right halves
        left_sort = MergeSort(L)
        left_sort._sort()  # Recursively sort the left half
        right_sort = MergeSort(R)
        right_sort._sort()  # Recursively sort the right half

        # Merge the two sorted halves back into the original list
        self._merge(L, R)

    # Return the sorted list
    return self._items


def _merge(self, left, right):
    i = j = k = 0

    # Merge the two halves (left and right) into a single sorted list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            self._items[k] = left[i]
            i += 1
        else:
            self._items[k] = right[j]
            j += 1
        k += 1

    # Check for any remaining elements in L and R
    while i < len(left):
        self._items[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        self._items[k] = right[j]
        j += 1
        k += 1


def _time(self):
    # Measure the execution time of the sorting process
    start = time.time()  # Record the start time
    self._sort()         # Call the sorting algorithm
    end = time.time()    # Record the end time
    self.time = end - start  # Calculate and store the elapsed time
    return self.time
