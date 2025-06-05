import os
from flask import Flask, render_template
from models import db, Mood, Post

# Set up instance folder and app
base_dir = os.path.abspath(os.path.dirname(__file__))
instance_path = os.path.join(base_dir, 'instance')
os.makedirs(instance_path, exist_ok=True)

app = Flask(__name__, instance_path=instance_path)

# Configure SQLite database inside the instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(app.instance_path, 'moodfeed.sqlite')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

@app.route('/')
def index():
    moods = Mood.query.all()
    return render_template("index.html", moods=moods)

@app.route('/mood/<mood_name>')
def mood_feed(mood_name):
    moods = Mood.query.all()
    mood = Mood.query.filter_by(name=mood_name.capitalize()).first_or_404()
    posts = Post.query.filter_by(mood_id=mood.id).all()
    return render_template("feed.html", mood=mood, posts=posts, moods=moods)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
