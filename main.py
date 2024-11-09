from flask import Flask
from src.api import api_endpoint


host = '127.0.0.1'
port = 5000

app = Flask(__name__)
app.register_blueprint(api_endpoint, url_prefix='/api')

if __name__ == '__main__':
    app.run(host=host, port=port)
