from flask import Flask, jsonify, request
from services.BookService import BookService

app = Flask(__name__)
service = BookService()

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify([book.to_dict() for book in service.get_all_books()])

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = service.get_book_by_id(book_id)
    return jsonify(book.to_dict()) if book else ('Not Found', 404)

@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    book = service.add_book(data['title'], data['author'], data['publisher'], data['isbn'])
    return jsonify(book.to_dict()), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    book = service.update_book(book_id, data.get('title'), data.get('author'), data.get('publisher'), data.get('isbn'))
    return jsonify(book.to_dict()) if book else ('Not Found', 404)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    success = service.delete_book(book_id)
    return ('Deleted', 204) if success else ('Not Found', 404)

if __name__ == '__main__':
    app.run(debug=True)