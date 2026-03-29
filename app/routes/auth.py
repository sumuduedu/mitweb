from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import User
from app.extensions import db
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask_login import current_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            # 🔥 Redirect ALL roles to dashboard
            return redirect(url_for("dashboard.dashboard"))

        else:
            flash("Invalid username or password", "danger")

    return render_template("auth/login.html")


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard.dashboard"))

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]

        # Check if user exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists", "danger")
            return redirect(url_for("auth.signup"))

        # Create user
        hashed_pw = generate_password_hash(password)

        user = User(
            username=username,
            password=hashed_pw,
            role=role
        )

        db.session.add(user)
        db.session.commit()

        flash("Account created successfully", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/signup.html")
