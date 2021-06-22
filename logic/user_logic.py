from core.pyba_logic import PybaLogic


class UserLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertUser(self, user, password, salt):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `hotel`.`preloadusers` "
            + "(`id`,`user`,`role`,`password`,`salt`) "
            + f"VALUES(0,'{user}','client','{password}','{salt}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getUser(self, user):
        database = self.createDatabaseObj()
        sql = (
            "SELECT user, role, password, salt "
            + f"FROM hotel.preloadusers where user like '{user}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []

    def getAllRooms(self):
        database = self.createDatabaseObj()
        sql = "SELECT * FROM hotel.preloadrooms;;"
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []

    def getRoom(self, roomId):
        database = self.createDatabaseObj()
        sql = "SELECT id, room " + f"FROM hotel.preloadrooms where roomId '{roomId}';"
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []

    def deleteRoomBooked(self, room):
        database = self.createDatabaseObj()
        sql = f"Delete FROM hotel.roomsBooked where roomId '{room}';"
        result = database.executeNonQueryRows(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []
