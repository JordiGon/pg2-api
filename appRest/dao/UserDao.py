from db import DbConnection
from appRest.model.UserModel import User

class UserDao():
    def __init__(self):
        self.db = DbConnection()

    def getAllUsers(self):
        session = self.db.get_session()
        result = session.query(User).all()
        session.close()
        return result

    def createUser(self, newUser):
        session = self.db.get_session()
        session.add(newUser)
        session.flush()
        created_user = User(**newUser.to_dict())
        session.commit()
        session.close()
        return created_user

    def deleteUser(self, id):
        session = self.db.get_session()
        deleted_user = session.query(User).get(id)
        response = User(**deleted_user.to_dict())
        session.delete(deleted_user)
        session.flush()
        session.commit()
        session.close()
        return response

    def getUserById(self, id):
        session = self.db.get_session()
        user = session.query(User).get(id)
        session.close()
        return user

    def updateUser(self, updatedUser):
        session = self.db.get_session()
        session.merge(updatedUser)
        session.commit()
        session.close()
        return User(**updatedUser.to_dict())

    def getUserByEmail(self, email):
        session = self.db.get_session()
        user = session.query(User).filter_by(email=email).first()
        session.close()
        return user

    def getUserCredentials(self, email):
        session = self.db.get_session()
        user = session.query(User).filter_by(email=email).first()
        if user:
            return {'username': user.email, 'password': user.password}
        session.close()
        return None
    
    
    def check_email_exists(self, email):
        session = self.db.get_session()
        result = session.query(User).filter_by(email=email).first()
        session.close()
        return result is not None

    def check_username_exists(self, username):
        session = self.db.get_session()
        result = session.query(User).filter_by(username=username).first()
        session.close()
        return result is not None