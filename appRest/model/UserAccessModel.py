from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from appRest.model.UserModel import User
from sqlalchemy.orm import relationship
from appRest.model.FuelStationModel import FuelStation


Base = declarative_base()


class UserAccess(Base):
    __tablename__ = 'user_access'
    id_user_access = Column(Integer, primary_key=True, autoincrement=True)
    id_user_fk = Column(Integer, ForeignKey(User.id_user))
    id_fuel_station_fk = Column(Integer, ForeignKey(FuelStation.id_station))
    users = relationship(User, passive_deletes=True, cascade="none"
                         )
    stations = relationship(FuelStation, passive_deletes=True, cascade="none"
                            )

    def to_dict(self):
        return {
            'id_user_access': self.id_user_access,
            'id_user_fk': self.id_user_fk,
            'id_fuel_station_fk': self.id_fuel_station_fk
        }
