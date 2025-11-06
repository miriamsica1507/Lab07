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
    def leggi_artefatto(self, museo:str, epoca:str) -> list[Any] | None:
        artefatti = []
        cnx = ConnessioneDB.get_connection()
        try:
            cursor = cnx.cursor(dictionary=True)
            query = ("SELECT * "
                     "FROM artefatto "
                     "WHERE (epoca = COALESCE(%s, epoca)) "
                     "AND (id_museo = COALESCE(%s, id_museo))")
            cursor.execute(query,(epoca,museo))
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
            print(e)