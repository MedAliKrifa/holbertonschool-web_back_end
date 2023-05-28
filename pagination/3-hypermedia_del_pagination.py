#!/usr/bin/env python3
"""
hypermedia_pagination
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
        Get pagination information based on the given index and page size.
        """
        dataset = self.dataset()
        total_rows = len(dataset)
        last_index = total_rows - 1

        # Verify that the index is within a valid range
        assert index is None or 0 <= index <= last_index, "Invalid index."

        # Calculate the current start index
        start_index = 0 if index is None else index

        # Calculate the next index to query
        next_index = min(start_index + page_size, total_rows)

        # Retrieve the data for the current page
        data = dataset[start_index:next_index]

        return {
            "index": start_index,
            "next_index": next_index if next_index <= last_index else None,
            "page_size": len(data),
            "data": data
        }
