from typing import List

from types_and_stuff import PCSet, all_single_key_sets, all_pcsets, key_to_pcset, show_key_set, is_atonal
from calc_modulation import calc_modulation

class Modulation:
	def __init__(self, start_key_set, pcset):
		self.start_key_set = start_key_set 
		self.pcset = pcset
		self.end_key_set = calc_modulation(self.start_key_set, self.pcset)
		self.foreign_pitches = self.calc_foreign_pitches(self.start_key_set, self.pcset)

	# information_functions

	def calc_foreign_pitches(self, start_key_set, pcset) -> List[PCSet]:
		"""
		Only implemented for simple modulations: One key to one key.
		"""
		if len(start_key_set) != 1:
			return None
		return [p for p in pcset if p not in key_to_pcset(start_key_set[0]) and p in key_to_pcset(self.end_key_set[0])]


def build_modulations(pcsets, root_key_sets, constraints):
	"""
	pcsets: alle pcsets, die wir zur Generation verwenden
	root_key_sets: alle key_sets, von denen aus wir modulieren
	constraints: filter functions, die entstehende Modulationen behalten oder nicht.

	Diese Funktion berechnet alle entstehenden Modulationen. Bei jede Modulation ist ein Objekt aus Start und Zielkeyset, mit dem benutzten pcset. Hier werden dann auch weitere Informationen berechnet.
	"""
	
	result_list: Modulation = [] 

	for k in root_key_sets:
		for p in pcsets:
			m = Modulation(k, p)
			#print(show_key_set(m.start_key_set), show_key_set(m.end_key_set), str(m.pcset), str(m.foreign_pitches))

			# check constraints
			is_elegible = True
			for c in constraints:
				is_elegible = c(m) and is_elegible
				if not is_elegible:
					break
			if not is_elegible:
				continue

			result_list.append(m)

	# replace with database filling code.
	# Grouping
	for k in root_key_sets:
		for end_k in all_single_key_sets:
			if k == end_k:
				continue
			print(show_key_set(k) + "->" + show_key_set(end_k) + ":")
			for m in result_list:
				if m.start_key_set == k and m.end_key_set == end_k:
					# Printing
					print(
						#"Start:" + show_key_set(m.start_key_set) + 
						#", Ende:" + show_key_set(m.end_key_set) +
						"PCSet:" + str(m.pcset) +
						", modulierende Töne:" + str(m.foreign_pitches) 
					)
					result_list.remove(m)
			print("")

if __name__ == "__main__":
	pcsets = all_pcsets
	root_key_sets = [[(0, 'dur')], [(0, 'moll')]]
	#constraints = []
	constraints = [
		lambda m: len(m.end_key_set) == 1,
		lambda m: m.start_key_set != m.end_key_set,
		lambda m: is_atonal(m.pcset) == False]
	
	build_modulations(pcsets, root_key_sets, constraints)
	