from flask import Flask

from handler.user import user

from db_config import app
# app = Flask(__name__)

from flask_cors import CORS
CORS(app,supports_credentials=True)

app.register_blueprint(user,url_prefix="/user")

@app.route('/')
def helle():
    return 'hello'

if __name__ == '__main__':
    app.run(host="127.0.0.1",port='5000')