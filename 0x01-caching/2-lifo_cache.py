#!/usr/bin/env python3
"""
Script that impliments LIFO in caching system
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        intializes LIFOcache object & call parent class constructor
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache using LIFO

        Args:
            key: key for the item
            item: item value to be stored in cache

        Returns:
            None
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                dis_key, _ = self.cache_data.popitem()
                print("DISCARD:", dis_key)

        self.cache_data[key] = item

        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        retrives an item from the cache

        Args:
            key: key to look for in the cache

        Returns:
                value of the key if it exists else returns None
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
