from dataclasses import dataclass
from PyQt5.QtSql import QSqlQueryModel, QSqlDatabase, QSqlQuery

@dataclass
class Runner():
    '''Class for tracking a Shadowrunnner'''
    name: str
    id: int = None

class RunnerListModel(QSqlQueryModel):
    _database : QSqlDatabase

    def __init__(self, database: QSqlDatabase):
        super(RunnerListModel, self).__init__()
        self._database = database
        self.refresh()

    def refresh(self):
        self.setQuery(QSqlQuery("SELECT name FROM runners", self._database))
