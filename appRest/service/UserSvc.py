from appRest.dao.UserDao import UserDao
from appRest.dao.FuelStationDao import FuelStationDao
from appRest.dao.UserAccessDao import UserAccessDao
from appRest.model.UserModel import User
from appRest.model.responseApi import ResponseApi
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import jwt


class UserSvc():
    def __init__(self):
        self.dao = UserDao()
        self.daoAccess = UserAccessDao()
        self.stationDao = FuelStationDao()

    def getAllUsers(self):
        try:
            result = self.dao.getAllUsers()
            return ResponseApi(200, [r.to_dict() for r in result], "successful query")
        except Exception as e:
            return ResponseApi(500, str(e), "unsuccessful query")

    def createUser(self, newUser):
        try:
            # Validar si ya existe el correo o el nombre de usuario
            if self.dao.check_email_exists(newUser.email):
                return ResponseApi(400, None, "Email already exists")
            if self.dao.check_username_exists(newUser.username):
                return ResponseApi(400, None, "Username already exists")
            # Hashear la contraseña antes de guardarla en la BD
            hashed_password = generate_password_hash(
                newUser.password, method='sha256')
            newUser.password = hashed_password
            newUser.created_at = datetime.now()
            newUser.updated_at = datetime.now()
            result = self.dao.createUser(newUser)
            return ResponseApi(200, result.to_dict(), "successful query")
        except Exception as e:
            return ResponseApi(500, str(e), "unsuccessful query")

    def deleteUser(self, id):
        try:
            result = self.dao.deleteUser(id)
            return ResponseApi(200, result.to_dict(), "successful query")
        except Exception as e:
            return ResponseApi(500, str(e), "unsuccessful query")

    def updateUser(self, updatedUser):
        try:
            if not self.dao.getUserById(updatedUser.id_user):
                return ResponseApi(404, None, "User not found")
            # Validar si ya existe el correo o el nombre de usuario
            if self.dao.check_email_exists(updatedUser.email) and self.dao.getUserById(updatedUser.id_user).email != updatedUser.email:
                return ResponseApi(400, None, "Email already exists")
            if self.dao.check_username_exists(updatedUser.username) and self.dao.getUserById(updatedUser.id_user).username != updatedUser.username:
                return ResponseApi(400, None, "Username already exists")
            # Actualizar la contraseña si viene en la petición y hashearla antes de guardarla en la BD
            if updatedUser.password:
                hashed_password = generate_password_hash(
                    updatedUser.password, method='sha256')
                updatedUser.password = hashed_password
            updatedUser.updated_at = datetime.now()
            result = self.dao.updateUser(updatedUser)
            return ResponseApi(200, result.to_dict(), "successful query")
        except Exception as e:
            return ResponseApi(500, str(e), "unsuccessful query")

    def login(self, email, password):
        try:
            user = self.dao.getUserByEmail(email)
            # Validar si existe el correo en la BD y si la contraseña coincide con la almacenada en la BD
            if user and check_password_hash(user.password, password):
                token_data = {'email': email}
                token = jwt.encode(
                    {'exp': datetime.utcnow() + timedelta(minutes=30),
                     'iat': datetime.utcnow(), 'sub': email},
                    'secret_key',
                    algorithm='HS256'
                )
                return ResponseApi(200, {'token': token, 'user': user.to_dict()}, "successful login")
            else:
                return ResponseApi(401, None, "invalid credentials")
        except Exception as e:
            return ResponseApi(500, str(e), "unsuccessful login")

    def getAccess(self, idx):
        try:
            stations = UserSvc.getStations(self, id=idx)
            return ResponseApi(200, stations, "successful query")
        except Exception as e:
            return ResponseApi(500, str(e), "unsuccessful query")

    def getStations(self, id):
        try:
            if not self.dao.getUserById(id):
                return None
            else:
                infoUser = self.dao.getUserById(id)
                stations = []
                if (infoUser.is_admin == True):
                    aux = self.stationDao.getAllFuelStation()
                    for station in aux:
                        stations.append(station.to_dict())
                else:
                    access = self.daoAccess.getUserAccessById(id)
                    for aux in access:
                        station = self.stationDao.getById(
                            aux.id_fuel_station_fk)
                        stations.append(station.to_dict())
                return stations
        except Exception as e:
            return str(e)
