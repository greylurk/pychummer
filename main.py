'''open a window'''
from PyQt5.QtWidgets import QApplication, QLabel, QListView
from PyQt5.QtSql import QSqlTableModel
from model import Database

app = QApplication([])
label = QLabel("Hello World!")
label.show()

database = Database()

model = QSqlTableModel()
model.setQuery(database.get_runners())

listView = QListView()
listView.setModel(model)
listView.show()

app.exec_()
