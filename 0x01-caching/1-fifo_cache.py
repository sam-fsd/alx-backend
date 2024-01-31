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

    def put(self, key=None, item=None):
        """
        Add an item to the cache.

        Args:
            key: The key of the item.
            item: The item to be added.

        Returns:
            None
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first = list(self.cache_data.keys())[0]
                del self.cache_data[first]
                print("DISCARD: {}".format(first))

    def get(self, key):
        """ Retrieve item from cache
        """
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        return None
