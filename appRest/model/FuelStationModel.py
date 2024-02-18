from sqlalchemy import String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class FuelStation(base):
    
    #nombre de la tabla que utilizaremos
    __tablename__ = 'fuel_station'
    
    #se especifican los datos 
    id_station = Column(Integer, primary_key = True)
    gu_station = Column(String)
    station_name = Column(String)
    
    #funcion para crear el json a retornar
    def to_dict(self):
        return {
        'id_station':self.id_station,
        'gu_station':self.gu_station,
        'station_name':self.station_name
        }
    