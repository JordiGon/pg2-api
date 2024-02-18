from flask import Blueprint, jsonify, request, Response
from appRest.service.DataUnoSvc import DataUnoSvc
from appRest.ml.data_preparation import DataPreparation
from appRest.ml.model_training import ModelTraining
import gzip
import pickle


class DataUnoController:
    def __init__(self):
        self.blueprint = Blueprint(
            'DataUno_Controller', __name__, url_prefix='/transactions')

        @self.blueprint.route('/get-all', methods=['GET'])
        def getAllData():
            svc = DataUnoSvc()
            response = svc.getAllDataUno()
            return jsonify(response.to_dict())

        @self.blueprint.route('/get-by-date', methods=['POST'])
        def get_by_date():
            data = request.get_json()
            month_year = data['month_year']
            id_user = data['id_user']
            svc = DataUnoSvc()
            response = svc.getByDate(month_year=month_year, id=id_user)
            responseCompress = gzip.compress(jsonify(response.to_dict()).data)
            return Response(response=responseCompress, status=200, mimetype='application/json', headers={'Content-Encoding': 'gzip'})
