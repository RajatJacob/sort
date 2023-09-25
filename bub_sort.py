from abc import ABC, abstractmethod
from datetime import time              #import Datetime

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
            # To measure the execution time of the sorting process
            start = time.time()  #  read start time
            self._sort()         # calling sort function from BubbleSort 
            end = time.time()    #  read end time 
            self.time = end - start  # calculate and store the elapsed time
            return self.time
        except TypeError as e:
            # handles type error
            print("Sorting algorithm encountered a TypeError.")
        except Exception as e:
            # handles other unexpected Exceptions
            print(f"An unexpected error occurred: {str(e)}")


