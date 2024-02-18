from db import DbConnection
from appRest.model.DataUnoModel import DataUnoModel
from sqlalchemy import and_


class DataUnoDao():
    def __init__(self):
        self.db = DbConnection()
        
    def getAllData(self):
        session = self.db.get_session()
        result = session.query(DataUnoModel).limit(10).all()
        session.close()
        return result
    
    def getByDate(self, start_date, end_date):
        session = self.db.get_session()
        result = session.query(DataUnoModel).filter(
            and_(
                DataUnoModel.TRDATE >= start_date,
                DataUnoModel.TRDATE <= end_date
                )
            )
        session.close()
        return result
    
    
    def getBySiteAndDate(self, start_date, end_date, site):
        session = self.db.get_session()
        result = session.query(DataUnoModel).filter(
            and_(
                DataUnoModel.TRDATE >= start_date,
                DataUnoModel.TRDATE <= end_date,
                DataUnoModel.SITE == site)
            )
        session.close()
        return result
        