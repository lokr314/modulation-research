from src.model.types_and_stuff import show_keyset, all_keys, all_pcsets
from calc_modulation import calc_modulation

def calc_keyset_closure(pcsets, root_keysets):
        
    already_reached = set()

    start_keysets = root_keysets

    depth = -1

    i = 0

    while i > depth and start_keysets: 
        i += 1

        new_keysets = []
        print("Depth: ", i)
        for k in start_keysets:
            for p in pcsets:
                end_k = calc_modulation(k, p)
                #print(show_keyset(k), show_keyset(end_k), p)
                end_k_tuple = tuple(end_k)
                #print(end_k_tuple)

                if end_k_tuple not in already_reached:
                    new_keysets.append(end_k)
                    already_reached.add(end_k_tuple)

        start_keysets = new_keysets
        print("Number of new key sets: ", len(new_keysets))

    reached_keysets = list(already_reached)

    with open("less-than-7-and-keys_closure_allKeys-root.txt", "w") as file:
        for i in range(1,25):
            for keyset in reached_keysets:
                if len(keyset) == i:
                    file.write(show_keyset(keyset) + "\n")

if __name__ == "__main__":
    pcsets = [pcset for pcset in all_pcsets if len(pcset) <=6]
    #pcsets = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11]]
    #root_keysets = [[(0, 'dur')]]
    root_keysets = [all_keys]

    calc_keyset_closure(pcsets, root_keysets)
	