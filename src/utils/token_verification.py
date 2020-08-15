import jwt
from functools import wraps
from flask import request
from user.user_service import UserService
from utils.validation_data import buildResponse

# Decorator dan indicate than is token required
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            content = 401, {"error":'Unauthorized, token is missing'}
            return buildResponse('application/json', content)

        secret = 'developedbydbgroldan'
        try:
            data = jwt.decode(token, secret)
            code, user = UserService().get(data.get('id'))
            current_user = user if code == 200 else False
            if not current_user:
                content = 401, 'Unauthorized, token is invalid'
                return buildResponse('application/json', content)
        except Exception as e:
            content = 401, {"error":'Unauthorized, token is invalid'}
            return buildResponse('application/json', content)
        return f(current_user, *args, **kwargs)
    return decorated
