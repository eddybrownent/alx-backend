#!/usr/bin/env python3
"""
Script has a class that impliments fifo in the cache
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    inherits from BaseCaching & is a caching system
    """
    def __init__(self):
        """
        Initialize the FIFOCache object and call the parent class constructor
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds items to the cache using FIFO

        Args:
            key: key for the item
            item: item value to be stored

        Returns:
                None
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            dis_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", dis_key)

        self.cache_data[key] = item

    def get(self, key):
        """
        gets an item from the cache

        Args:
            key: key to look for in the cache

        Returns:
            value of the key if exists else None
        """
        if key is not None and key in self.cache_dat:
            return self.cache_data[key]
        return None
