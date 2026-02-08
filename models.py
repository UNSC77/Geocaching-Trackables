from app import db
from datetime import datetime

class Trackable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(8), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    locations = db.relationship('Location', backref='trackable', lazy=True)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trackable_id = db.Column(db.Integer, db.ForeignKey('trackable.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
