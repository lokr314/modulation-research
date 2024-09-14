from src.types_and_stuff import powerset, is_atonal, deserialize_key_set

def test_powerset():
    assert powerset([1, 2, 3]) == [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert powerset([1, 2, 3, 4]) == [[1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]


def test_is_atonal():
    assert is_atonal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == True
    assert is_atonal([0, 1, 2]) == True
    assert is_atonal([0, 2, 4]) == False
    assert is_atonal([0]) == False

def test_deserialize_key_set():
    assert deserialize_key_set("[C, Cis, Cism, Bm, Bbm]") == [(0, 'dur'), (1, 'dur'), (1, 'moll'), (11, 'moll'), (10, 'moll')]
    assert deserialize_key_set("[]") == []
    assert deserialize_key_set("[C]") == [(0, 'dur')]
    assert deserialize_key_set("[C, Cm, Cis, Cism, D, Dm, Es, Esm, E, Em, F, Fm, Fis, Fism, G, Gm, As, Asm, A, Am, Bb, Bbm, B, Bm]") == [(0, 'dur'), (0, 'moll'), (1, 'dur'), (1, 'moll'), (2, 'dur'), (2, 'moll'), (3, 'dur'), (3, 'moll'), (4, 'dur'), (4, 'moll'), (5, 'dur'), (5, 'moll'), (6, 'dur'), (6, 'moll'), (7, 'dur'), (7, 'moll'), (8, 'dur'), (8, 'moll'), (9, 'dur'), (9, 'moll'), (10, 'dur'), (10, 'moll'), (11, 'dur'), (11, 'moll')]