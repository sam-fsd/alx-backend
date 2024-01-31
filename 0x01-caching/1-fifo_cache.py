#!/usr/bin/env python3
"""Defines a class implemeting FIFO
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    First-In-First-Out (FIFO) Cache implementation.

    Inherits from the BaseCaching class.

    Attributes:
        cache_data (dict): Dictionary to store key-value pairs.
    """

    def __init__(self):
        """
        Initializes a FIFO cache object.
        """
        super().__init__()
        self.order = []

    def put(self, key=None, item=None):
        """
        Add an item to the cache.

        Args:
            key: The key of the item.
            item: The item to be added.

        Returns:
            None
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve item from cache
        """
        return super().get(key)
