#!/usr/bin/env python3
"""Defines LIFOCache class"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A Last-In-First-Out (LIFO) cache implementation.

    Inherits from the BaseCaching class and provides methods
    for putting items into the cache
    and retrieving items from the cache.

    Attributes:
        order (list): A list that keeps track of the order
        in which items are added to the cache.

    Methods:
        put(key, item): Adds an item to the cache with
        the specified key.
        get(key): Retrieves the item associated with the
        specified key from the cache.

    """

    def __init__(self):
        """
        Initializes a new instance of the LIFOCache class.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key of the item.
            item: The item to be added to the cache.
        """
        length = len(self.cache_data)
        if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            print("DISCARD: {}".format(self.order[-1]))
            del self.cache_data[self.order[-1]]
            del self.order[-1]
        self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve item from cache
        """
        return super().get(key)
