import peewee
from models import *
 
if __name__ == '__main__':
    try:
        dbhandle.connect()
        University.create_table()
        Faculty.create_table()
        Specialty.create_table()
        Contact.create_table()
        Ort.create_table()
    except peewee.InternalError as px:
        print(str(px))