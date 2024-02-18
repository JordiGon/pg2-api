from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DbConnection:
    def __init__(self):
        self.engine = create_engine(
            "mysql+pymysql://root:admin123@localhost:3306/prototype_db")
        self.connection = self.engine.connect()
        self.Session = sessionmaker(bind=self.engine)

    def close_connection(self):
        self.connection.close()

    def get_session(self):
        return self.Session()
