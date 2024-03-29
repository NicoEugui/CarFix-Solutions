from flask import Blueprint, jsonify, request

import traceback

#logger
from src.utils.Logger import Logger

api = Blueprint('index_blueprint', __name__)

@api.route('/')
def index():
    try:
        Logger.add_to_log("info", "{} {}".format(request.method, request.path))
        return "Welcome to the API. Version 1.0"
    except Exception as e:
        Logger.add_to_log("error", str(e))
        Logger.add_to_log("error", traceback.format_exc())

        response = jsonify({'message': "Internal Server Error", 'success': False})
        return response, 500