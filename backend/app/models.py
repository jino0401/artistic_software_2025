from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(128), nullable=False)

class Lecture(db.Model):
    __tablename__ = 'lectures'
    id = db.Column(db.Integer, primary_key=True)
    lecture_id = db.Column(db.String(20), unique=True, nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    professor = db.Column(db.String(50), nullable=False)
    weekday = db.Column(db.String(10), nullable=False)
    start_time = db.Column(db.String(10), nullable=False)
    end_time = db.Column(db.String(10), nullable=False)
    room = db.Column(db.String(50), nullable=False)
    semester = db.Column(db.String(20), nullable=False)

class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    lecture_id = db.Column(db.Integer, db.ForeignKey('lectures.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('enrollments', cascade='all, delete-orphan'))
    lecture = db.relationship('Lecture', backref=db.backref('enrollments', cascade='all, delete-orphan'))

class Attendance(db.Model):
    __tablename__ = 'attendances'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    lecture_id = db.Column(db.Integer, db.ForeignKey('lectures.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    recorded_at = db.Column(db.DateTime, nullable=False)

    user = db.relationship('User', backref=db.backref('attendances', cascade='all, delete-orphan'))
    lecture = db.relationship('Lecture', backref=db.backref('attendances', cascade='all, delete-orphan'))
