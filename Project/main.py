# main.py

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from flask_login import logout_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')



@main.route("/logout")
def logout():
    logout_user()
    flash("Logged out successfully.")
    return redirect(url_for("guest.login"))