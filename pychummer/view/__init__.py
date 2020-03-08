'''Views for the pychummer'''
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QListView, QWidget, QPushButton
from pychummer.model import Runner

class CharacterListPanel(QWidget):
    '''Present a character list panel'''
    def __init__(self, database):
        super().__init__()
        self._model = QSqlTableModel()
        self._model.setQuery(database.get_runners())
        self._database = database

        self.init_ui()

    def init_ui(self) -> None:
        '''Initialize the UI'''
        layout = QVBoxLayout()
        label = QLabel("Hello World!")
        layout.addWidget(label)

        list_view = QListView()
        list_view.setModel(self._model)
        layout.addWidget(list_view)

        add_button = QPushButton("Add", self)
        add_button.clicked.connect(self.on_click_add)        
        layout.addWidget(add_button)

        self.setLayout(layout)
        self.show()

    @pyqtSlot()
    def on_click_add(self) -> None:
        runner = Runner();
        
