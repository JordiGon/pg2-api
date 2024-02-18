from appRest.ml.model_training import ModelTraining
from appRest.model.responseApi import ResponseApi
from appRest.ml.data_preparation import DataPreparation
from appRest.service.UserSvc import UserSvc
from appRest.dao.UserDao import UserDao
from appRest.dao.FuelStationDao import FuelStationDao
import pandas as pd


class PredictionModelSvc:
    def __init__(self):
        self.model = ModelTraining()
        self.dataPreparation = DataPreparation()
        self.user = UserSvc()
        self.userDao = UserDao()
        self.stationsDao = FuelStationDao()

    def createModels(self, start_date, end_date):
        try:
            self.model.train(start_date, end_date)
            return ResponseApi(200, "Models Created", "succesfull query")
        except Exception as e:
            return ResponseApi(500, e, "unsuccesfull query")

    def getPrediction(self, month_year, id):
        try:
            result_df = pd.DataFrame()
            stations = self.user.getStations(id)
            if (len(stations) > 0):
                for row in stations:
                    site = row['gu_station']
                    data = self.model.predict(site, month_year)
                    result_df = pd.concat([result_df, data], ignore_index=True)
            data_dict = result_df.to_dict(orient='records')
            return ResponseApi(200, data_dict, "succesfull query")
        except Exception as e:
            return ResponseApi(500, str(e), "unsuccesfull query")
