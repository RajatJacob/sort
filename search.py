
from abc import ABC, abstractmethod
import time
"""Module with the base implementation of a Sort class."""


class Search(ABC):
    """Abstract base class for searching."""

    def __init__(self, items, target):

        self._items = list(items)
        self._target = target
        self.time = None

    @abstractmethod
    def _search(self):
        """ Returns the index of the element to be searched
        Returns:
                The index of the element to be searched or -1 if not found
        """
        pass

    def get_items(self):
        return self._items

    def get_target(self):
        return self._target

    def _time(self):
        return self.time

    def search(self):
        start_time = time.time()
        out = self._search()
        self.time = time.time() - start_time
        return out


class BinarySearch(Search):

    def __init__(self, items, target):
        super().__init__(list(sorted(items)), target)

    def _search(self):
        i = self._items
        a = 0
        b = len(i) - 1
        while a <= b:
            mid = (a + b) // 2
            if i[mid] < self._target:
                a = mid + 1
            elif i[mid] > self._target:
                b = mid - 1
            else:
                return mid
        return -1


class LinSearch(Search):
    def _search(self):
        """
        Perform linear search to find the index of the target in the list.

        Returns:
            int: The index of the target element, or -1 if not found.
        """
        try:
            items = self.get_items()  # Get the list of items to search within
            target = self.get_target()  # Get the target value to search for
            for i in range(len(items)):
                if items[i] == target:  # Check if the current item matches the target
                    return i  # Return the index if found
            return -1  # Return -1 if the target is not found

        except TypeError:
            # Handle the case where items is not a list or target is not a comparable value
            raise TypeError(
                "Items should be a list, and target should be a comparable value.")

        except Exception as e:
            # Handle other exceptions by re-raising them for further investigation
            raise e
