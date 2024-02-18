from flask import Blueprint, jsonify, request
from appRest.service.FuelStationSvc import FuelStationSvc
from appRest.model.FuelStationModel import FuelStation


class FileStationController:
    def __init__(self):
        self.blueprint = Blueprint(
            'FileStation_Controller', __name__, url_prefix='/station')

        @self.blueprint.route('/get-all', methods=['GET'])
        def getAllData():
            svc = FuelStationSvc()
            response = svc.getAllFuelStation()
            return jsonify(response.to_dict())

        @self.blueprint.route('/create', methods=['POST'])
        def createStation():
            data = request.get_json()
            fuel_station = FuelStation(**data)
            svc = FuelStationSvc()
            response = svc.createStation(fuel_station)
            return jsonify(response.to_dict())

        @self.blueprint.route('/delete/<int:id>', methods=['DELETE'])
        def deleteStation(id):
            svc = FuelStationSvc()
            response = svc.deleteStation(id)
            return jsonify(response.to_dict())

        @self.blueprint.route('/update', methods=['PUT'])
        def updateStation():
            data = request.get_json()
            fuel_station = FuelStation(**data)
            svc = FuelStationSvc()
            response = svc.updateStation(fuel_station)
            return jsonify(response.to_dict())
