from src.model.types_and_stuff import KeySet as kset
from src.model.pcsets import is_reduced

class KeySetClass:
    def __init__(self, keyset: kset):
        self.keyset = keyset
        self.keyset_size = len(keyset)
        self.is_simple = self.keyset_size == 1
        self.shortest_path_length = None
        self.shortest_path_example = None