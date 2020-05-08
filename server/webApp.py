import os
import uuid

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'books.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


class Book(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    read = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        return '<Book %r>' % self.title

BOOKS = [
    {
        'id': uuid.uuid4().hex[25:],
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex[25:],
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex[25:],
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

# routes
@app.route('/', methods=['GET'])
@app.route('/books', methods=['GET', 'POST'])
def books():
   return jsonify(BOOKS)

@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def book(book_id):
    return "A book"


    
if __name__ == '__main__':
    app.run(debug=True)