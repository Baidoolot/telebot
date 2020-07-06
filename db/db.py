from peewee import *

user = 'newuser'
password = 'password'
db_name = 'telebot'
 
dbhandle = MySQLDatabase(
    db_name, user=user,
    password=password,
    host='localhost',
    charset='utf8mb4'
)

