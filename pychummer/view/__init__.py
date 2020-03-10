'''Views for the pychummer'''
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QListView, QWidget, QPushButton
from pychummer.model import Runner, Database

class CharacterListPanel(QWidget):
    '''Present a character list panel'''

    _list_view : QListView

    def __init__(self, database: Database):
        super().__init__()
        self._model:QSqlTableModel = QSqlTableModel()
        self._model.setQuery(database.get_runners())
        self._database:QSqlDatabase = database

        self.init_ui()

    def init_ui(self) -> None:
        '''Initialize the UI'''
        layout = QVBoxLayout()
        label = QLabel("Hello World!")
        layout.addWidget(label)

        self._list_view = QListView()
        self._list_view.setModel(self._model)
        layout.addWidget(self.list_view)

        add_button = QPushButton("Add", self)
        add_button.clicked.connect(self.on_click_add)        
        layout.addWidget(add_button)

        self.setLayout(layout)
        self.show()

    @pyqtSlot()
    def on_click_add(self) -> None:
        runner = Runner("John Jacob Jingleheimer Schmidt")
        runner = self._database.save_runner(runner)
        self._model.query()
        print(runner.id)

        
