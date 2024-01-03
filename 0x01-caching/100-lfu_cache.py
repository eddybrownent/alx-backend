#!/usr/bin/env python3
"""
This script implements LFU in a caching system
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        Initialize LFUCache object & call parent class constructor
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.key_frequencies = []

    def __recorder(self, recently_used_key):
        """
        Records the items in the cache based on most recently used key
        """
        max_freq_pos = []
        recently_used_frequency = 0
        recently_used_position = 0
        insert_position = 0

        for i, key_freq_pair in enumerate(self.key_frequencies):
            if key_freq_pair[0] == recently_used_key:
                recently_used_frequency = key_freq_pair[1] + 1
                recently_used_position = i
                break
            elif len(max_freq_pos) == 0:
                max_freq_pos.append(i)
            elif key_freq_pair[1] < self.key_frequencies[max_freq_pos[-1]][1]:
                max_freq_pos.append(i)

        max_freq_pos.reverse()

        for position in max_freq_pos:
            if self.key_frequencies[position][1] > recently_used_frequency:
                break
            insert_position = position

        self.key_frequencies.pop(recently_used_position)
        self.key_frequencies.insert(insert_position, [recently_used_key,
                                                      recently_used_frequency])

    def put(self, key, item):
        """
        Add an item to the cache using the LFU algorithm

        Args:
            key: key for the item
            item: item value to be stored in the cache

        Returns:
            None
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                dis_key, _ = self.key_frequencies[-1]
                self.cache_data.pop(dis_key)
                self.key_frequencies.pop()
                print("DISCARD:", dis_key)
            self.cache_data[key] = item
            insert_index = len(self.key_frequencies)
            for i, key_frequency in enumerate(self.key_frequencies):
                if key_frequency[1] == 0:
                    insert_index = i
                    break
            self.key_frequencies.insert(insert_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__recorder(key)

    def get(self, key):
        """
        Retrieve an item from the cache

        Args:
            key: key to look for in the cache

        Returns:
                value of the key if it exists, else returns None
        """
        if key is not None and key in self.cache_data:
            self.__recorder(key)
            return self.cache_data[key]
        return None
