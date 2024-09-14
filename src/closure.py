from types_and_stuff import show_key_set, all_keys, all_pcsets
from calc_modulation import calc_modulation

def calc_key_set_closure(pcsets, root_key_sets):
        
    already_reached = set()

    start_key_sets = root_key_sets

    depth = -1

    i = 0

    while i > depth and start_key_sets: 
        i += 1

        new_key_sets = []
        print("Depth: ", i)
        for k in start_key_sets:
            for p in pcsets:
                end_k = calc_modulation(k, p)
                #print(show_key_set(k), show_key_set(end_k), p)
                end_k_tuple = tuple(end_k)
                #print(end_k_tuple)

                if end_k_tuple not in already_reached:
                    new_key_sets.append(end_k)
                    already_reached.add(end_k_tuple)

        start_key_sets = new_key_sets
        print("Number of new key sets: ", len(new_key_sets))

    reached_key_sets = list(already_reached)

    with open("less-than-7-and-keys_closure_allKeys-root.txt", "w") as file:
        for i in range(1,25):
            for key_set in reached_key_sets:
                if len(key_set) == i:
                    file.write(show_key_set(key_set) + "\n")

if __name__ == "__main__":
    pcsets = [pcset for pcset in all_pcsets if len(pcset) <=6]
    #pcsets = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11]]
    #root_key_sets = [[(0, 'dur')]]
    root_key_sets = [all_keys]

    calc_key_set_closure(pcsets, root_key_sets)
	