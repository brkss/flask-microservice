from flask import request 
import os
import json
from .init import create_app 
from .models import Book, db 
import uuid
from .validate import validate_adding_book_data

app = create_app()
print("name from app : ", __name__)

@app.route('/', methods=['GET'])
def fetch():
    return json.dumps({"success": True}), 200

@app.route('/books', methods=['GET'])
def books():
    books = Book.query.all()
    all_books = []
    for book in books:
        new_book = {
            "id": book.id,
            "name": book.name,
            "author": book.author,
            "price": book.price
        }
        all_books.append(new_book)
    return json.dumps(all_books), 200

@app.route('/add', methods=['POST'])
def add_book():
    data = request.get_json()
    print(data)
    if not validate_adding_book_data(data):
        return json.dumps({"success": False, "message": "Invalid Data !"}), 200
    name = data["name"];
    author = data["author"]
    price = data["price"]
    id = uuid.uuid4()
    book = Book(name=name, author=author, price=price, id=id)
    db.session.add(book)
    db.session.commit()
    return json.dumps({"success": True}), 200

if __name__ == '__main__':
    port = 5000
    app.run(debug=True, host='0.0.0.0', port=port)
