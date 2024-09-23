from typing import List

from src.model.types_and_stuff import PCSet, KeySet, key_to_pcset
from calc_modulation import calc_modulation

class Modulation:
	def __init__(self, start_keyset, pcset):
		self.start_keyset = start_keyset 
		self.pcset = pcset
		self.end_keyset = calc_modulation(self.start_keyset, self.pcset)
		self.foreign_pitches = self.calc_foreign_pitches(self.start_keyset, self.pcset)

	# information_functions

	def calc_foreign_pitches(self, start_keyset, pcset) -> List[PCSet]:
		"""
		Only implemented for simple modulations: One key to one key.
		"""
		if len(start_keyset) != 1:
			return None
		return [p for p in pcset if p not in key_to_pcset(start_keyset[0]) and p in key_to_pcset(self.end_keyset[0])]