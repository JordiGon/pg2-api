from appRest.ml.data_preparation import DataPreparation
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error
from datetime import datetime, date
import pickle
import calendar


class ModelTraining:
    def __init__(self):
        self.X_train = None
        self.y_train = None
        self.model = None
        self.data_preparation = DataPreparation()

    def train(self, start_date, end_date):
        stations = self.data_preparation.get_stations()
        for index, row in stations.iterrows():
            site = row['gu_station']
            self.data = self.data_preparation.get_for_site(
                start_date, end_date, site)
            X = self.data[['FUELPROD', 'TRLDAY', 'TRLHOUR',
                           'MONTH', 'YEAR', 'WEEKDAY']]
            y = self.data['FUELVOLUME']
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                X, y, test_size=0.2, random_state=0)
            param_grid = {
                'n_estimators': [100, 200, 300],
                'max_depth': [5, 10, 20],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 2, 4]
            }
            self.model = GridSearchCV(
                RandomForestRegressor(), param_grid, cv=5, n_jobs=-1)
            self.model.fit(self.X_train, self.y_train)
            with open(f'{site}.pkl', 'wb') as file:
                pickle.dump(self.get_model(), file)

    def get_model(self):
        return self.model

    def evaluate_model(self):
        y_pred = self.model.predict(self.X_test)
        rmse = np.sqrt(mean_squared_error(self.y_test, y_pred))
        return rmse

    def predict(self, site, month_year):
        with open(f'{site}.pkl', 'rb') as file:
            model = pickle.load(file)
        dateAux = datetime.strptime(month_year, '%m-%Y')
        num_days = calendar.monthrange(dateAux.year, dateAux.month)[1]
        hours = pd.DataFrame({'TRLHOUR': range(24)})
        days = pd.DataFrame({'TRLDAY': range(1, num_days+1)})
        fuel = pd.DataFrame({'FUELPROD': range(1, 4)})
        df = pd.merge(hours, days, how='cross')
        df = pd.merge(df, fuel, how='cross')
        df['MONTH'] = dateAux.month
        df['YEAR'] = dateAux.year
        df['SITE'] = site
        for index, row in df.iterrows():
            df.at[index, 'WEEKDAY'] = date(
                row['YEAR'], row['MONTH'], row['TRLDAY']).weekday()
        df['WEEKDAY'] = df['WEEKDAY'].astype(int)
        X_pred = df[['FUELPROD', 'TRLDAY', 'TRLHOUR',
                     'MONTH', 'YEAR', 'WEEKDAY']]
        y_pred = model.predict(X_pred)
        df['FUELVOLUME'] = y_pred
        return df[['FUELPROD', 'TRLDAY', 'TRLHOUR', 'MONTH', 'YEAR', 'FUELVOLUME', 'SITE', 'WEEKDAY']]
