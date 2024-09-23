from src.model.types_and_stuff import is_atonal
from src.model.pcsets import is_reduced

class PCSetClass:
    def __init__(self, pcset, pcset_name = None):
        self.pcset = pcset
        self.pcset_size = len(pcset)
        self.pcset_name = pcset_name
        self.is_atonal = is_atonal(pcset)
        self.is_reduced = is_reduced(pcset)