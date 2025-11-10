import mysql

from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    # TODO
    def leggi_musei(self, museo: str | None = None):
        musei = []
        cnx = ConnessioneDB.get_connection()
        try:
            cursor = cnx.cursor(dictionary=True)
            query = ("SELECT * "
                     "FROM museo")
            cursor.execute(query,museo)
            for row in cursor:
                museo = Museo(row["id"],
                              row["nome"],
                              row["tipologia"])
                musei.append(museo)

            cursor.close()
            cnx.close()
            return musei
        except Exception as e:
            print(e)
