#!/usr/bin/env python3
"""
hypermedia_pagination
"""
import csv
import math
from typing import List, Tuple


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        Return a tuple of size two containing a start index and an end index.
        """
        end = page * page_size
        start = (page - 1) * page_size
        return (start, end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get the dataset page for the given page number and page size.
        """
        dataset = self.dataset()
        start, end = self.index_range(page, page_size)
        if end > len(dataset):
            return []
        return [list(dataset[row]) for row in range(start, end)]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Get pagination information for the given page number and page size.
        """
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        current_page = page
        next_page = current_page + 1 if current_page < total_pages else None
        prev_page = current_page - 1 if current_page > 1 else None

        page_data = self.get_page(page, page_size)

        return {
            "page_size": len(page_data),
            "page": current_page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }


# Usage example
server = Server()

# Get page 2 with page size 5
page_data = server.get_page(2, 5)
print(page_data)

# Get pagination information for page 2 with page size 5
hyper_info = server.get_hyper(2, 5)
print(hyper_info)
