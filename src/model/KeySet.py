from src.model.types_and_stuff import KeySet as kset
from src.model.pcsets import is_reduced

class KeySet:
    def __init__(self, keyset: kset):
        self.keyset = keyset
        self.keyset_size = len(keyset)