# init.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import logout_user, login_required, current_user

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
migrate = Migrate()
admin = Admin(name='Project', template_mode='bootstrap4')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '9OLWxNDhfvhjvj4o83j4K4iu3545860nhgkopO'

    # For XAMPP
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

    #SQLALCHEMY DATABASE URI Format         'db+driver://username:password@host/name_of_db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://phpmyadmin:root@127.0.0.1/db_urlcheck'

    # For Sqlite3 db
    # app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_urlcheck.sqlite3'


    db.init_app(app)
    migrate.init_app(app, db)
    login_manager = LoginManager()
    login_manager.login_view = 'guest.login'
    login_manager.init_app(app)
    from Project.Models.models import Users
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return Users.query.get(int(user_id))

    # blueprint for guest routes in our app
    from .Guest import guest as guest_blueprint
    app.register_blueprint(guest_blueprint.guest)


    # blueprint for admin routes in our app
    # from .Admin import admin as admin_blueprint
    # app.register_blueprint(admin_blueprint.adminNew_blueprint)

    admin.init_app(app)

    # blueprint for user routes in our app
    from .User import user as user_blueprint
    app.register_blueprint(user_blueprint.user)

    # blueprint for non-auth parts of app
    from Project.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app, admin

# app = create_app()
