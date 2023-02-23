import mongoengine as me
from flask_mongoengine import MongoEngine
import click
from flask import current_app, g
from flask import Flask

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    "db": "myapp",
}

def get_db():
    if 'db' not in g:
        g.db = MongoEngine(app)

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.disconnect()
        
class User(me.EmbeddedDocument):
    user_id = me.StringField()
    username = me.StringField()
    password = me.StringField()

class Post(me.Document):
    post_id = me.StringField()
    author_id = me.StringField()
    created = me.DateTimeField
    title = me.StringField()
    body = me.StringField()