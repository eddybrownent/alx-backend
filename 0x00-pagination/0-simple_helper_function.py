#!/usr/bin/env python3
"""
Script that Calculates start and & indx for pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start & end indx for pagination

    Args:
        page: current page number
        page_size: number of items per page

    Returns:
        tuple: tuple containing start and end indices
    """
    # page num to 0-indexed (page - 1)
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
