from flask import Blueprint, request, jsonify
from app.controllers.book_controller import get_all_books, create_book

book_bp = Blueprint('book_bp', __name__)

@book_bp.route('/books', methods=['GET'])
def list_books():
    books = get_all_books()
    return jsonify([book.to_dict() for book in books])
    #return jsonify([book.title for book in books])

@book_bp.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    book = create_book(data)
    return jsonify({"id": book.id, "title": book.title}), 201