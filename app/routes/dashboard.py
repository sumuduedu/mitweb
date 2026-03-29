from flask import Blueprint, render_template
from flask_login import login_required, current_user

# ✅ FIRST define blueprint
dashboard_bp = Blueprint('dashboard', __name__)

# ✅ THEN use it
@dashboard_bp.route("/dashboard")
@login_required
def dashboard():
    role = current_user.role

    template_map = {
        "admin": "dashboard/admin.html",
        "teacher": "dashboard/teacher.html",
        "student": "dashboard/student.html",
        "parent": "dashboard/parent.html",
        "staff": "dashboard/staff.html"
    }

    return render_template(template_map.get(role, "dashboard/default.html"))
