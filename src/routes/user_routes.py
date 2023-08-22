from flask import Blueprint, request

# from flask_jwt_extended import jwt_required,get_jwt_identity
from controllers.user_controller import get_all, get_user, get_allfavorites, get_userfavorites
user_routes = Blueprint("user", __name__)

@user_routes.route('/', methods=['GET'])
def users():
    if request.method == 'GET':
        return get_all()

@user_routes.route('/favorites', methods=['GET'])
def usersfavorites():
    if request.method == 'GET':
        return get_allfavorites()


@user_routes.route('/<int:id>', methods=['GET'])
def user(id):
    if request.method == 'GET':
        return get_user(id)
 
@user_routes.route('/favorites/<int:id>', methods=['GET'])
def userfavorites(id):
    if request.method == 'GET':
        return get_userfavorites(id)
