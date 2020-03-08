"""
A module to contain the model for the PyChummer database
"""
from PyQt5.QtSql import QSqlDatabase, QSqlQuery 
from dataclasses import dataclass

@dataclass
class Runner():
    '''Class for tracking a Shadowrunnner'''
    id: int
    name: str

class Database():
    """
    The database model
    """
    def __init__(self):
        self._db = QSqlDatabase.addDatabase("QSQLITE")
        self._db.setDatabaseName("runners.db")
        self._db.open()

        self._setup_runners()

    def _setup_runners(self):
        '''Setup the runners table'''
        if "runners" in self._db.tables():
            return
        QSqlQuery("""
            CREATE TABLE runners ( 
                id integer primary key autoincrement, 
                name varchar(255) 
            )""", self._db).exec_()
        self.add_runner(Runner(id=None, name="Chummer"))


    def get_runners(self) -> QSqlQuery:
        '''Get a list of the runners as a QSqlQuery'''
        query = QSqlQuery("SELECT name FROM runners", self._db)
        return query

    def add_runner(self, runner: Runner) -> Runner:
        '''Add a runner to the SQLite Database'''
        query = QSqlQuery("INSERT INTO runners (id, name) values (?, ?)", self._db)
        query.bindValue(0, runner.id)
        query.bindValue(1, runner.name)
        query.exec_()
        runner.id = query.lastInsertId()
