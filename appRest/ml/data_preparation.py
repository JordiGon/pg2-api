from appRest.dao.DataUnoDao import DataUnoDao
from appRest.dao.FuelStationDao import FuelStationDao
import pandas as pd


class DataPreparation:
    def __init__(self):
        self.transactions_dao = DataUnoDao()
        self.stations_dao = FuelStationDao()

    def get_stations(self):
        data = self.stations_dao.getAllFuelStation()
        data_dict = [d.__dict__ for d in data]
        df = pd.DataFrame(
            data_dict, columns=['gu_station', 'id_station', 'station_name'])
        df = df[['gu_station']]
        return df

    def get_data(self, start_date, end_date):
        data = self.transactions_dao.getByDate(
            start_date=start_date, end_date=end_date)
        data_dict = [d.__dict__ for d in data]
        df = self.cleaning_data(data_dict)
        grouped_data = df.groupby(['FUELPROD', 'TRLDAY', 'TRLHOUR', 'MONTH', 'YEAR', 'WEEKDAY'])[
            'FUELVOLUME'].sum().reset_index()
        print(grouped_data)
        return grouped_data

    def get_for_site(self, start_date, end_date, site):
        data = self.transactions_dao.getBySiteAndDate(
            start_date, end_date, site)
        data_dict = [d.__dict__ for d in data]
        df = self.cleaning_data(data_dict)
        grouped_data = df.groupby(['FUELPROD', 'TRLDAY', 'TRLHOUR', 'MONTH', 'YEAR', 'WEEKDAY'])[
            'FUELVOLUME'].sum().reset_index()
        print(grouped_data)
        return grouped_data

    def cleaning_data(self, data):
        # Convertimos los datos a un DataFrame de Pandas
        df = pd.DataFrame(data, columns=['ID', 'LONGID', 'SHORTID', 'SITE', 'TURNO', 'TYPEID',
                                         'RECALLED', 'TRDATE', 'TRTIME', 'TRSEQ', 'TRLDEPT',
                                         'TRLQTY', 'TRLUNITPRICE', 'TRLLINETOT', 'FUELPROD',
                                         'FUELSVCMODE', 'FUELPOSITION', 'FUELVOLUME', 'TRPPAYCODE',
                                         'IDTRANESTACIONLOCAL', 'POSNUM', 'AUTHORIZATION_FLOTA',
                                         'ELECTRONICBILLNUMBER', 'TAXNUMBER', 'FISCALNAME',
                                         'OPENEDTIME', 'CLOSETIME', 'TRAN_ORIGIN', 'START_DATE',
                                         'START_TIME', 'END_DATE', 'END_TIME', 'IDTRPPAYCODE'])

        df['TRLDATETIME'] = pd.to_datetime(
            df['TRDATE'].astype(str)+' '+df['TRTIME'])
        df = df.sort_values(['TRLDATETIME'])
        df['TRLDAY'] = df['TRLDATETIME'].dt.day
        df['TRLHOUR'] = df['TRLDATETIME'].dt.hour
        df['WEEKDAY'] = df['TRLDATETIME'].dt.weekday
        df['MONTH'] = df['TRLDATETIME'].dt.month
        df['YEAR'] = df['TRLDATETIME'].dt.year
        df = df[['SITE', 'FUELPROD', 'FUELPOSITION', 'FUELVOLUME',
                 'TRLDAY', 'TRLHOUR', 'WEEKDAY', 'MONTH', 'YEAR', 'TRLUNITPRICE']]

        # diccionario de productos
        fuel_codes = {
            'Regular con Dynamax': 1,
            'Super con Dynamax': 2,
            'Diesel con Dynamax': 3,
            'ULS Diesel con Dynamax': 3,
            'Regular': 1,
            'Super': 2,
            'Diesel': 3
        }
        df['FUELPOSITION'] = pd.to_numeric(df['FUELPOSITION'], errors='coerce')
        df['FUELVOLUME'] = pd.to_numeric(df['FUELVOLUME'], errors='coerce')
        df['FUELPROD'] = df['FUELPROD'].replace(fuel_codes)
        return df
