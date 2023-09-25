
from abc import ABC, abstractmethod
import time
import numpy as np
import matplotlib.pyplot as plt

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


if __name__ == '__main__':
    assert LinSearch([3, 1, 4, 5, 9], 4).search() == 2
    assert BinarySearch([3, 1, 4, 5, 9], 4).search() == 2
    assert LinSearch([3, 1, 4, 5, 9], 6).search() == -1
    assert BinarySearch([3, 1, 4, 5, 9], 6).search() == -1
    print("All test cases passed.")
    print("Plotting... (this might take a while)")
    x = range(1, int(1e4), 50)
    bt = []
    lt = []
    for i in x:
        ba = []
        la = []
        for j in range(50):
            a = np.random.randint(0, i*1000, i)
            target = np.random.choice(a)
            b = BinarySearch(a, target)
            b.search()
            ba.append(b._time())
            li = LinSearch(a, target)
            li.search()
            la.append(li._time())
        bt.append(sum(ba)/len(ba))
        lt.append(sum(la)/len(la))
    plt.plot(x, lt, label='Linear')
    plt.plot(x, bt, label='Binary')
    plt.legend()
    plt.show()
