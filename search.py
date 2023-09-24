
from abc import ABC, abstractmethod

"""Module with the base implementation of a Sort class."""


class Search(ABC):
    """Abstract base class for searching."""

    def __init__(self, items, target):
        self._items = items
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
