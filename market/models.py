from market import db,login_manager
from market import bcrypt
from flask_login import UserMixin
from datetime import datetime
import json

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    PRN=db.Column(db.Integer(), nullable=False, unique=True)
    Password = db.Column(db.String(length=60), nullable=False)
    # budget=db.Column(db.integer(),nullable=False,defalut=10)
    # items=db.relationship('Item',backref='owned_user',lazy=True)
    
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.Password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    def check_password_correction(self, attempted_passward):
        return bcrypt.check_password_hash(self.Password,attempted_passward)

    def __repr__(self):
        return f'User{self.name}' 

         
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    # owner= db.Column(db.Integer(),db.ForeignKey('User.id'))

    def __repr__(self):
        return f'Item{self.name}'  

class Bill(db.Model):
    name=db.Column( db.String())
    quantity = db.Column(db.Integer())
    price=db.Column( db.Integer())
    Total=db.Column(db.Integer(),primary_key=True)
    date=db.Column(db.DateTime,default=datetime.utcnow)
        
    def __repr__(self):
        return f'Bill{self.Total}'  
