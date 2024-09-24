from typing import List

from src.database import insert_pcset, select_pcset, get_connection, insert_pcsets, bitstring_to_keyset, keyset_to_bitstring, bitstring_to_pcset, pcset_to_bitstring
from src.model.PCSet import PCSetClass
from src.model.types_and_stuff import tonal_and_up_to_6_pcs_pcsets, Key


# def test_insert_and_select_pcset():
#     """
#     requires this the pcset [0,1,2,3,4,5,6,7,8,9,10,11] not to be in the database.
#     """
#     pcset = [0,1,2,3,4,5,6,7,8,9,10,11]
#     pcset = PCSetClass(pcset)
#     insert_pcset(pcset)
    
#     pcset = select_pcset([0,1,2,3,4,5,6,7,8,9,10,11])
#     assert pcset == [0,1,2,3,4,5,6,7,8,9,10,11]

#     conn = get_connection()
#     with conn, conn.cursor() as cursor:
#         cursor.execute("DELETE FROM pcsets WHERE pcset = B'111111111111';")


# def test_insert_pcsets():
#     print(len(tonal_and_up_to_6_pcs_pcsets))
#     insert_pcsets([PCSetClass(pcset) for pcset in tonal_and_up_to_6_pcs_pcsets])
#     conn = get_connection()	
#     with conn, conn.cursor() as cursor:
#         cursor.execute("SELECT * FROM pcsets")
#         pcsets = cursor.fetchall()
#         assert len(pcsets) == len(tonal_and_up_to_6_pcs_pcsets)
#     with conn, conn.cursor() as cursor:
#        cursor.execute("DELETE FROM pcsets")
        
def test_pcset_to_bitstring():
    pcset = [0,1,2,3,4,5,6,7,8,9,10,11]
    assert pcset_to_bitstring(pcset) == 0b111111111111
    pcset = [0]
    assert pcset_to_bitstring(pcset) == 0b100000000000
    pcset = []
    assert pcset_to_bitstring(pcset) == 0b000000000000

def test_bitstring_to_pcset():
    assert bitstring_to_pcset('111111111111') == [0,1,2,3,4,5,6,7,8,9,10,11]
    assert bitstring_to_pcset('100000000000') == [0]
    assert bitstring_to_pcset('000000000000') == []
    assert bitstring_to_pcset('000000000001') == [11]

def test_keyset_to_bitstring():
    keyset = [(0, 'dur'), (0, 'moll')]
    assert keyset_to_bitstring(keyset) == 0b110000000000000000000000
    keyset = [(0, 'dur'), (0, 'moll'), (1, 'dur'), (1, 'moll'), (2, 'dur'), (2, 'moll'), (3, 'dur'), (3, 'moll'), (4, 'dur'), (4, 'moll'), (5, 'dur'), (5, 'moll'), (6, 'dur'), (6, 'moll'), (7, 'dur'), (7, 'moll'), (8, 'dur'), (8, 'moll'), (9, 'dur'), (9, 'moll'), (10, 'dur'), (10, 'moll'), (11, 'dur'), (11, 'moll')]
    assert keyset_to_bitstring(keyset) == 0b111111111111111111111111

def test_bitstring_to_keyset():
    assert bitstring_to_keyset('000000000000000000000000') == []
    assert bitstring_to_keyset('110000000000000000000000') == [(0, 'dur'), (0, 'moll')]
    assert bitstring_to_keyset('111111111111111111111111') == [(0, 'dur'), (0, 'moll'), (1, 'dur'), (1, 'moll'), (2, 'dur'), (2, 'moll'), (3, 'dur'), (3, 'moll'), (4, 'dur'), (4, 'moll'), (5, 'dur'), (5, 'moll'), (6, 'dur'), (6, 'moll'), (7, 'dur'), (7, 'moll'), (8, 'dur'), (8, 'moll'), (9, 'dur'), (9, 'moll'), (10, 'dur'), (10, 'moll'), (11, 'dur'), (11, 'moll')]
    assert bitstring_to_keyset('000000000000000000000001') == [(11, 'moll')]

def test_insert_keysets():
    pass