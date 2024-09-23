# from src.database import insert_pcset, select_pcset, get_connection, insert_pcsets
# from src.model.PCSet import PCSetClass
# from src.model.types_and_stuff import tonal_and_up_to_6_pcs_pcsets


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
        