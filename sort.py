from abc import ABC, abstractmethod

import time
import random
import matplotlib.pyplot as plt

"""Module with the base implementation of a Sort class."""


class Sort(ABC):
    """Abstract base class for sorting."""
    def __init__(self, items):
            try:
                self._items = list(items)
            except TypeError as e:
                print("There is some error.Enter only an iterable list")  
    @abstractmethod
    def _sort(self):
        """Returns the sorted version of the elements contained
        in the `_items` property.
        Returns:
            List: The sorted elements.
        """
        pass

    def get_items(self):
        return self._items

    def _time(self):
        self.time = 0
        return self.time


class MergeSort(Sort):
    """Class that represents a MergeSort implementation."""

    def _sort(self):
        try:
            #length of the list is greater than 1 (base case for recursion)
            if len(self._items) > 1:
                # Calculate the midpoint of the list
                mid = len(self._items) // 2

                # Divide the list into two halves: L and R
                L = self._items[:mid]
                R = self._items[mid:]

                # Creating instances of MergeSort for left and right halves
                left_sort = MergeSort(L)
                left_sort._sort()         # Recursively sort the right half
                right_sort = MergeSort(R)
                right_sort._sort()  # Recursively sort the right half

                # Merge the two sorted halves back into the original list
                self._merge(left_sort._items,right_sort._items)
                # Return the sorted list
                return self._items
        except RecursionError as e:
            # Handle recursion depth exceeded error
            print("Recursion depth exceeded. Consider using a shorter array")
        except TypeError as e:
            # Handle type error
            print("Input list is of incompatible type.")
        except IndexError as e:
            # Handle index error
            print("Index error. Check list indices.")
        except Exception as e:
            # Handle other exceptions
            print(f"An unexpected error occurred: {str(e)}")

    def _merge(self, left, right):
        i = j = k = 0

        try:
            # Merge the two halves (left and right) into a single sorted list
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    self._items[k] = left[i]
                    i += 1
                else:
                    self._items[k] = right[j]
                    j += 1
                k += 1

            # Check for any remaining elements in left and right
            while i < len(left):
                self._items[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                self._items[k] = right[j]
                j += 1
                k += 1

        except IndexError as e:
            # Handle index error
            print("Index error. Check list indices.")
        except TypeError as e:
            # Handle type error
            print("Input lists contain incompatible elements.")
        except Exception as e:
            # Handle other unexpected exceptions

"""Module with the base implementation of a Sort class."""

class BubbleSort(Sort):
    """Class that represents a BubbleSort implementation."""

    def _sort(self):
        try:
            n = len(self._items)
            for i in range(n):
                swap=0
                for j in range(0, n - i - 1):
                    if self._items[j] > self._items[j + 1]:
                        self._items[j], self._items[j + 1] = self._items[j + 1], self._items[j]
                        swap+=1
                if swap==0:
                    break
            return self._items            
        
        except IndexError as e:
            # handles Index Error
            print("IndexError: Check List Indices")
        except TypeError as e:
            # handles Type Error
            print("Input list is of incompatible type.")
        except Exception as e:
            # handles other unexpected Exceptions

            print(f"An unexpected error occurred: {str(e)}")

    def _time(self):
        try:

            # Measure the execution time of the sorting process
            start = time.time()  # Record the start time
            self._sort()         # Call the sorting algorithm
            end = time.time()    # Record the end time
            self.time = end - start  # Calculate and store the elapsed time
            return self.time
        except TypeError as e:
            # Handle type error
            print("Sorting algorithm encountered a TypeError.")
        except Exception as e:
            # Handle other unexpected exceptions
            print(f"An unexpected error occurred: {str(e)}")


# Main code for performance comparison

if __name__ == "__main__":
        merge_sort_times = []
        bubble_sort_times = []
        input_sizes = [100, 200, 500, 1000, 5000, 10000]

        for size in input_sizes:
          # Generate a random list of numbers between 1 and the input size
          random_list = [random.randint(1, size) for _ in range(size)]

          # Create instances of MergeSort and BubbleSort
          merge_sort_instance = MergeSort(random_list.copy())
          bubble_sort_instance = BubbleSort(random_list.copy())

          # Measure the execution times and store them
          merge_sort_time = merge_sort_instance._time()
          bubble_sort_time = bubble_sort_instance._time()

          merge_sort_times.append(merge_sort_time)
          bubble_sort_times.append(bubble_sort_time)

          print(f"Input size: {size}")
          print(f"Merge Sort Execution Time: {merge_sort_time} seconds")
          print(f"Bubble Sort Execution Time: {bubble_sort_time} seconds")
          print("-" * 40)

      # Plot the execution times for both algorithms
      plt.plot(input_sizes, merge_sort_times, label="Merge Sort")
      plt.plot(input_sizes, bubble_sort_times, label="Bubble Sort")
      plt.xlabel("Input Size")
      plt.ylabel("Execution Time (seconds)")
      plt.title("Sorting Algorithm Performance Comparison")
      plt.legend()
      plt.grid(True)

      # Show the plot
      plt.show()
