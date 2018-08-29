import os
import sortedcollections


class DiskIndex(object):
    def __init__(self, root_directory="."):
        self.root_directory = root_directory
        os.makedirs(root_directory, exist_ok=True)

    def update_item_index(self, items):
        self._fetch_if_exists()