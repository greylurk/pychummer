'''open a window'''
from PyQt5.QtWidgets import QApplication
from model import Database
from view import CharacterListPanel

def main():
    '''Start a new pychummer application'''
    app = QApplication([])
    database = Database()
    view = CharacterListPanel(database=database)

    view.widget().show()

    app.exec_()

if __name__ == "__main__":
    main()
