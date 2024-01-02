#!/usr/bin/env python3
"""
This script adds an item to the cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    caching system that inherits from BaseCaching class
    """
    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: key for the item.
            item: item value to be stored in the cache

        Returns:
            None
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        retrives an item from the cache

        Args:
            key: key to check in the cache

        Returns:
            value of the key if it exits else None
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
