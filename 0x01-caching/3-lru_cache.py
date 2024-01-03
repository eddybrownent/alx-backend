#!/usr/bin/env python3
"""
script that implements LRU in caching system
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        Intialize LRUCache object & call parent of class constructor
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to cache using LRU

    `   Args:
            key: the key to look for
            item: value to be stored in cache

        Returns:
                None
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                dis_key, _ = self.cache_data.popitem(last=True)
                print("DISCARD:", dis_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache

        Args:
            key: key to look for in the cache

        Returns:
            The value of the key if it exists, else returns None
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data[key]
        return None
