# -*- coding: utf-8 -*-
import jwt, datetime, uuid
from werkzeug.security import generate_password_hash, check_password_hash
from database.postg_connection import Connection
from database.postg_crud import ObjectDAO
from config.settings import getConfig
from utils.validation_data import existEmail


config = getConfig()
db_data = config.get('db_config')
db_config = 'dbname=%s user=%s host=%s port=%s password=%s'%db_data

db_tbl = config.get('db_tables_path')

class UserService:
    """docstring forUserService."""

    def __init__(self):
        connection = Connection(db_config)
        connection.createTables(db_tbl)
        self.user_control = ObjectDAO(connection, 'user_schema.user')

    def login(self, data, secret):
        user = existEmail(data.get('email'), self.user_control)[0]
        if user:
            if check_password_hash(user.get('password'), data.get('password')):
                expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                payload = {
                    'id': user.get('id'),
                    'first_name': user.get('first_name'),
                    'last_name': user.get('last_name'),
                    'exp' : expiration
                }
                token = jwt.encode(payload, secret, algorithm='HS256')
                user['token'] = token.decode('UTF-8')
                return 200, user
        return 401, {'error': 'Error in user or password'}

    def add_user(self, data):
        if not existEmail(data.get('email'), self.user_control):
            data['token'] =  str(uuid.uuid1())
            data['password'] = generate_password_hash(data.get('password'),
                method='pbkdf2:sha256',
                salt_length=10)
            new_id = self.user_control.add(data)
            if new_id:
                user = self.user_control.findById(str(new_id))
                return 201, user
        else:
            return 409, {'error': 'Account with email exist'}
        return 400, {'error': 'Bad Request'}

    def update_user(self, id, data):
        if not existEmail(data.get('email'), self.user_control):
            filt = {
                'and': [
                    {
                        'condition': '=',
                        'param': 'id',
                        'value': id
                    }
                    ]}
            if self.user_control.update(data, filt):
                return 200, self.user_control.findById(id)
        else:
            return 409, {'error': 'Account with email exist'}
        return 400, {'error': 'Bad Request'}

    def get_all(self):
        users = self.user_control.findAll()
        return 200, users

    def get(self, id):
        user = self.user_control.findById(str(id))
        if user:
            return 200, user
        return 404, {'error': 'Not Found'}

    def delete(self, id):
        user = self.user_control.findById(id)
        if user:
            if self.user_control.delete(id):
                return 200, user
            return 400, {'error': 'Bad Request'}
        return 404, {'error': 'Not Found'}
