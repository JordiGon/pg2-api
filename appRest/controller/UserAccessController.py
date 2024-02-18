from flask import Blueprint, jsonify, request
from appRest.service.UserAcessSvc import UserAccessSvc
from appRest.model.UserAccessModel import UserAccess


class UserAccessController:
    def __init__(self):
        self.blueprint = Blueprint(
            'UserAccess_Controller', __name__, url_prefix='/user-access')

        @self.blueprint.route('/get-all', methods=['GET'])
        def getAllData():
            svc = UserAccessSvc()
            response = svc.getAllUserAccess()
            return jsonify(response.to_dict())

        @self.blueprint.route('/create', methods=['POST'])
        def createUserAccess():
            data = request.get_json()
            user_access = UserAccess(**data)
            svc = UserAccessSvc()
            response = svc.createUserAccess(user_access)
            return jsonify(response.to_dict())

        @self.blueprint.route('/delete/<int:id>', methods=['DELETE'])
        def deleteUserAccess(id):
            svc = UserAccessSvc()
            response = svc.deleteUserAccess(id)
            return jsonify(response.to_dict())

        @self.blueprint.route('/update', methods=['PUT'])
        def updateUserAccess():
            data = request.get_json()
            user_access = UserAccess(**data)
            svc = UserAccessSvc()
            response = svc.updateUserAccess(user_access)
            return jsonify(response.to_dict())
