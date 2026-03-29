from .extensions import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(50))
    fee = db.Column(db.Float)

    def __repr__(self):
        return f"<Course {self.name}>"
