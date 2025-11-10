from typing import Any

from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    def leggi_artefatto(self, museo: str | None = None, epoca: str | None = None):
        artefatti = []
        cnx = ConnessioneDB.get_connection()
        try:
            cursor = cnx.cursor(dictionary=True)
            query = ("SELECT * "
                     "FROM artefatto "
                     "WHERE (%s IS NULL OR id_museo = %s) "
                     "AND (%s IS NULL OR epoca = %s)")
            cursor.execute(query,(museo,museo,epoca,epoca))
            for row in cursor:
                artefatto = Artefatto(id = row["id"],
                                      nome = row["nome"],
                                      tipologia = row["tipologia"],
                                      epoca = row["epoca"],
                                      id_museo = row["id_museo"])
                artefatti.append(artefatto)
            cursor.close()
            cnx.close()
            return artefatti
        except Exception as e:
            print("Errore in leggi_artefatto:", e)
            return []