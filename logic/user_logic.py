from core.pyba_logic import PybaLogic


class UserLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertUser(self, user, role, password, salt):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `hotel`.`preloadusers` "
            + "(`id`,`user`,`role`,`password`,`salt`) "
            + f"VALUES(0,'{user}','{role}','{password}','{salt}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getUser(self, user):
        database = self.createDatabaseObj()
        sql = (
            "SELECT user, password, salt "
            + f"FROM hotel.preloadusers where user like '{user}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []
