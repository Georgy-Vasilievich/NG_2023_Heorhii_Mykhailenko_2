"""SQLAlchemy models"""

from sqlalchemy import func
from app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(60))


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    messageDate = db.Column(db.DateTime, default=func.now())
    sender = db.Column(db.String(64), db.ForeignKey("users.id"))
    message = db.Column(db.Text)
