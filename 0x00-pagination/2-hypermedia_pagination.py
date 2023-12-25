#!/usr/bin/env python3
"""
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start & end indx for pagination

    Args:
        page: current page number
        page_size: number of items per page

    Returns:
        tuple: tuple containing the start & end indx
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of the dataset using provided page number & page size

        Args:
            page: current page number
            page_size: number of items per page

        Returns:
            List: paginated dataset for the given page and page size
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        # Return the paginated dataset for the given range
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Gets hypermedia info for db based using provided page num & page size

        Args:
            page (int): The current page number (1-indexed)
            page_size (int): The number of items per page.

        Returns:
        - dict: A dictionary containing hypermedia information.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        current_page = page
        next_page = current_page + 1 if end_index <= total_pages else None
        prev_page = current_page - 1 if start_index > 0 else None

        return {
            'page_size': len(self.get_page(page, page_size)),
            'page': current_page,
            'data': self.get_page(page, page_size),
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
