from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.extensions import db
from app.models import Student
from app.utils.permissions import admin_required

students_bp = Blueprint('students', __name__, url_prefix="/students")

# LIST
@students_bp.route("/")
@login_required
@admin_required
def list_students():
    students = Student.query.all()
    return render_template("students/list.html", students=students)

# ADD
@students_bp.route("/add", methods=["GET", "POST"])
@login_required
@admin_required
def add_student():
    if request.method == "POST":
        student = Student(
            name=request.form["name"],
            email=request.form["email"],
            phone=request.form["phone"]
        )
        db.session.add(student)
        db.session.commit()

        flash("Student added successfully", "success")
        return redirect(url_for("students.list_students"))

    return render_template("students/add.html")

# EDIT
@students_bp.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit_student(id):
    student = Student.query.get_or_404(id)

    if request.method == "POST":
        student.name = request.form["name"]
        student.email = request.form["email"]
        student.phone = request.form["phone"]

        db.session.commit()

        flash("Student updated", "success")
        return redirect(url_for("students.list_students"))

    return render_template("students/edit.html", student=student)

# DELETE
@students_bp.route("/delete/<int:id>", methods=["POST"])
@login_required
@admin_required
def delete_student(id):
    student = Student.query.get_or_404(id)

    db.session.delete(student)
    db.session.commit()

    flash("Student deleted", "warning")
    return redirect(url_for("students.list_students"))
