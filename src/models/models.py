from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

db = SQLAlchemy()


# DONE:
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False, default='user')
    role = db.Column(db.String(25), nullable=False, default='user')

    # Relationships
    user_data = db.relationship('UserData', back_populates='user', uselist=False)

    def __repr__(self):
        return '{}'.format(self.email)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "is_active": self.is_active,
            "role": self.role
        }

# DONE:
class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    firstname = db.Column(db.String(50), unique=False, nullable=False)
    lastname = db.Column(db.String(50), unique=False, nullable=False)
    address = db.Column(db.String(255), unique=False, nullable=False)
    phone = db.Column(db.String(60), unique=True, nullable=False)

    # Relationships
    user = db.relationship(User)

    def __repr__(self):
        return '{} {}'.format(self.firstname, self.lastname)
    
    def serialize(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "address": self.address,
            "phone": self.phone
        }