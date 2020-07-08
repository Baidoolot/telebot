from flask_security import UserMixin, RoleMixin
from flask_security import SQLAlchemySessionUserDatastore, Security 

from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.automap import automap_base


from app import app, db

#### Flask security -------------

roles_users = db.Table('roles_users', 
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')),
    )   

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))



user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
security = Security(app, user_datastore)

#### --------------------------

#### Flask admin -----------------

Base = automap_base()

class University(Base):
    __tablename__ = 'university'
    title = db.Column(db.String(50))

    def __repr__(self):
        return self.title

class Faculty(Base):
    __tablename__ = 'faculty'
    title = db.Column(db.String(50))

    def __repr__(self):
        return self.title


class Specialty(Base):
    __tablename__ = 'specialty'
    title = db.Column(db.String(100))

    def __repr__(self):
        return self.title

class Contact(Base):
    __tablename__ = 'contact'
    body = db.Column(db.String(100))

    def __repr__(self):
        return self.body

class Ort(Base):
    __tablename__ = 'ort'
    body = db.Column(db.String(100))

    def __repr__(self):
        return self.body


Base.prepare(db.engine, reflect=True)


##### --------------------

