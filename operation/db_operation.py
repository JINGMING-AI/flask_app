from models.models import *

class User_Operation():
    def __init__(self):
        self.__fields__ = ['id',
                           'username',
                           'password',
                           'phone',
                           'others']
    def _all(self):
        user_data = User.query.all()
        return user_data
                             
        

    def _reg(self,kwargs):
        me = User(**kwargs)
        db.session.add(me)
        db.session.commit()
        return "success"    
    def _login(self,username,password):
        user_data = User.query.filter_by(username=username).first()
        # print(user_data.password)
        return user_data.password
# db_operation

# user_operation
# goods_operation