from typing import List, Tuple

from src.model.types_and_stuff import Key, KeySet,  PCSet, all_keys, key_to_pcset

def calc_modulation(start_keyset, pcset) -> KeySet:
    possible_keys = calc_possible_keys(pcset)

    end_keyset = [key for key, _ in get_max_tupel(
            [
                (key, max(
                        map(lambda x: x[1], compare(start_keyset, key_to_pcset(key))) # For each key in possible_keys: Get the highest number of equal pitchclasses with any key in old_harmonic_state.
                    )) for key in possible_keys                                             
            ])
    ]

    return end_keyset


def calc_possible_keys(pcset: PCSet) -> List[Key]:
    """
    Input:
    - pcset: PCSet, a List of pitchclasses, where pitchclass is a int in range 0-11.

    Output:
    - List of keys: (pitchclass, mode), where pitchclass is a int in range 0-11 and mode is 'dur' or 'moll'.

    Calculates all possible keys for the given pcset and returns them as a list of keys. (1. in the algorithm from the paper)
    Possible keys are all keys, where a maximum of the pitchclasses of the pcset are in the key.
    (For tonal pcsets exists always a key, where all pitchclasses are in the key, for atonal pcsets there are no such keys.)
    
    Keep in mind that for minor keys the harmonic minor scale with the raised 7th degree is used.

    Example:
    calc_possible_keys([0, 2, 4]) -> [ #The Pitchclasses for C, D and E
        (0, 'dur'),
        (5, 'dur'),
        (7, 'dur'),
        (9, 'moll')
    ]
    calc_possible_keys([0, 1, 2]) -> [ #The Pitchclasses for C, Cis and D, which is an atonal pcset. Because of that the return value will be all keys that have not three (there do not exist such keys), but one less: two pitchclasses of the pcset in it, because there exist such keys.
        (0, 'dur'),
        (0, 'moll'),
        (1, 'dur'),
        (1, 'moll'),
        (2, 'dur'),
        (2, 'moll'),
        (3, 'dur'),
        (5, 'dur'),
        (5, 'moll'),
        (6, 'moll'),
        (7, 'dur'),
        (7, 'moll'),
        (8, 'dur'),
        (9, 'dur'),
        (9, 'moll'),
        (10, 'dur'),
        (10, 'moll'),
        (11, 'moll')
    ]
    """
    keys_with_value = compare(all_keys, pcset)
    return [key for key, _ in get_max_tupel(keys_with_value)]


def compare(keys: KeySet, pcset: PCSet) -> List[Tuple[Key, int]]:
    """
    Input:
    - keys: List of keys: (pitchclass, mode), where pitchclass is a int in range 0-11 and mode is 'dur' or 'moll'.
    - pcset: List of pitchclasses, where pitchclass is a int in range 0-11.

    Output:
    - List of tuples (key, int), where int is the number of equal pitch classes between the key and the given pcset (see calc_how_many_equal_pcs).

    Calculates for each key in the given list of keys the number of equal pitch classes with the given pcset.
    Then returns a list of tuples (key, int), where int is the number of equal pitch classes between the key and the given pcset.
    Keep in mind that for minor keys the harmonic minor scale with the raised 7th degree is used.

    Example:
    compare(
        [(0, 'dur'), (1, 'dur'), (2, 'dur'), (3, 'moll')], #C major, Cis major, D major, Dis major
        [0, 2, 4] #The Pitchclasses for C, D and E
    ) -> [
        ((0, 'dur'), 3),
        ((1, 'dur'), 1), # The pitch class 0 is in the key Cis major, but 2 and 4 are not.
        ((2, 'dur'), 2), # D major has D and E, but not C.
        ((3, 'moll'), 1) # Dis minor (or Es minor) has Pitchclass 2 (Cisis (or D)), but not C or E.
        ]
    """
    return [(key, calc_how_many_equal_pcs(key, pcset)) for key in keys]


# Function to calculate how many equal pitch classes a Key has with a PCSet
def calc_how_many_equal_pcs(key: Key, pcset: PCSet) -> int:
    """
    Input:
    - key: (pitchclass, mode), where pitchclass is a int in range 0-11 and mode is 'dur' or 'moll'.
    - pcset: List of pitchclasses, where pitchclass is a int in range 0-11.

    Output:
    - int. The number of equal pitch classes between key and pcset.

    Returns the number of equal pitch classes between the pitchclasses of a key and the given pcset.

    Example:
    calc_how_many_equal_pcs((0, 'dur'), [0, 2, 4]) -> 3 #Pitchclasses 0 (C), 2 (D) and 4 (E) are in the key C major.
    calc_how_many_equal_pcs((0, 'dur'), [1, 3, 5]) -> 1 #Pitchclass 5 (F) is in the key C major, but 1 (C#) and 3 (D#) are not.
    """
    return len(set(key_to_pcset(key)).intersection(pcset))


def get_max_tupel(tupel_list: List[Tuple[Key, int]]) -> List[Tuple[Key, int]]:
    """
    Input:
    - tupel_list: List of tuples (key, quantity), where quantity is an int.
    
    Output:
    - List of tuples (key, quantity) of all the given tuples, of which quantity has the maximum value. If there are multiple tuples with the same maximum value, all of them are returned.

    Returns the maximum tuples from a list of tuples of Key and int. 'Maximum' is based on the int value of the tuple.

    Example:
    get_max_tupel([((0, 'dur'), 1), ((1, 'dur'), 2), ((2, 'dur'), 2), ((3, 'dur'), 1)]) -> [((1, 'dur'), 2), ((2, 'dur'), 2)]
    """
    max_quantity = max(map(lambda x: x[1], tupel_list))
    return [(key, quantity) for key, quantity in tupel_list if quantity == max_quantity]