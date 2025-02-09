from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# configures database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# the book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"{self.book_name} written by {self.author} (Publisher: {self.publisher})"

# home
@app.route('/')
def index():
    return 'Yo this is the books db!'

# list books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    output= []
    for book in books:
        book_data = {"id": book.id, "book_name": book.book_name, "author": book.author, "publisher": book.publisher}
        output.append(book_data)
    return {"books": output}

# get single book with id
@app.route('/books/<id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"id": book.id, "book_name": book.book_name, "author": book.author, "publisher": book.publisher}

# add a book
@app.route('/books', methods=['POST'])
def add_book():
    book = Book(book_name=request.json['book_name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

# delete a book
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "yeet!@"}
