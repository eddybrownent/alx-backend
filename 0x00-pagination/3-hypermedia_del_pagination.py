#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get hypermedia info for the DB using provided start index & page size

        Args:
            index : current start index of return page. Defaults to None
            page_size : number of items per page. Defaults to 10

        Returns:
            dict: A dictionary containing hypermedia information
        """
        assert index is None or (isinstance(index, int) and index >= 0)
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        total_items = len(dataset)

        if index is not None:
            assert index < total_items

        start_index = index if index is not None else 0
        end_index = start_index + page_size

        next_index = min(end_index, total_items)

        # Adjust end_index based on the dataset size
        end_index = min(end_index, total_items)

        # Return the paginated dataset for the given range
        data = dataset[start_index:end_index]

        return {
            'index': start_index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
