from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO
from model.artefattoDTO import Artefatto

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo: str | None = None, epoca: str | None = None):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO
        return self._artefatto_dao.leggi_artefatto(museo, epoca)
    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        # TODO
    # --- MUSEI ---
        epoche = []
        artefatti = self._artefatto_dao.leggi_artefatto(None,None) or []
        for element in artefatti:
            if element.epoca not in epoche:
                epoche.append(element.epoca)
        return epoche

    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        # TODO
        musei = []
        for element in self._museo_dao.leggi_musei():
            musei.append(element)
        return musei
