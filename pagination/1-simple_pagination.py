#!/usr/bin/env python3
"""
Simple helper function
"""


import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Returns the start and end indices for a given page and page size.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start and end indices.

    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        """Return dataset for the given page and page size."""
        assert isinstance(page, int) and page >= 1
        assert isinstance(page_size, int) and page_size >= 1

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        dataset_max_range = len(dataset)
        if start_index >= dataset_max_range:
            return []
        return dataset[start_index: end_index]
