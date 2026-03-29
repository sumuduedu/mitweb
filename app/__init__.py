from flask import Flask
from .extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    from .routes.courses import courses_bp
    app.register_blueprint(courses_bp)

    return app
