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
        self.save_runner(Runner(id=None, name="Chummer"))


    def get_runners(self) -> QSqlQuery:
        '''Get a list of the runners as a QSqlQuery'''
        query = QSqlQuery("SELECT name FROM runners", self._db)
        return query

    def save_runner(self, runner: Runner) -> Runner:
        '''Add a runner to the SQLite Database'''
        if runner.id is not None:
            _update_runner = QSqlQuery(self._db)
            _update_runner.prepare("UPDATE runners SET name=:name where id=:id")
            _update_runner.bindValue(":id", runner.id)
            _update_runner.bindValue(":name", runner.name)
            _update_runner.exec_()
        if runner.id is None or _update_runner.numRowsAffected == 0:
            _insert_runner = QSqlQuery("INSERT INTO runners (name) values (:name)", self._db)
            _insert_runner.bindValue(":name", runner.name)
            _insert_runner.exec_()
            runner.id = _insert_runner.lastInsertId()
        return runner
