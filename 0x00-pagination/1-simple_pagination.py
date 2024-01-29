import csv
import math
from typing import List, Tuple


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
