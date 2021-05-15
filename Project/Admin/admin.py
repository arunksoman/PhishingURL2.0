from flask import Blueprint, render_template, session, request, url_for, redirect, flash, jsonify
from flask_login import logout_user, login_required, current_user
from ..Models.models import *
from Project import db, admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose, AdminIndexView
import pandas as pd
import numpy as np
from ..configuration import *
from ..utils.dataset_preprocessing import preprocessing


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        if current_user.is_authenticated and not current_user.is_anonymous:
            user = Users.query.filter_by(id=current_user.id).first()
            if user.roles[0].name == 'Admin':
                return True
            else:
                return False

admin = Admin(app, name='Project', index_view=MyAdminIndexView(), template_mode='bootstrap3')


class AdminModelView(ModelView):
    def is_accessible(self):
        if current_user.is_authenticated and not current_user.is_anonymous:
            user = Users.query.filter_by(id=current_user.id).first()
            if user.roles[0].name == 'Admin':
                return True
            else:
                return False
        # return current_user.is_authenticated and not current_user.is_anonymous

class AdminBaseView(BaseView):
    def is_accessible(self):
        if current_user.is_authenticated and not current_user.is_anonymous:
            user = Users.query.filter_by(id=current_user.id).first()
            # print(user.roles[0].name)
            if user.roles[0].name == 'Admin':
                return True
            else:
                return False
        # return current_user.is_authenticated and not current_user.is_anonymous
# admin = Blueprint('admin_blueprint', __name__, template_folder='ad_template', static_folder='ad_static', url_prefix='/admin')
# adminNew_blueprint = Blueprint('adminNew_blueprint', __name__, template_folder='ad_template', url_prefix='/admin')
class DatapreprocessView(AdminBaseView):
    @expose('/')
    def preprocess_dataset(self):
        urldata = pd.read_csv(DATASET_PATH)
        # print(urldata.head(10))

        preprocessed_df = preprocessing(urldata)
        # print(preprocessed_df.head())
        preprocessed_df.to_csv(PREPROCESSED_DATASET)
        print("Test Success")
        return self.render('admin/preprocess.html', endpoint='test')
class LogoutAdmin(AdminBaseView):
    @expose('/')
    def logoutAdmin(self):
        return redirect(url_for("main.logout"))


admin.add_view(AdminModelView(Whitelist_url,db.session, name='Whitelist URL'))
admin.add_view(AdminModelView(Blacklist_url, db.session, name='Blacklist URL'))
admin.add_view(DatapreprocessView(name='Dataset Preprocessing'))
admin.add_view(LogoutAdmin(name='Logout'))
