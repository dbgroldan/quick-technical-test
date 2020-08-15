from dotenv import load_dotenv
from flask import Flask
from user.user_routes import cons_user_blueprint
from config.settings import getConfig
from utils.validation_data import buildResponse

# Config Server
config = getConfig()
port = config.get('port_http')
host = config.get('host')

# Server Application
app = Flask(__name__)
server_key = 'developedbydbgroldan'
app.secret_key = server_key

# Routes
@app.route('/', methods = ['GET'])
def index():
    content = 200, {'message': 'Server started successfully'}
    return buildResponse('application/json', content)

app.register_blueprint(cons_user_blueprint(server_key), url_prefix='')

# Error Routes
@app.errorhandler(404)
def not_found(e):
    content = 200, {'error': 'Not found'}
    return buildResponse('application/json', content)

# Application initialization
if __name__ == '__main__':
    print('Server is listening in port: ' + str(port))
    app.run(port=port, debug=True, host = host)
