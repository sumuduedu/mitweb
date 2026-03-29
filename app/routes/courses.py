from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Course
from app.extensions import db

courses_bp = Blueprint('courses', __name__)

@courses_bp.route("/")
def list_courses():
    courses = Course.query.all()
    return render_template("courses/list.html", courses=courses)

@courses_bp.route("/add", methods=["GET", "POST"])
def add_course():
    if request.method == "POST":
        course = Course(
            name=request.form["name"],
            duration=request.form["duration"],
            fee=request.form["fee"]
        )
        db.session.add(course)
        db.session.commit()
        return redirect(url_for("courses.list_courses"))

    return render_template("courses/add.html")

@courses_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_course(id):
    course = Course.query.get_or_404(id)

    if request.method == "POST":
        course.name = request.form["name"]
        course.duration = request.form["duration"]
        course.fee = request.form["fee"]

        db.session.commit()
        return redirect(url_for("courses.list_courses"))

    return render_template("courses/edit.html", course=course)

@courses_bp.route("/delete/<int:id>")
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()

    return redirect(url_for("courses.list_courses"))
