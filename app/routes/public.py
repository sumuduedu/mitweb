from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models import Course

# Create blueprint ONCE
public_bp = Blueprint('public', __name__)

# -------------------------
# HOME PAGE
# -------------------------
@public_bp.route("/")
def home():
    courses = Course.query.limit(3).all()
    return render_template("public/home.html", courses=courses)

# -------------------------
# COURSES PAGE
# -------------------------
@public_bp.route("/courses")
def courses():
    courses = Course.query.all()
    return render_template("public/courses.html", courses=courses)

# -------------------------
# ABOUT PAGE
# -------------------------
@public_bp.route("/about")
def about():
    return render_template("public/about.html")

# -------------------------
# CONTACT PAGE
# -------------------------
@public_bp.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        print(name, email, message)  # debug

        flash("Message sent successfully!", "success")
        return redirect(url_for("public.contact"))

    return render_template("public/contact.html")
