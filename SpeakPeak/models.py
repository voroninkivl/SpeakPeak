from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    teacher = db.Column(db.Integer, default=0, nullable=False)

    # Связь с Folder
    folders = db.relationship("Folder", backref="user", lazy=True)

    # Связь с Record
    records = db.relationship("Record", backref="user", lazy=True)

class Folder(db.Model):
    __tablename__ = "folder"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

class Record(db.Model):
    __tablename__ = "record"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    trash = db.Column(db.Integer, default=0, nullable=False)
    length = db.Column(db.Float, nullable=True)
    audio_file = db.Column(db.String(255), nullable=True)
    datetime = db.Column(db.DateTime, default=datetime.utcnow)

    # Связь "Record -> Mistake"
    mistakes = db.relationship("Mistake", backref="record", lazy=True)

class Mistake(db.Model):
    __tablename__ = "mistake"
    id = db.Column(db.Integer, primary_key=True)
    record_id = db.Column(db.Integer, db.ForeignKey("record.id"), nullable=False)
    comment = db.Column(db.String(255), nullable=True)
    time_of_mistake = db.Column(db.Float, nullable=True)
    type = db.Column(db.Integer, nullable=True)
