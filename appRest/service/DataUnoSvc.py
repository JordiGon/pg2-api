from appRest.dao.DataUnoDao import DataUnoDao
from appRest.model.responseApi import ResponseApi
from appRest.ml.data_preparation import DataPreparation
from appRest.service.UserSvc import UserSvc
from appRest.dao.UserDao import UserDao
from appRest.dao.FuelStationDao import FuelStationDao
from datetime import datetime, date
import pandas as pd
import calendar


class DataUnoSvc():
    def __init__(self):
        self.dao = DataUnoDao()
        self.dataPreparation = DataPreparation()
        self.user = UserSvc()
        self.userDao = UserDao()
        self.stationsDao = FuelStationDao()

    def getAllDataUno(self):
        try:
            resultDao = self.dao.getAllData()
            resulPreparation = self.dataPreparation.cleaning_data(resultDao)
            df = resulPreparation.groupby(['FUELPROD', 'TRLDAY', 'TRLHOUR', 'MONTH', 'YEAR', 'WEEKDAY', 'SITE'])[
                'FUELVOLUME'].sum().reset_index()
            df = df.to_dict(orient='records')
            return ResponseApi(200, df, "Succesfull query")
        except Exception as e:
            return ResponseApi(500, e, "unsuccesfull query")

    def getByDate(self, month_year, id):
        try:
            start_date, end_date = DataUnoSvc.get_date_range(month_year)
            result_df = pd.DataFrame()
            data = self.user.getStations(id)
            for item in data:
                resultDao = self.dao.getBySiteAndDate(
                    start_date=start_date, end_date=end_date, site=item['gu_station'])
                data_dict = [d.__dict__ for d in resultDao]
                resulPreparation = self.dataPreparation.cleaning_data(
                    data_dict)
                df = resulPreparation.groupby(['FUELPROD', 'TRLDAY', 'TRLHOUR', 'MONTH', 'YEAR', 'WEEKDAY', 'SITE'])[
                    'FUELVOLUME'].sum().reset_index()
                result_df = pd.concat([result_df, df], ignore_index=True)
            response = result_df.to_dict(orient='records')
            return ResponseApi(200, response, "Succesfull query")
        except Exception as e:
            return ResponseApi(500, str(e), "unsuccesfull query")

    @classmethod
    def get_date_range(cls, month_year):
        date = datetime.strptime(month_year, '%m-%Y')
        year = date.year
        month = date.month
        _, last_day = calendar.monthrange(year, month)
        start_date = datetime(year, month, 1).strftime('%Y-%m-%d')
        end_date = datetime(year, month, last_day).strftime('%Y-%m-%d')
        return start_date, end_date
