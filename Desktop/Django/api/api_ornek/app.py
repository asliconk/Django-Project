from flask import Flask, jsonify, request, abort

app = Flask(__name__)

books = [
    {"id": 1, "title": "Python Programming", "author": "John Doe"},
    {"id": 2, "title": "Web Development", "author": "Jane Smith"},
    {"id": 3, "title": "Mobil Development", "author": "Bella Green"},
    {"id": 4, "title": "Java Programming", "author": "Emily Blonde"}
    
]

# Tüm kitapları listeleme
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Belirli bir kitabı getirme
@app.route('/api/books/<int:id>', methods=['GET'])
def get_book(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        abort(404)
    return jsonify(book[0])

# Yeni bir kitap ekleme
@app.route('/api/books', methods=['POST'])
def add_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json.get('author', "")
    }
    books.append(book)
    return jsonify(book), 201

# Bir kitap güncelleme
@app.route('/api/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        abort(404)
    if not request.json:
        abort(400)
    book[0]['title'] = request.json.get('title', book[0]['title'])
    book[0]['author'] = request.json.get('author', book[0]['author'])
    return jsonify(book[0])

# Bir kitap silme
@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        abort(404)
    books.remove(book[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
