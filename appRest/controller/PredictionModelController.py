from flask import Blueprint, jsonify, request, Response
from appRest.service.PredictionModelSvc import PredictionModelSvc
from appRest.model import responseApi
from datetime import datetime
import gzip


class PredictionModelController:
    def __init__(self):
        self.blueprint = Blueprint(
            'Prediction_Controller', __name__, url_prefix='/prediction-model')

        @self.blueprint.route('create-train', methods=['GET'])
        def executeTrainModel():
            svc = PredictionModelSvc()
            currentDate = datetime.today().strftime('%Y-%m-%d')
            response = svc.createModels('2022-01-01', currentDate)
            return jsonify(response.to_dict())

        @self.blueprint.route('get-predict', methods=['POST'])
        def getPredictionsBySite():
            data = request.get_json()
            month_year = data['month_year']
            id_user = data['id_user']
            svc = PredictionModelSvc()
            response = svc.getPrediction(month_year, id_user)
            responseCompress = gzip.compress(jsonify(response.to_dict()).data)
            return Response(response=responseCompress, status=200, mimetype='application/json', headers={'Content-Encoding': 'gzip'})
            # return jsonify(response.to_dict())

            # return jsonify({'response': 'ok'})
