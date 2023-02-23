from flask import Flask
import mongoengine as me
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    "db": "myapp",
}
db = MongoEngine(app)

class Imdb(me.EmbeddedDocument):
    imdb_id = me.StringField()
    rating = me.DecimalField()
    votes = me.IntField()

class Movie(me.Document):
    title = me.StringField(required=True)
    year = me.IntField()
    rated = me.StringField()
    director = me.StringField()
    actors = me.ListField()
    imdb = me.EmbeddedDocumentField(Imdb)
    