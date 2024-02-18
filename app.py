from flask import Flask
from flask import jsonify
from db import DbConnection
from sqlalchemy import text
from appRest.controller.DataUnoController import DataUnoController
from appRest.controller.FileStationController import FileStationController
from appRest.controller.PredictionModelController import PredictionModelController
from appRest.controller.UserController import UserController
from appRest.controller.UserAccessController import UserAccessController
from flask_cors import CORS


app = Flask(__name__)

usrAccessController = UserAccessController()
usrController = UserController()
dataUnoController = DataUnoController()
fileStationController = FileStationController()
predictionController = PredictionModelController()
app.register_blueprint(usrAccessController.blueprint)
app.register_blueprint(usrController.blueprint)
app.register_blueprint(predictionController.blueprint)
app.register_blueprint(fileStationController.blueprint)
app.register_blueprint(dataUnoController.blueprint)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})


if __name__ == '__main__':
    app.run(debug=True)
