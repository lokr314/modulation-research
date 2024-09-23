from src.model.types_and_stuff import PCSet, all_single_key_keysets, all_pcsets, key_to_pcset, show_keyset, is_atonal
from src.model.Modulation import Modulation


def build_modulations(pcsets, root_keysets, constraints):
	"""
	pcsets: alle pcsets, die wir zur Generation verwenden
	root_keysets: alle keysets, von denen aus wir modulieren
	constraints: filter functions, die entstehende Modulationen behalten oder nicht.

	Diese Funktion berechnet alle entstehenden Modulationen. Jede Modulation ist ein Objekt aus Start und Zielkeyset, mit dem benutzten pcset. Hier werden dann auch weitere Informationen berechnet.
	"""
	
	result_list: Modulation = [] 

	for k in root_keysets:
		for p in pcsets:
			m = Modulation(k, p)
			#print(show_keyset(m.start_keyset), show_keyset(m.end_keyset), str(m.pcset), str(m.foreign_pitches))

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
	for k in root_keysets:
		for end_k in all_single_key_keysets:
			if k == end_k:
				continue
			print(show_keyset(k) + "->" + show_keyset(end_k) + ":")
			for m in result_list:
				if m.start_keyset == k and m.end_keyset == end_k:
					# Printing
					print(
						#"Start:" + show_keyset(m.start_keyset) + 
						#", Ende:" + show_keyset(m.end_keyset) +
						str(m.pcset)# +
						#", modulierende Töne:" + str(m.foreign_pitches) 
					)
					result_list.remove(m)
			print("")

if __name__ == "__main__":
	pcsets = all_pcsets
	root_keysets = [[(0, 'dur')], [(0, 'moll')]]
	#constraints = []
	constraints = [
		lambda m: len(m.end_keyset) == 1,
		lambda m: m.start_keyset != m.end_keyset,
		lambda m: is_atonal(m.pcset) == False]
	
	build_modulations(pcsets, root_keysets, constraints)
	