from flask import redirect, url_for, request

from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, AdminIndexView

from flask_security import current_user 

from app import app, db
from models import *




#####  Flask admin ----------


class AdminView(ModelView):
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))



admin = Admin(app, template_mode='bootstrap3')


admin.add_view(AdminView(University, db.session))
admin.add_view(AdminView(Faculty, db.session))
admin.add_view(AdminView(Specialty, db.session))
admin.add_view(AdminView(Contact, db.session))
admin.add_view(AdminView(Ort, db.session))


###### ----------------