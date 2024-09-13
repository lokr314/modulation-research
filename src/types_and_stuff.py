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

PC = int
all_pcs: List[PC] = list(range(12))

PCSet = List[PC]
all_pcsets: List[PCSet] = [pcset for pcset in powerset(all_pcs)]

Key = Tuple[PC, str]
all_keys: List[Key] = [(n, mode) for n in range(12) for mode in ['dur', 'moll']]

KeySet = List[Key]
#all_harmonic_states: List[KeySet] = [hs for hs in powerset(all_keys) if len(hs) < 15] # This takes waaaaay to long
all_single_key_sets: List[KeySet] = [[(n, mode)] for n in range(12) for mode in ['dur', 'moll']]

dur = [0, 2, 4, 5, 7, 9, 11]
moll = [0, 2, 3, 5, 7, 8, 11]


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

def show_key_set(keys: KeySet) -> str:
    if not keys:
        return "[]"
    return "[" + ", ".join([show_key(key) for key in keys]) + "]"

def show_key_sets(states: List[KeySet]) -> str:
    return "".join([show_key_set(state) for state in states])


def pcset_equal(pcset1, pcset2):
    """Returns True if pcset1 and pcset2 are equal, False otherwise.
    pcset1 and pcset2 are lists of pitch classes, e.g. [0, 4, 7]"""
    return sorted(pcset1) == sorted(pcset2)

def key_set_equal(key_set1, key_set2):
    """Returns True if key_set1 and key_set2 are equal, False otherwise.
    key_set1 and key_set2 are lists of keys, e.g. [(0, 'dur'), (4, 'moll')]"""
    return sorted(key_set1) == sorted(key_set2)


def key_to_pcset(key: Key) -> PCSet:
    n, mode = key
    return transpose(n, dur) if mode == 'dur' else transpose(n, moll)

def transpose(n: int, pcset: PCSet) -> PCSet:
    return [(pc + n) % 12 for pc in pcset]

def is_atonal(pcset: PCSet) -> bool:
    for key in list(map(lambda key: key_to_pcset(key), all_keys)):
        if all(i in key for i in pcset):
            return False
    return True