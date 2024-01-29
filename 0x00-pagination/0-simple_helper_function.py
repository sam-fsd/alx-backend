#!/usr/bin/env python3
"""defines a function"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Return the start and end indices for a given
    page and page size.

    Parameters:
    - page (int): The page number.
    - page_size (int): The number of items per page.

    Returns:
    - tuple[int, int]: A tuple containing the start and end
    indices for the given page.
"""
    start_idx = (page - 1) * page_size
    end_idx = page * page_size

    return (start_idx, end_idx)
