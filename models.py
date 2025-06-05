from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Mood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    posts = db.relationship('Post', backref='mood', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #title = db.Column(db.String(100))  # Optional, or rename to caption if needed
    caption = db.Column(db.String(255))  # <- ADD THIS LINE
    image_url = db.Column(db.String(255), nullable=False)
    mood_id = db.Column(db.Integer, db.ForeignKey('mood.id'), nullable=False)
