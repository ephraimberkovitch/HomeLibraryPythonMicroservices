#! /usr/bin/env python
import json
from datetime import datetime

from flask import Flask
from flask import request

from crossdomain import crossdomain
import server.microservices.books.bl.books_operations;

app = Flask(__name__)

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)

@app.route("/books")
@crossdomain(origin='*')
def get_books():
    return json.dumps(server.microservices.books.bl.books_operations.get_all_books(), cls=DateTimeEncoder)

@app.route("/insert_book")
@crossdomain(origin='*')
def insert_book():
    writers = request.args['w']
    title = request.args['t']
    series = request.args['s']
    volumes = request.args['v']
    copies = request.args['c']
    is_owned = int(request.args['o'])
    is_younger = int(request.args['y'])
    return json.dumps(
        server.microservices.books.bl.books_operations.insert_book(writers, title, series, volumes, copies, is_owned, is_younger))

@app.route("/delete_book")
@crossdomain(origin='*')
def delete_book():
    server.microservices.books.bl.books_operations.delete_book(request.args['id'])
    return "Ok"

@app.route("/update_book")
@crossdomain(origin='*')
def update_book():
    id = request.args['i']
    writers = request.args['w']
    title = request.args['t']
    series = request.args['s']
    volumes = request.args['v']
    copies = request.args['c']
    is_owned = request.args['o']
    is_younger = request.args['y']
    server.microservices.books.bl.books_operations.update_book(id, writers, title, series, volumes, copies, is_owned, is_younger)
    return'Ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5555)