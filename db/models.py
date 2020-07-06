from peewee import *
import datetime
from .db import *


class BaseModel(Model):
    class Meta:
        database = dbhandle
 
 
class University(BaseModel):
    id = PrimaryKeyField(null=False)
    title = CharField(max_length=100)
    body = TextField()
    city = CharField(max_length=100)
    
 
    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())
 
    class Meta:
        db_table = "university"
        order_by = ('created_at',)


class Faculty(BaseModel):
    id = PrimaryKeyField(null=False)
    title = CharField(max_length=100)
    univer = ForeignKeyField(University, backref='faculties')

    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())    

    class Meta:
        order_by = ('id',)

class Specialty(BaseModel):
    id = PrimaryKeyField(null=False)
    title = CharField(max_length=100,null=False)
    faculty = ForeignKeyField(Faculty, backref='specialties')

    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())   

class Ort(BaseModel):
    id = PrimaryKeyField(null=False)
    body = CharField(max_length=255)
    ort = ForeignKeyField(Faculty, backref='ort')

class Contact(BaseModel):
    id = PrimaryKeyField(null=False)
    body = TextField()
    contacts = ForeignKeyField(University, backref='contacts')

