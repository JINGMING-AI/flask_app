from flask import Blueprint,request,Response,jsonify

from api.user_api import *

user = Blueprint('user',__name__)

@user.route('/list')
def user_list():
    users = User_list()
    return jsonify(users)

# GET 参数 username  password phone others
@user.route('/reg',methods=['GET'])
def reg():
    username = request.args.get("username")
    password = request.args.get("password")
    phone = request.args.get("phone")
    others = request.args.get("others")
    users = User_reg({
        "username":username,
        "password":password,
        "phone":phone,
        "others":others
    })
    return jsonify(users)

# GET 参数 username  password phone others
@user.route('/login',methods=['GET'])
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    result = User_login(username,password)
    return str(result)