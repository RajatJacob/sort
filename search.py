
from abc import ABC, abstractmethod

"""Module with the base implementation of a Sort class."""


class Search(ABC):
    """Abstract base class for searching."""

    def __init__(self, items, target):
        try:
            self._items = list(items)
        except TypeError:
            raise TypeError(
                f"""Please provide an iterable. Received value of type <{type(
                    items
                ).__name__}>!"""
            )
        self._target = target

    @abstractmethod
    def _search(self):
        """Returns the index of the element to be searched
        Returns:
                The index of the element to be searched or -1 if not found
        """
        pass

    def get_items(self):
        return self._items

    def get_target(self):
        return self._target

    def _time(self):
        self.time = 0
        return self.time


class BinarySearch(Search):

    def _search(self):
        i = list(sorted(self._items))
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
