from appRest.dao.UserAccessDao import UserAccessDao
from appRest.model.responseApi import ResponseApi
from sqlalchemy.orm.exc import NoResultFound


class UserAccessSvc():
    def __init__(self):
        self.dao = UserAccessDao()

    def getAllUserAccess(self):
        try:
            result = self.dao.getAllUserAccess()
            return ResponseApi(200, [r.to_dict() for r in result], "successful query")
        except Exception as e:
            return ResponseApi(500, str(e), "unsuccessful query")

    def createUserAccess(self, newUserAccess):
        try:
            result = self.dao.createUserAccess(newUserAccess)
            return ResponseApi(200, result.to_dict(), "successful query")
        except Exception as e:
            return ResponseApi(500, str(e), "unsuccessful query")

    def deleteUserAccess(self, id):
        try:
            result = self.dao.deleteUserAccess(id)
            return ResponseApi(200, result.to_dict(), "successful query")
        except Exception as e:
            return ResponseApi(500, str(e), "unsuccessful query")

    def getUserAccessById(self, id):
        try:
            result = self.dao.getUserAccessById(id)
            return ResponseApi(200, result.to_dict(), "successful query")
        except NoResultFound:
            return ResponseApi(404, None, "User access not found")
        except Exception as e:
            return ResponseApi(500, str(e), "unsuccessful query")

    def updateUserAccess(self, updatedUserAccess):
        try:
            if not self.dao.getUserAccessById(updatedUserAccess.id_user_access):
                return ResponseApi(404, None, "User access not found")
            result = self.dao.updateUserAccess(updatedUserAccess)
            return ResponseApi(200, result.to_dict(), "successful query")
        except Exception as e:
            return ResponseApi(500, str(e), "unsuccessful query")
