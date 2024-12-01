# from services.sync_service import ejecutar_proceso
from services.recorre_BBDD import ejecutar_proceso
import pymssql
'''
Quevedo:                                    CONCORD305-303\SQLEXPRESS_R2
LAMALLORQUINA: (Norte)                       DESKTOP-9MN4P32\SQLEXPRESS_2016
Velázquez (que es otra que funciona bien):  CONCORD3050\SQLEXPRESS_2019
MallorquinaMG:                              SERVIDOR\SQLEXPRESS_2014
SOL (BOMBONERIA):                           CONCORD305-303\SQLSERVER2019
SOL (MALLORQUINA2017):                      CONCORD305-303\SQLSERVER2019
'''

if __name__ == "__main__":
    ejecutar_proceso()
