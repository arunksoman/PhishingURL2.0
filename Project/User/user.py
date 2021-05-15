from flask import Blueprint, render_template, session, request, url_for, redirect, flash, jsonify
from flask_login import logout_user, current_user
from ..checker import url_checker
from ..Models.models import *

user = Blueprint('user', __name__, template_folder='user_template', static_folder='user_static', url_prefix='/user')

@user.route('homepage')
# @login_required
def user_homepage():
    return render_template("user_homepage.html")

@user.route('test', methods=["POST"])
def url_check():
    if request.method == "POST":
        url = request.form.get("url")
        check_url = Whitelist_url.query.filter_by(white_url=url).first()
        check_user = UserBlocked.query.filter_by(black_url=url).filter_by(userid=current_user.id).first()
        mal_url_check = Blacklist_url.query.filter_by(black_url=url).first()
        user_blocked = False
        admin_blocked = False
        if check_user:
            if check_user.black_url == url:
                user_blocked = True
        if mal_url_check:
            if mal_url_check.black_url == url:
                admin_blocked = True

        # print(check_url.white_url)
        if check_url:
            if check_url.white_url == url:
                return render_template("user_result.html", user_url=url, url="benign", css_class="success")
        if user_blocked or admin_blocked:
            return render_template("user_result.html", url="malicious", css_class="error")
        result = url_checker(url)
        if result:
            print("hai")
            return render_template("user_result.html", url="malicious", css_class="error")
        else:
            return render_template("user_result.html", url="benign", user_url=url, css_class="success")
@user.route("/block_url", methods=["GET", "POST"])
def block_url():
    if request.method == "POST":
        block_url = request.form.get("url_address")
        uid = current_user.id
        url_for_blockList = UserBlocked(black_url=block_url, userid=uid)
        db.session.add(url_for_blockList)
        db.session.commit()
        return redirect(url_for('user.block_url'))
    all_blocked = UserBlocked.query.all()
    return render_template("block_url.html", all_blocked=all_blocked)

@user.route('/delete',methods = ['POST', 'GET'])
def dataRemove():
   if request.method == 'GET':
        dprimary = request.args.get('dprimary')
        delete_this = UserBlocked.query.filter_by(id=dprimary).first()
        db.session.delete(delete_this)
        db.session.commit()
        return redirect(url_for("user.block_url"))
