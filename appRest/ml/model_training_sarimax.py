from appRest.ml.data_preparation import DataPreparation
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.statespace.sarimax import SARIMAX
from datetime import datetime
import pickle
import calendar


class ModelTrainingSARIMAX:
    def __init__(self):
        self.model = None
        self.data_preparation = DataPreparation()

    def train(self, start_date, end_date):
        site = 'GU300'
        self.data = self.data_preparation.get_for_site(
            start_date, end_date, site)
        # Selecciona las columnas que serán utilizadas como features
        exog_vars = self.data[['FUELPROD', 'TRLDAY', 'TRLHOUR',
                               'MONTH', 'YEAR']]
        # Selecciona la columna que se utilizará como target
        endog_var = self.data['FUELVOLUME']
        train_end = len(endog_var) - 12
        train_data = endog_var[:train_end]
        test_data = endog_var[train_end:]
        train_exog = exog_vars[:train_end]
        test_exog = exog_vars[train_end:]
        # Entrenamiento del modelo utilizando SARIMAX
        self.model = SARIMAX(
            train_data, exog=train_exog, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
        self.model_fit = self.model.fit()
        # Imprimir los resultados del modelo
        print("Site:", site)
        print("AIC:", self.model_fit.aic)
        # Guardar el modelo entrenado
        with open(f'{site}.pkl', 'wb') as file:
            pickle.dump(self.model_fit, file)

    def get_model(self):
        return self.model

    def evaluate_model(self):
        y_pred = self.model.predict(self.X_test)
        rmse = np.sqrt(mean_squared_error(self.y_test, y_pred))
        return rmse

    def predict(self, site, month_year):
        # Convertir el string con el mes y año en un objeto datetime
        with open(f'{site}.pkl', 'rb') as file:
            model = pickle.load(file)
        date = datetime.strptime(month_year, '%m-%Y')
        num_days = calendar.monthrange(date.year, date.month)[1]
        # Crear un DataFrame con todas las combinaciones posibles de día y hora para el mes y sitio especificado
        hours = pd.DataFrame({'TRLHOUR': range(24)})
        days = pd.DataFrame({'TRLDAY': range(1, num_days+1)})
        fuel = pd.DataFrame({'FUELPROD': range(1, 4)})
        df = pd.merge(hours, days, how='cross')
        df = pd.merge(df, fuel, how='cross')
        df['MONTH'] = date.month
        df['YEAR'] = date.year
        df['SITE'] = site

        exog = df[['FUELPROD', 'TRLDAY', 'TRLHOUR',
                   'MONTH', 'YEAR']]
        df = df.reset_index(drop=True)[
            ['FUELPROD', 'TRLDAY', 'TRLHOUR', 'MONTH', 'YEAR']]
        pred = model.forecast(len(df), exog=exog)
        df['FUELVOLUME'] = pred.reset_index(drop=True)

        # y_pred = pd.Series(y_pred, index=df.index)
        # y_pred = y_pred.reset_index(drop=True)

        print('valores')
        print(pred)
        # Agregar los valores de predicción al DataFrame
        # df['FUELVOLUME'] = pred
        return df[['FUELPROD', 'TRLDAY', 'TRLHOUR', 'MONTH', 'YEAR', 'FUELVOLUME']]
