from operation.db_operation import *

from utils.data_proccess import *

# 用户相关操作的方法
def User_list():
    user_operation = User_Operation()
    re_data = user_operation._all()
    re_data = Class_To_Data(re_data,user_operation.__fields__)
    return re_data

# 用户注册方法
def User_reg(kwargs):
    user_operation = User_Operation()
    re_data = user_operation._reg(kwargs)
    return re_data

# 用户登录方法
def User_login(username,password):
    user_operation = User_Operation()
    re_data = user_operation._login(username,password)
    return re_data