from sqlalchemy import String, Column, Integer, Date, BigInteger, DECIMAL, DateTime
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class DataUnoModel(base):
    __tablename__ = 'uno_trans_xml_autocollect'
    
    ID = Column(Integer, primary_key=True )
    LONGID = Column(Date)
    SHORTID = Column(String)
    SITE = Column(String)
    TURNO = Column(String)
    TYPEID = Column(String)
    RECALLED = Column(String)
    TRDATE = Column(Date)
    TRTIME = Column(String)
    TRSEQ = Column(BigInteger)
    TRLDEPT = Column(String)
    TRLQTY = Column(Integer)
    TRLUNITPRICE = Column(DECIMAL(15,2))
    TRLLINETOT = Column(DECIMAL(20,2))
    FUELPROD = Column(String)
    FUELSVCMODE = Column(String)
    FUELPOSITION = Column(String)
    FUELVOLUME = Column(DECIMAL(10,3))
    TRPPAYCODE = Column(String)
    IDTRANESTACIONLOCAL = Column(DECIMAL(25,0))
    POSNUM  = Column(String)
    AUTHORIZATION_FLOTA = Column(String)
    ELECTRONICBILLNUMBER = Column(String)
    TAXNUMBER = Column(String)
    FISCALNAME = Column(String)
    OPENEDTIME = Column(DateTime)
    CLOSETIME = Column(DateTime)
    TRAN_ORIGIN = Column(String)
    START_DATE = Column(Date)
    START_TIME = Column(DateTime)
    END_DATE = Column(Date)
    END_TIME = Column(DateTime)
    IDTRPPAYCODE = Column(BigInteger)
    
    def to_dict(self):
        return {
        'ID':self.ID,
        'LONGID':self.LONGID,
        'SHORTID': self.SHORTID,
        'SITE': self.SITE,
        'TURNO': self.TURNO,
        'TYPEID': self.TYPEID,
        'RECALLED': self.RECALLED,
        'TRDATE': self.TRDATE,
        'TRTIME': self.TRTIME,
        'TRSEQ': self.TRSEQ,
        'TRLDEPT': self.TRLDEPT,
        'TRLQTY': self.TRLQTY,
        'TRLUNITPRICE': self.TRLUNITPRICE,
        'TRLLINETOT': self.TRLLINETOT,
        'FUELPROD': self.FUELPROD,
        'FUELSVCMODE': self.FUELSVCMODE,
        'FUELPOSITION': self.FUELPOSITION,
        'FUELVOLUME': self.FUELVOLUME,
        'TRPPAYCODE': self.TRPPAYCODE,
        'IDTRANESTACIONLOCAL': self.IDTRANESTACIONLOCAL,
        'POSNUM': self.POSNUM,
        'AUTHORIZATION_FLOTA': self.AUTHORIZATION_FLOTA,
        'ELECTRONICBILLNUMBER': self.ELECTRONICBILLNUMBER,
        'TAXNUMBER': self.TAXNUMBER,
        'FISCALNAME': self.FISCALNAME,
        'OPENEDTIME': self.OPENEDTIME,
        'CLOSETIME': self.CLOSETIME,
        'TRAN_ORIGIN': self.TRAN_ORIGIN,
        'START_DATE': self.START_DATE,
        'START_TIME': self.START_TIME,
        'END_DATE': self.END_DATE,
        'END_TIME': self.END_TIME,
        'IDTRPPAYCODE': self.IDTRPPAYCODE
        }