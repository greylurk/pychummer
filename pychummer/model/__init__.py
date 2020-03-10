"""
A module to contain the model for the PyChummer database
"""
from PyQt5.QtCore import qDebug, qFatal
from PyQt5.QtSql import QSqlDatabase, QSqlQuery 
from pychummer.model.runner import Runner, RunnerListModel

class Database():
    """
    The database model
    """
    def __init__(self):
        self._db: QSqlDatabase = QSqlDatabase.addDatabase("QSQLITE")
        self._db.setDatabaseName("runners.db")
        if not self._db.open():
            qFatal("Something awful has happened")

        self._setup_runners()

    def _setup_runners(self):
        '''Setup the runners table'''
        self._db.exec_("""
            CREATE TABLE runners ( 
                id integer primary key autoincrement, 
                name varchar(255) 
            )""")
        self.save_runner(Runner("Chummer"))

    def runner_list_model(self) -> RunnerListModel:
        '''Get a ListModel of the runners'''
        return RunnerListModel(self._db)

    def save_runner(self, runner: Runner) -> Runner:
        '''Add a runner to the SQLite Database'''
        if runner.id is not None:
            _update_runner = QSqlQuery(self._db)
            _update_runner.prepare("UPDATE runners SET name=:name where id=:id")
            _update_runner.bindValue(":id", runner.id)
            _update_runner.bindValue(":name", runner.name)
            if not _update_runner.exec_():
                qDebug(_update_runner.lastError().text())
        if runner.id is None or _update_runner.numRowsAffected == 0:
            if not "runners" in self._db.tables():
                qDebug("The table is missing")
            _insert_runner = QSqlQuery(self._db)
            _insert_runner.prepare('''
                INSERT INTO runners (
                    name
                ) values (
                    :name
                )''')
            _insert_runner.bindValue(":name", runner.name)
            if not _insert_runner.exec_():
               qDebug(_insert_runner.lastError().text()) 

            runner.id = _insert_runner.lastInsertId()
        return runner
