from typing import List, Tuple
from itertools import chain, combinations

def powerset(iterable):
    """
    Input:
    - iterable: list of elements

    Output:
    A list of all possible subsets of the input iterable, excluding the empty set. 
    Each subset is returned as a list.

    Example:
    powerset([1, 2, 3]) -> [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    """
    s = list(iterable)
    return [list(subset) for subset in chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))]

#--- PC ------------------------------------------------------------------------

PC = int
all_pcs: List[PC] = list(range(12))

#--- PCSet ---------------------------------------------------------------------

PCSet = List[PC]
all_pcsets: List[PCSet] = [pcset for pcset in powerset(all_pcs)]
dur = [0, 2, 4, 5, 7, 9, 11]
moll = [0, 2, 3, 5, 7, 8, 11]

def transpose(n: int, pcset: PCSet) -> PCSet:
    return [(pc + n) % 12 for pc in pcset]

def is_atonal(pcset: PCSet) -> bool:
    for key in list(map(lambda key: key_to_pcset(key), all_keys)):
        if all(i in key for i in pcset):
            return False
    return True


def pcset_equal(pcset1, pcset2):
    """Returns True if pcset1 and pcset2 are equal, False otherwise.
    pcset1 and pcset2 are lists of pitch classes, e.g. [0, 4, 7]"""
    return sorted(pcset1) == sorted(pcset2)

#--- Key -----------------------------------------------------------------------

Key = Tuple[PC, str]
all_keys: List[Key] = [(n, mode) for n in range(12) for mode in ['dur', 'moll']]


def key_to_pcset(key: Key) -> PCSet:
    n, mode = key
    return transpose(n, dur) if mode == 'dur' else transpose(n, moll)

def show_key(key: Key) -> str:
    """
    Input:
    - key: tupel with two fields: pitchclass: int from 0-11 and mode: 'dur' or 'moll'

    Output:
    The Key as a string in the format 'C' for dur and 'Am' for moll. Fis and Es are used for sharp and flat keys.
    Bb is used for pitchclass 10, B for pitchclass 11.
    
    Example:
    (0, 'dur') -> 'C'
    (1, 'dur') -> 'Cis'
    (1, 'moll') -> 'Cism'
    (11, 'moll') -> 'Bm'
    (10, 'dur') -> 'Bb'
    """
    n, mode = key
    notes = ['C', 'Cis', 'D', 'Es', 'E', 'F', 'Fis', 'G', 'As', 'A', 'Bb', 'B']
    return notes[n] + ('' if mode == 'dur' else 'm')

def deserialize_key(key_str: str) -> tuple:
    """
    Deserializes a single key string back into a (pitchclass, mode) tuple.

    Example:
    'C' -> (0, 'dur')
    'Cis' -> (1, 'dur')
    'Cism' -> (1, 'moll')
    'Bm' -> (11, 'moll')
    'Bb' -> (10, 'dur')
    """
    notes_map = {
        'C': 0, 'Cis': 1, 'D': 2, 'Es': 3, 'E': 4, 'F': 5, 'Fis': 6,
        'G': 7, 'As': 8, 'A': 9, 'Bb': 10, 'B': 11
    }
    
    if key_str.endswith('m'):
        note = key_str[:-1]
        mode = 'moll'
    else:
        note = key_str
        mode = 'dur'

    pitchclass = notes_map[note]
    return (pitchclass, mode)

def keyset_equal(keyset1, keyset2):
    """Returns True if keyset1 and keyset2 are equal, False otherwise.
    keyset1 and keyset2 are lists of keys, e.g. [(0, 'dur'), (4, 'moll')]"""
    return sorted(keyset1) == sorted(keyset2)

tonal_and_up_to_6_pcs_pcsets: List[PCSet] = [pcset for pcset in all_pcsets if len(pcset) <= 6] + list(map(lambda key: key_to_pcset(key), all_keys))

#--- KeySet --------------------------------------------------------------------

KeySet = List[Key]
#all_harmonic_states: List[KeySet] = [hs for hs in powerset(all_keys) if len(hs) < 15] # This takes waaaaay to long
all_single_key_keysets: List[KeySet] = [[(n, mode)] for n in range(12) for mode in ['dur', 'moll']]

def show_keyset(keys: KeySet) -> str:
    if not keys:
        return "[]"
    return "[" + ", ".join([show_key(key) for key in keys]) + "]"
def show_keysets(keysets: List[KeySet]) -> str:
    return "".join([show_keyset(keyset) for keyset in keysets])

def deserialize_keyset(keyset_str: str) -> list:
    """
    Deserializes the string representation of a key set back into a list of (pitchclass, mode) tuples.
    
    Example:
    '[C, Cis, Cism, Bm]' -> [(0, 'dur'), (1, 'dur'), (1, 'moll'), (11, 'moll')]
    '[]' -> []
    """
    # Remove the square brackets and split by commas
    keyset_str = keyset_str.strip("[]").strip()
    
    if not keyset_str:
        return []
    
    # Split the string into individual keys
    key_strings = [key.strip() for key in keyset_str.split(",")]
    
    # Deserialize each key string
    return [deserialize_key(key_str) for key_str in key_strings]















