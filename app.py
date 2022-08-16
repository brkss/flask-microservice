from flask import Flask
import os
import json
from .init import create_app 
from .models import Book 

app = create_app()

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


if __name__ == '__main__':
    port = 5000
    app.run(debug=True, host='0.0.0.0', port=port)
