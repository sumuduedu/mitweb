def get_menu(role):
    base_menu = [
        {"name": "Dashboard", "url": "dashboard.dashboard"}
    ]

    role_menus = {
        "admin": [
            {"name": "Courses", "url": "courses.list_courses"},
            {"name": "Students", "url": "students.list_students"},  # ✅ FIXED
            {"name": "Teachers", "url": "#"},
            {"name": "Reports", "url": "#"},
        ],
        "teacher": [
            {"name": "My Courses", "url": "courses.list_courses"},
            {"name": "My Students", "url": "#"},
            {"name": "Attendance", "url": "#"},
        ],
        "student": [
            {"name": "My Courses", "url": "#"},
            {"name": "Assignments", "url": "#"},
            {"name": "Results", "url": "#"},
        ],
        "parent": [
            {"name": "Child Progress", "url": "#"},
            {"name": "Attendance", "url": "#"},
        ],
        "staff": [
            {"name": "Admin Tasks", "url": "#"},
            {"name": "Support", "url": "#"},
        ],
    }

    return base_menu + role_menus.get(role, [])
