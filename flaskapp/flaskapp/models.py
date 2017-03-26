from flaskapp import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    id = db.Column('user_id',db.Integer , primary_key=True)
    username = db.Column('username', db.String(20), unique=True , index=True)
    password = db.Column('password' , db.String(10))
    email = db.Column('email',db.String(50),unique=True , index=True)
    registered_on = db.Column('registered_on' , db.DateTime)
 
    def __init__(self , username ,password , email):
        self.username = username
        self.password = password
        self.email = email
        self.registered_on = datetime.utcnow()
 
    def is_authenticated(self):
        return True
 
    def is_active(self):
        return True
 
    def is_anonymous(self):
        return False
 
    def get_id(self):
        return unicode(self.id)
 
    def __repr__(self):
        return '<User %r>' % (self.username)

    def check_password(self, password):
        password_matched = False
        if self.password == password:
            password_matched = True
        return password_matched

class Orders(db.Model):
    __tablename__ = "orders"
    id = db.Column('id',db.Integer , primary_key=True)
    order_status = db.Column('order_status' , db.String(10))
    order_id = db.Column('order_id' , db.String(10))    
    product_name = db.Column('product_name', db.String(200))
    product_url = db.Column('product_url', db.String(400))
    cost_price = db.Column('cost_price', db.Float)
    created_on = db.Column('created_on' , db.DateTime)
 
    """def __init__(self , order_status ,product_name , product_url, cost_price):
        self.order_status = order_status
        self.order_id = '7777777777777777777 '
        self.product_name = product_name
        self.cost_price = cost_price
        self.created_on = datetime.utcnow()"""