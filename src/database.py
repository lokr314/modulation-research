from typing import List

import psycopg2

from src.model.PCSet import PCSetClass
from src.model.types_and_stuff import PCSet


def get_connection():
    return psycopg2.connect(database="modulation_research",
                            host="localhost",
                            user="postgres",
                            password="17002002",
                            port="5432")

# --- Create Tables ------------------------------------------------------------

def create_tables():
    conn = get_connection()

    with conn, conn.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS pcsets (
                        pcset bit(12) NOT NULL UNIQUE PRIMARY KEY,
                        pcset_size integer NOT NULL,
                        pcset_name varchar(255),
                        is_atonal boolean NOT NULL,
                        is_reduced boolean NOT NULL
                       );""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS keysets (
                        keyset bit(24) NOT NULL UNIQUE PRIMARY KEY,
                        keyset_size integer NOT NULL,
                        shortest_path_length integer NOT NULL,
                        shortest_path_example integer[] NOT NULL,
                        is_simple boolean NOT NULL
                       );""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS modulations (
                        id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                        start_keyset bit(24) NOT NULL,
                        pcset bit(12) NOT NULL,
                        end_keyset bit(24) NOT NULL,
                        foreign_pitches int[] NOT NULL,
                        is_same_keyset boolean NOT NULL,
                        is_key_constitution boolean NOT NULL,
                        is_modulation boolean NOT NULL,
                        is_simple_modulation boolean NOT NULL,
                        FOREIGN KEY (start_keyset) REFERENCES keysets(keyset),
                        FOREIGN KEY (end_keyset) REFERENCES keysets(keyset),
                        FOREIGN KEY (pcset) REFERENCES pcsets(pcset)
                       );""")

# --- Insert PCSet -------------------------------------------------------------

def pcset_to_bitstring(pcset: List[int]) -> int:
    bitstring = 0
    for pc in pcset:
        bitstring |= 1 << 11 - pc
    return bitstring

def bitstring_to_pcset(bitstring: str) -> List[int]:
    pcset = []
    bitstring = bitstring[::-1]
    for i in range(12):
        if bitstring[i] == "1":
            pcset.append(i)
    return pcset


def insert_pcsets(pcsets: List[PCSetClass]):
    conn = get_connection()

    sql_string = """INSERT INTO pcsets (pcset, pcset_size, pcset_name, is_atonal, is_reduced)
VALUES
"""

    for pcset in pcsets:
        sql_string += f"    ({pcset_to_bitstring(pcset.pcset)}::bit(12), {pcset.pcset_size}, {pcset.pcset_name if pcset.pcset_name else 'NULL'}, {pcset.is_atonal}, {pcset.is_reduced}),\n"

    sql_string = sql_string[:-2] + ";"

    with conn, conn.cursor() as cursor:
        cursor.execute(sql_string)


def insert_pcset(pcset: PCSetClass):
    conn = get_connection()

    sql_string = f"""INSERT INTO pcsets (pcset, pcset_size, pcset_name, is_atonal, is_reduced)
VALUES 
    ({pcset_to_bitstring(pcset.pcset)}::bit(12), {pcset.pcset_size}, {pcset.pcset_name if pcset.pcset_name else 'NULL'}, {pcset.is_atonal}, {pcset.is_reduced});"""

    with conn, conn.cursor() as cursor:
        cursor.execute(sql_string)


# --- Insert KeySet ------------------------------------------------------------


# --- Insert Modulation --------------------------------------------------------


# --- Select PCSet -------------------------------------------------------------
def select_pcset(pcset: PCSet) -> PCSet:
    conn = get_connection()

    sql_string = f"""SELECT * FROM pcsets WHERE pcset = {pcset_to_bitstring(pcset)}::bit(12);"""

    with conn, conn.cursor() as cursor:
        cursor.execute(sql_string)
        row = cursor.fetchone()

    return bitstring_to_pcset(row[0]) if row else None


if __name__ == "__main__":
    #create_tables()
    pass

