from flask import Blueprint, jsonify, request
import traceback

#logger
from src.utils.Logger import Logger

api = Blueprint('user_blueprint', __name__)

@api.route('/register')
def register():
    return "Welcome to user endpoint", 200