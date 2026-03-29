from flask import Blueprint, render_template, request, redirect, url_for, abort, flash
from flask_login import login_required
from app.models import Course
from app.extensions import db
from app.utils.permissions import admin_required

courses_bp = Blueprint('courses', __name__)

# 🔹 List
@courses_bp.route("/")
@login_required
@admin_required
def list_courses():
    courses = Course.query.all()
    return render_template("courses/list.html", courses=courses)

# 🔹 Add
@courses_bp.route("/add", methods=["GET", "POST"])
@login_required
@admin_required
def add_course():
    if request.method == "POST":
        name = request.form["name"]

        if not name:
            flash("Course name is required", "danger")
            return redirect(url_for("courses.add_course"))

        course = Course(
            name=name,
            duration=request.form["duration"],
            fee=request.form["fee"]
        )

        db.session.add(course)
        db.session.commit()

        flash("Course added successfully", "success")
        return redirect(url_for("courses.list_courses"))

    return render_template("courses/add.html")

# 🔹 Edit
@courses_bp.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit_course(id):
    course = Course.query.get_or_404(id)

    if request.method == "POST":
        name = request.form["name"]

        if not name:
            flash("Course name is required", "danger")
            return redirect(url_for("courses.edit_course", id=id))

        course.name = name
        course.duration = request.form["duration"]
        course.fee = request.form["fee"]

        db.session.commit()

        flash("Course updated successfully", "success")
        return redirect(url_for("courses.list_courses"))

    return render_template("courses/edit.html", course=course)

# 🔹 Delete (POST only)
@courses_bp.route("/delete/<int:id>", methods=["POST"])
@login_required
@admin_required
def delete_course(id):
    course = Course.query.get_or_404(id)

    db.session.delete(course)
    db.session.commit()

    flash("Course deleted successfully", "warning")
    return redirect(url_for("courses.list_courses"))
