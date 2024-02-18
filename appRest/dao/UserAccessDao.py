from db import DbConnection
from appRest.model.UserAccessModel import UserAccess
from sqlalchemy import and_


class UserAccessDao():
    def __init__(self):
        self.db = DbConnection()

    def getAllUserAccess(self):
        session = self.db.get_session()
        result = session.query(UserAccess).all()
        session.close()
        return result

    def createUserAccess(self, newUserAccess):
        session = self.db.get_session()
        session.add(newUserAccess)
        session.flush()
        created_user_access = UserAccess(**newUserAccess.to_dict())
        session.commit()
        session.close()
        return created_user_access

    def deleteUserAccess(self, id):
        session = self.db.get_session()
        deleted_user_access = session.query(UserAccess).get(id)
        response = UserAccess(**deleted_user_access.to_dict())
        session.delete(deleted_user_access)
        session.flush()
        session.commit()
        session.close()
        return response

    def getUserAccessById(self, id):
        session = self.db.get_session()
        user_access = session.query(UserAccess).get(id)
        session.close()
        return user_access

    def updateUserAccess(self, updatedUserAccess):
        session = self.db.get_session()
        session.merge(updatedUserAccess)
        session.commit()
        session.close()
        return UserAccess(**updatedUserAccess.to_dict())

    def getUserAccessById(self, id):
        session = self.db.get_session()
        result = session.query(UserAccess).filter(and_(
            UserAccess.id_user_fk == id
        ))
        session.close()
        return result
