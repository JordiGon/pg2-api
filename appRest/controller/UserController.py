from flask import Blueprint, jsonify, request
from appRest.service.UserSvc import UserSvc
from appRest.model.UserModel import User


class UserController:
    def __init__(self):
        self.blueprint = Blueprint(
            'user-controller', __name__, url_prefix='/user')

        @self.blueprint.route('/get-all', methods=['GET'])
        def get_all_users():
            svc = UserSvc()
            response = svc.getAllUsers()
            return jsonify(response.to_dict())

        @self.blueprint.route('/create', methods=['POST'])
        def create_user():
            data = request.get_json()
            user = User(**data)
            svc = UserSvc()
            response = svc.createUser(user)
            return jsonify(response.to_dict())

        @self.blueprint.route('/delete/<int:id>', methods=['DELETE'])
        def delete_user(id):
            svc = UserSvc()
            response = svc.deleteUser(id)
            return jsonify(response.to_dict())

        @self.blueprint.route('/update', methods=['PUT'])
        def update_user():
            data = request.get_json()
            user = User(**data)
            svc = UserSvc()
            response = svc.updateUser(user)
            return jsonify(response.to_dict())

        @self.blueprint.route('/login', methods=['POST'])
        def login():
            data = request.get_json()
            svc = UserSvc()
            response = svc.login(data['email'], data['password'])
            return jsonify(response.to_dict())

        @self.blueprint.route('/get-access/<int:id>', methods=['GET'])
        def getAccess(id):
            svc = UserSvc()
            response = svc.getAccess(id)
            return jsonify(response.to_dict())
