#!/usr/bin/env python3
"""BaseCache module with no limits"""

from base_caching import BaseCaching
from typing import Dict


class BasicCache(BaseCaching):
    """
    A basic cache implementation that inherits from BaseCaching.
    """

    def __init__(self):
        super().__init__()

    def put(self, key: str, item) -> None:
        """
        Add an item to the cache.

        Args:
            key (str): The key to associate with the item.
            item: The item to be added to the cache.

        Returns:
            None
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.
        """
        return super().get(key)
