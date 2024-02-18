from appRest.dao.FuelStationDao import FuelStationDao
from appRest.model.responseApi import ResponseApi
from sqlalchemy.orm.exc import NoResultFound


class FuelStationSvc():
    def __init__(self):
        self.dao = FuelStationDao()

    def getAllFuelStation(self):
        try:
            result = self.dao.getAllFuelStation()
            return ResponseApi(200, [r.to_dict() for r in result], "succesfull query")
        except Exception as e:
            return ResponseApi(500, str(e), "unsuccesfull query")

    def createStation(self, newFuelStation):
        try:
            result = self.dao.createStation(newFuelStation)
            return ResponseApi(200, result.to_dict(), "succesfull query")
        except Exception as e:
            return ResponseApi(500, str(e), "unsuccesfull query")

    def deleteStation(self, id):
        try:
            result = self.dao.deleteStation(id)
            return ResponseApi(200, result.to_dict(), "succesfull query")
        except Exception as e:
            return ResponseApi(500, str(e), "unsuccesfull query")

    def updateStation(self, updatedStation):
        try:
            if not self.dao.getById(updatedStation.id_station):
                return ResponseApi(404, None, "Station not found")
            result = self.dao.updateStation(updatedStation)
            return ResponseApi(200, result.to_dict(), "succesfull query")
        except Exception as e:
            return ResponseApi(500, str(e), "unsuccesfull query")
