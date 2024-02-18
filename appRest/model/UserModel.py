from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# from appRest.model.UserAccessModel import UserAccess
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(300), nullable=False)
    second_name = Column(String(300), nullable=False)
    first_lastname = Column(String(300), nullable=False)
    second_lastname = Column(String(300), nullable=False)
    email = Column(String(500), nullable=False)
    password = Column(String(255), nullable=False)
    username = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False,
                        server_default="CURRENT_TIMESTAMP")
    updated_at = Column(TIMESTAMP, nullable=False,
                        server_default="CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    is_admin = Column(Boolean, nullable=False)

    def to_dict(self):
        return {
            'id_user': self.id_user,
            'first_name': self.first_name,
            'second_name': self.second_name,
            'first_lastname': self.first_lastname,
            'second_lastname': self.second_lastname,
            'email': self.email,
            'username': self.username,
            'password': self.password,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at),
            'is_admin': self.is_admin
        }
