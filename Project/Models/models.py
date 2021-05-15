from flask_login import UserMixin
from Project import db
# from flask_admin.contrib.sqla import ModelView

# Define User data-model
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # User Authentication fields
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    # Relationships
    roles = db.relationship('Roles', secondary='user_roles')
    user_blacklist = db.relationship('UserBlocked', backref='user_blocked_urls', foreign_keys='UserBlocked.userid')

# Define the Role data-model
class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

# Define the UserRoles association table
class UserRoles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'))


class Whitelist_url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    white_url = db.Column(db.String(50), nullable=False, unique=True)

class Blacklist_url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    black_url = db.Column(db.String(50), nullable=False, unique=True)

class UserBlocked(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    black_url = db.Column(db.String(50), nullable=False, unique=False)
    userid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
