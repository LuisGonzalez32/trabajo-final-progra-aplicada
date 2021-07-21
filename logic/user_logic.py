from core.pyba_logic import PybaLogic


class UserLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertUser(self, user, password, salt):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `heroku_505461be12611e0`.`user` "
            + "(`id`,`user_name`,`role`,`password`,`salt`) "
            + f"VALUES(0,'{user}','client','{password}','{salt}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def insertEvent(self, eventName, client, date, numberOfPeople):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `heroku_505461be12611e0`.`event` "
            + "(`id`,`event_name`,`user`,`date`,`number_of_people`) "
            + f"VALUES(0,'{eventName}','{client}','{date}',{numberOfPeople});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def bookRoom(self, userName, roomId, checkin, checkout):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `heroku_505461be12611e0`.`roomsBooked` "
            + "(`id`,`userName`,`bookId`,`checkin`,`checkout`) "
            + f"VALUES(0, '{userName}', {roomId}, '{checkin}', '{checkout}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getUser(self, user):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM heroku_505461be12611e0.user where user_name = '{user}';"
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []

    def getAllRooms(self):
        database = self.createDatabaseObj()
        sql = "select * from heroku_505461be12611e0.rooms;"
        result = database.executeQuery(sql)
        return result

    def getAllEvents(self):
        database = self.createDatabaseObj()
        sql = "select * from heroku_505461be12611e0.event;"
        result = database.executeQuery(sql)
        return result

    def getRoomsBooked(self):
        database = self.createDatabaseObj()
        sql = "select * from heroku_505461be12611e0.viewroomsbooked;"
        result = database.executeQuery(sql)
        return result

    def roomsBooked(self):
        database = self.createDatabaseObj()
        sql = "select * from heroku_505461be12611e0.roomsbooked;"
        result = database.executeQuery(sql)
        return result

    def roomsBooked(self):
        database = self.createDatabaseObj()
        sql = "select * from hotel.roomsbooked;"
        result = database.executeQuery(sql)
        return result

    def deleteRoomBooked(self, room):
        database = self.createDatabaseObj()
        sql = f"Delete FROM heroku_505461be12611e0.roomsBooked where id = '{room}';"
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteEvent(self, room):
        database = self.createDatabaseObj()
        sql = f"Delete FROM heroku_505461be12611e0.event where id = '{room}';"
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteEvent(self, room):
        database = self.createDatabaseObj()
        sql = f"Delete FROM hotel.event where id = '{room}';"
        rows = database.executeNonQueryRows(sql)
        return rows
