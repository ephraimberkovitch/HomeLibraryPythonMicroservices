#! /usr/bin/env python
from flask import Flask
from flask.ext.cors import CORS
import books.bl.books_operations
import json

app = Flask(__name__)
CORS(app)

@app.route("/books")
def get_books():
    return json.dumps(books.bl.books_operations.get_all_books())

if __name__ == '__main__':
    app.run(debug=True,port=5555)