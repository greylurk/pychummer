'''Views for the pychummer'''
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QListView, QWidget
from PyQt5.QtSql import QSqlTableModel

class CharacterListPanel():
    '''Present a character list panel'''
    def __init__(self, database):
        self._window = QWidget()

        layout = QVBoxLayout()
        label = QLabel("Hello World!")
        layout.addWidget(label)

        model = QSqlTableModel()
        model.setQuery(database.get_runners())

        list_view = QListView()
        list_view.setModel(model)
        layout.addWidget(list_view)

        self._window.setLayout(layout)

    def widget(self):
        '''Expose the root widget of this panel'''
        return self._window
