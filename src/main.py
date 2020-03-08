'''open a window'''
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel, QListView, QWidget
from PyQt5.QtSql import QSqlTableModel
from model import Database

app = QApplication([])

window = QWidget()

layout = QVBoxLayout()

label = QLabel("Hello World!")
layout.addWidget(label)

database = Database()

model = QSqlTableModel()
model.setQuery(database.get_runners())

listView = QListView()
listView.setModel(model)
layout.addWidget(listView)

window.setLayout(layout)
window.show()

app.exec_()
