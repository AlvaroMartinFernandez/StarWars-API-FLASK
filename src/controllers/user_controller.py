from flask import current_app, jsonify
from models import User
from schema import UserSchema,UserSchemaExtend
from utils import db
from sqlalchemy.orm import joinedload




def get_all():
    try: 
        query= db.select(User).order_by(User.id)
        users = db.session.execute(query).scalars().all()
        if len(users) == 0:
            return jsonify({"message": "No hay usuarios"}), 404
        user_schema = UserSchema(many=True)
        data = user_schema.dump(users)
        return jsonify(data),200
    except Exception as error:
        return jsonify({"message": "Error al obtener el usuario", "error": str(error)})    
def get_user(id):
    try:
        query= db.select(User).where(User.id == id)
        user = db.session.execute(query).scalars().all()
        if len(user) == 0:
            return jsonify({"message": "Usuario no encontrado"}), 404
        user_schema = UserSchema(many=True)
        data = user_schema.dump(user)
        return jsonify(data),200
    except Exception as error:
        return jsonify({"message": "Error al obtener el usuario", "error": str(error)})

def get_allfavorites():
    try: 
        query= db.select(User).order_by(User.id)
        users = db.session.execute(query).scalars().all()
        if len(users) == 0:
            return jsonify({"message": "No hay usuarios"}), 404
        user_schema = UserSchemaExtend(many=True)
        data = user_schema.dump(users)
        return jsonify(data),200
    except Exception as error:
        return jsonify({"message": "Error al obtener el usuario", "error": str(error)})    
def get_userfavorites(id):
    try:
        query= db.select(User).where(User.id == id)
        user = db.session.execute(query).scalars().all()
        if len(user) == 0:
            return jsonify({"message": "Usuario no encontrado"}), 404
        user_schema = UserSchemaExtend(many=True)
        data = user_schema.dump(user)
        return jsonify(data),200
    except Exception as error:
        return jsonify({"message": "Error al obtener el usuario", "error": str(error)})
