#!/usr/bin/env python3
"""defines a class and a function"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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
        Return a paginated subset of the dataset.

        Parameters:
        - page (int): The page number to retrieve. Default is 1.
        - page_size (int): The number of items per page. Default is 10.

        Returns:
        - List[List]: A list of lists representing the paginated
        subset of the dataset.

        Raises:
        - AssertionError: If the page or page_size is not a positive integer.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        dataset = self.dataset()
        try:
            index = index_range(page, page_size)
            return dataset[index[0]:index[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Return a dictionary containing the following key-value pairs:
        - page_size: the length of the returned dataset page
        - page: the current page number
        - data: the dataset page (equivalent to return from previous task)
        - next_page: number of the next page, None if no next page
        - prev_page: number of the previous page, None if no previous page
        - total_pages: the total number of pages in the dataset as an integer
        """
        dataset = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            'page_size': len(dataset),
            'page': page,
            'data': dataset,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
