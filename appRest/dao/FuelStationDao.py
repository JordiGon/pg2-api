from db import DbConnection
from appRest.model.FuelStationModel import FuelStation


class FuelStationDao():
    def __init__(self):
        self.db = DbConnection()

    def getAllFuelStation(self):
        session = self.db.get_session()
        result = session.query(FuelStation).all()
        session.close()
        return result

    def createStation(self, newFuelStation):
        session = self.db.get_session()
        session.add(newFuelStation)
        session.flush()
        created_station = FuelStation(**newFuelStation.to_dict())
        session.commit()
        session.close()
        return created_station

    def deleteStation(self, id):
        session = self.db.get_session()
        deleted_station = session.query(FuelStation).get(id)
        response = FuelStation(**deleted_station.to_dict())
        session.delete(deleted_station)
        session.flush()
        session.commit()
        session.close()
        return response

    def getById(self, id):
        session = self.db.get_session()
        fuel_station = session.query(FuelStation).get(id)
        session.close()
        return fuel_station

    def updateStation(self, updatedStation):
        session = self.db.get_session()
        session.merge(updatedStation)
        session.commit()
        session.close()
        return FuelStation(**updatedStation.to_dict())
