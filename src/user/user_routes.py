# -*- coding: utf-8 -*-
import os
from flask import Blueprint, jsonify, request, make_response
from werkzeug.utils import secure_filename
from user.user_service import UserService
from config.settings import getConfig
from utils.validation_data import buildResponse, errorContent, removePass, removePassSet
from utils.token_verification import token_required

content_type = 'application/json'

def cons_user_blueprint(secret):
    user_bp = Blueprint('user_bp', __name__)
    user_control = UserService()

    @user_bp.route('/login', methods = ['POST'])
    def login():
        if request.method == 'POST':
            if request.content_type == content_type:
                requestJson = request.get_json(force = True)
                content = removePass(user_control.login(requestJson, secret))
            else:
                content = errorContent()
            return buildResponse('application/json', content)

    @user_bp.route('/users', methods = ['POST'])
    @token_required
    def register(current_user):
        if request.method == 'POST':
            if request.content_type == content_type:
                requestJson = request.get_json(force = True)
                content = removePass(user_control.add_user(requestJson))
            else:
                content = errorContent()
            return buildResponse('application/json', content)

    @user_bp.route('/users/<id>', methods = ['PUT', 'PATCH'])
    @token_required
    def update(current_user, id):
        method = request.method
        if method == 'PUT' or method == 'PATCH':
            if request.content_type == content_type:
                requestJson = request.get_json(force = True)
                content = removePass(user_control.update_user(id, requestJson))
            else:
                content = errorContent()
            return buildResponse('application/json', content)

    @user_bp.route('/users', methods = ['GET'])
    @token_required
    def get_all(current_user):
        content = removePassSet(user_control.get_all()) if request.content_type == content_type else errorContent()
        print('********', content)
        return buildResponse('application/json', content)

    @user_bp.route('/users/<id>', methods = ['GET'])
    @token_required
    def get(current_user, id):
        content = removePass(user_control.get(id)) if request.content_type == content_type else errorContent()
        return buildResponse('application/json', content)

    @user_bp.route('/users/<id>', methods = ['DELETE'])
    @token_required
    def delete(current_user, id):
        content = removePass(user_control.delete(id)) if request.content_type == content_type else errorContent()
        return buildResponse('application/json', content)

    return user_bp
