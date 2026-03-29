from flask import Blueprint, render_template, request, redirect, url_for
from app.models import User
from app.extensions import db
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash


auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()

        if user and check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("courses.list_courses"))

    return render_template("auth/login.html")

@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
