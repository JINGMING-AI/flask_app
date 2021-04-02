from db_config import db_init as db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=True)
    others = db.Column(db.String(255), nullable=True)
    
    def __repr__(self):
        return '<User %s>' % self.username


# models
# user
# goods