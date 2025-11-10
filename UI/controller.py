import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def handler_popola_dropdown(self):
        musei = self._model.get_musei()
        epoche = self._model.get_epoche()
        if not musei or not epoche:
            self._view.show_alert("Non hai selezionato niente!")
            return
        self._view.dd_museo.options.clear()
        self._view.dd_epoca.options.clear()
        for museo in musei:
            self._view.dd_museo.options.append(ft.dropdown.Option(text=museo.nome))
        for epoca in epoche:
            self._view.dd_epoca.options.append(ft.dropdown.Option(text=epoca))

        self._view.page.update()


    # CALLBACKS DROPDOWN
    # TODO
    def handler_seleziona_museo(self,e):
        self.museo_selezionato = self._view.dd_museo.value
        self._view.update()
    def handler_seleziona_epoca(self,e):
        self.epoca_selezionata = self._view.dd_epoca.value
        self._view.update()

    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def handler_mostra_artefatti(self,e):
        museo = self._view.dd_museo.value
        epoca = self._view.dd_epoca.value
        artefatti = self._model.get_artefatti_filtrati(museo, epoca)

        self._view.lista_artefatti.controls.clear()

        if not artefatti:
            self._view.show_alert("Non hai inserito artefatti!")
            return
        for artefatto in artefatti:
            self._view.btn_artefatti.options.append(ft.Text(f"{artefatto.nome},{artefatto.tipologia},"
                                                            f"{artefatto.epoca}"))
        self._view.update()